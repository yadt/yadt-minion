import yadtminion
from yadtminion import Status

import unittest
from mock import patch


class Test(unittest.TestCase):

    @patch('yadtminion.Status.load_defaults')
    @patch('yadtminion.Status.load_services_oldstyle')
    def test(self, load_services_oldstyle, load_defaults):
        load_services_oldstyle.return_value = {}
        load_defaults.return_value = {'YADT_LOCK_DIR': '/tmp/yadt-lock/',
                                      'YADT_LOG_DIR': '/tmp/yadt/',
                                      'YADT_SERVICES_FILE': '/etc/yadt.services'}
        yadt_minion = Status()
        yadt_minion.get_status()

if __name__ == "__main__":
    unittest.main()
