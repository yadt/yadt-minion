from yadtminion import Status

import unittest

class Test(unittest.TestCase):

    def test(self):
        yadt_minion = Status()
        yadt_minion.get_status()

if __name__ == "__main__":
    unittest.main()
