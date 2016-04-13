from yadtminionutils import (get_files_by_template,
                             get_systemd_overrides,
                             is_sysv_service,
                             could_be_sysv_service)
import os
import shutil
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

    @patch("yadtminionutils.sysv_scripts.get_chkconfig_output")
    def test_is_sysv_service_should_return_correct_value(self, get_chkconfig_output_mock):
        get_chkconfig_output_mock.return_value = dedent("""
            service1    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            service2    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            ser3           	0:off   1:off   2:off   3:on    4:on    5:on    6:off
            service4    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            longservice5	0:off   1:off   2:off   3:on    4:on    5:on    6:off
            service6    	0:off   1:on    2:on    3:on    4:on    5:on    6:off
            """).strip()
        self.assertTrue(is_sysv_service("service1"))
        get_chkconfig_output_mock.assert_called_once_with()
        self.assertFalse(is_sysv_service("noservice"))

    @patch("yadtminionutils.sysv_scripts.get_chkconfig_output")
    def test_is_sysv_service_should_return_correct_value_with_xinetd(self, get_chkconfig_output_mock):
        get_chkconfig_output_mock.return_value = dedent("""
            service1    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            service2    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            ser3           	0:off   1:off   2:off   3:on    4:on    5:on    6:off
            service4    	0:off   1:off   2:on    3:on    4:on    5:on    6:off
            longservice5	0:off   1:off   2:off   3:on    4:on    5:on    6:off
            service6    	0:off   1:on    2:on    3:on    4:on    5:on    6:off

            xinetd based services:
                foobar-server:  on
            """).strip()
        self.assertTrue(is_sysv_service("service1"))
        get_chkconfig_output_mock.assert_called_once_with()
        self.assertFalse(is_sysv_service("noservice"))

    def test_could_be_sysv_service(self):
        service_name = "foo"
        tempdir = mkdtemp()
        script_path = os.path.join(tempdir, service_name)
        try:
            with patch("yadtminionutils.sysv_scripts.SYSV_SCRIPT_LOCATION", new=tempdir):
                self.assertEqual(could_be_sysv_service("foo"), False)

                open(script_path, "w").close()

                # File is not executable, so still expect False.
                self.assertEqual(could_be_sysv_service("foo"), False)

                os.chmod(script_path, 0755)
                self.assertEqual(could_be_sysv_service("foo"), True)
        finally:
            shutil.rmtree(tempdir)


if __name__ == "__main__":
    unittest.main()
