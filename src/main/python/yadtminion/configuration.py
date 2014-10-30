import yadtminion
import os
import sys


def load_yadt_defaults():
    if os.path.isfile('/etc/yadt.services'):
        sys.stderr.write(
            "/etc/yadt.services is unsupported, please migrate to /etc/yadt.conf.d : https://github.com/yadt/yadtshell/wiki/Host-Configuration\n")
        sys.exit(1)
    else:
        return load_yadt_defaults_newstyle()


def load_yadt_defaults_newstyle():
    settings = yadtminion.yaml_merger.merge_yaml_files('/etc/yadt.conf.d/')
    return settings.get('defaults', {})
