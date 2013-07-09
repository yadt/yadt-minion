import yadtminion
from yadtminion import Status


def load_yadt_defaults():
    try:
        return load_yadt_defaults_oldstyle()
    except BaseException:
        return load_yadt_defaults_newstyle()


def load_yadt_defaults_oldstyle():
    defaults = Status.load_defaults()
    return defaults


def load_yadt_defaults_newstyle():
    settings = yadtminion.yaml_merger.merge_yaml_files('/etc/yadt.conf.d/')
    return settings.get('defaults', {})
