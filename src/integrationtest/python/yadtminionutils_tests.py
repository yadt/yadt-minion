from yadtminionutils import (get_files_by_template,
                             get_systemd_overrides,
                             is_sysv_service)
import os
from textwrap import dedent

import unittest2 as unittest
from mock import patch, Mock
from tempfile import NamedTemporaryFile, mkdtemp


class Test(unittest.TestCase):
    def test_get_files_by_template_should_return_files_list(self):
        service = "testservice"
        tempfile1 = NamedTemporaryFile()
        tempfile2 = NamedTemporaryFile()
        expected_list = [tempfile1.name, tempfile2.name]

        result_list = get_files_by_template(service, expected_list)
        self.assertItemsEqual(expected_list, result_list)

    def test_get_files_by_template_should_return_only_existing_files(self):
        service = "testservice"
        tempfile = NamedTemporaryFile()
        expected_list = [tempfile.name]
        result_list = get_files_by_template(service, [tempfile.name, "non_existing_file"])
        self.assertListEqual(expected_list, result_list)

    def test_get_files_by_template_should_return_empty_list(self):
        service = "testservice"
        expected_list = []
        result_list = get_files_by_template(service, ["non_existing_file", "non_existing_file"])
        self.assertItemsEqual(expected_list, result_list)
        result_list = get_files_by_template(service, ["non_existing_file"])
        self.assertItemsEqual(expected_list, result_list)
        result_list = get_files_by_template(service, [])
        self.assertItemsEqual(expected_list, result_list)

    def test_get_systemd_overrides_should_return_list_files(self):
        service = "testservice"
        override_dir = mkdtemp()
        override1 = NamedTemporaryFile(dir=override_dir)
        override2 = NamedTemporaryFile(dir=override_dir)
        expected_list = [override1.name, override2.name]
        result_list = get_systemd_overrides(service, override_path_template=override_dir)
        self.assertItemsEqual(expected_list, result_list)
        override1.close()
        override2.close()
        os.rmdir(override_dir)

    def test_get_systemd_overrides_should_return_empty_list_no_files(self):
        service = "testservice"
        override_dir = mkdtemp()
        expected_list = []
        result_list = get_systemd_overrides(service, override_path_template=override_dir)
        self.assertItemsEqual(expected_list, result_list)
        os.rmdir(override_dir)

    def test_get_systemd_overrides_should_return_empty_list_no_directory(self):
        service = "testservice"
        override_dir = "nonexistent_dir"
        expected_list = []
        result_list = get_systemd_overrides(service, override_path_template=override_dir)
        self.assertItemsEqual(expected_list, result_list)

    @patch("yadtminionutils.sysv_scripts.Command")
    def test_is_sysv_service_should_return_correct_value(self, command):
        chkconfigmock = Mock()
        chkconfigmock.return_value = dedent("""
            service1    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            service2    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            ser3           	0:off   1:off   2:off   3:on    4:on    5:on    6:off
            service4    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            longservice5	0:off   1:off   2:off   3:on    4:on    5:on    6:off
            service6    	0:off   1:on    2:on    3:on    4:on    5:on    6:off
            """).strip().split("\n")
        command.return_value = chkconfigmock
        self.assertTrue(is_sysv_service("service1"))
        chkconfigmock.assert_called_once_with()
        self.assertFalse(is_sysv_service("noservice"))

    @patch("yadtminionutils.sysv_scripts.Command")
    def test_is_sysv_service_should_return_correct_value_with_xinetd(self, command):
        chkconfigmock = Mock()
        chkconfigmock.return_value = dedent("""
            service1    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            service2    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            ser3           	0:off   1:off   2:off   3:on    4:on    5:on    6:off
            service4    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            longservice5	0:off   1:off   2:off   3:on    4:on    5:on    6:off
            service6    	0:off   1:on    2:on    3:on    4:on    5:on    6:off

            xinetd based services:
                foobar-server:  on
            """).strip().split("\n")
        command.return_value = chkconfigmock
        self.assertTrue(is_sysv_service("service1"))
        chkconfigmock.assert_called_once_with()
        self.assertFalse(is_sysv_service("noservice"))


if __name__ == "__main__":
    unittest.main()
