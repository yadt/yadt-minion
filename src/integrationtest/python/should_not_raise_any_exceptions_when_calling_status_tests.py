import yadtminion
from yadtminion import Status

import unittest
from mock import patch


class Test(unittest.TestCase):

    @patch("yadtminion.yaml_merger.merge_yaml_files")
    def test(self, load_settings):
        load_settings.return_value = {"defaults": {'YADT_LOG_DIR': '/tmp/yadt/log',
                                                   'YADT_LOCK_DIR': '/tmp/yadt/',
                                                   'YADT_EXITCODE_HOST_LOCKED': 150,
                                                   'YADT_EXITCODE_SERVICE_IGNORED': 151,
                                                   'YADT_EXITCODE_HOST_REBOOT_TIMEOUT': 152}}
        yadt_minion = Status()
        yadt_minion.get_status()

if __name__ == "__main__":
    unittest.main()
