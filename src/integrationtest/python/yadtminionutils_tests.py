from yadtminionutils import get_files_by_template, get_systemd_overrides
import os

import unittest2 as unittest
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

if __name__ == "__main__":
    unittest.main()
