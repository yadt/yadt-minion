#!/usr/bin/env python

import yadtminion
import sys

status = yadtminion.Status()
if status.host_is_up_to_date():
    sys.exit(0)
else:
    sys.exit(1)
