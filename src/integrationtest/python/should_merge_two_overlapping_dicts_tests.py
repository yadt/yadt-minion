from yadtminion import yaml_merger

import json
import unittest

class Test(unittest.TestCase):

    def test(self):
        test_dir = "src/integrationtest/resources/two_overlapping_dicts/"
        data = yaml_merger.merge_yaml_files(test_dir)
        print json.dumps(data, sort_keys=True, indent=4)
        self.assertEquals(data, {"a": "bar"})

if __name__ == "__main__":
    unittest.main()
