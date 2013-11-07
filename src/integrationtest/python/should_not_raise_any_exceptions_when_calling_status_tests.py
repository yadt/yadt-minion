import yadtminion
from yadtminion import Status

import unittest
from mock import patch


class Test(unittest.TestCase):

    @patch('yadtminion.Status.load_defaults')
    def test(self, load_defaults):
        load_defaults.return_value = {'YADT_LOCK_DIR': '/tmp/yadt-lock/',
                                      'YADT_LOG_DIR': '/tmp/yadt/',
                                      'YADT_SERVICES_FILE': '/etc/yadt.services'}
        yadt_minion = Status()
        yadt_minion.get_status()

if __name__ == "__main__":
    unittest.main()
