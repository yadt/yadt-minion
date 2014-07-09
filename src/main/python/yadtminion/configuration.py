import yadtminion
from yadtminion import Status
import os


def load_yadt_defaults():
    if os.path.exists('/etc/yadt.services'):
        return load_yadt_defaults_oldstyle()
    else:
        return load_yadt_defaults_newstyle()


def load_yadt_defaults_oldstyle():
    defaults = Status.load_defaults()
    return defaults


def load_yadt_defaults_newstyle():
    settings = yadtminion.yaml_merger.merge_yaml_files('/etc/yadt.conf.d/')
    return settings.get('defaults', {})
