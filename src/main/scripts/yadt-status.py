#!/usr/bin/env python

from yadtminion import Status

import simplejson as json

ys = Status()

print json.dumps(ys.get_status(), sort_keys=True, indent=4)
