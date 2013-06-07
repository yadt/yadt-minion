from status import Status

import unittest

class Test(unittest.TestCase):

    def test(self):
        yadt_minion = Status()
        yadt_minion.status()
