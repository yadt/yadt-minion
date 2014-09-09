import yadtminion
from yadtminion import Status
import os


def load_yadt_defaults():
    if os.path.isfile('/etc/yadt.services'):
        raise RuntimeError("/etc/yadt.services is unsupported, please migrate to /etc/yadt.conf.d : https://github.com/yadt/yadtshell/wiki/Host-Configuration")
    else:
        return load_yadt_defaults_newstyle()


def load_yadt_defaults_newstyle():
    settings = yadtminion.yaml_merger.merge_yaml_files('/etc/yadt.conf.d/')
    return settings.get('defaults', {})
