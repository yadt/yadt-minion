import os
from .yadtminionutils import get_files_by_template


def get_systemd_overrides(service_name, override_path_template='/etc/systemd/system/{0}.d'):
    overrides = []
    override_path = override_path_template.format(service_name)
    if os.path.isdir(override_path):
        for override_file in os.listdir(override_path):
            full_path = os.path.join(override_path, override_file)
            if os.path.isfile(full_path):
                overrides.append(full_path)
    return overrides


def get_systemd_init_scripts(service_name):
    init_scripts_templates = ['/usr/lib/systemd/system/{0}.service',
                              '/etc/systemd/system/{0}.service']
    return tuple(get_files_by_template(service_name, init_scripts_templates) +
                 get_systemd_overrides(service_name))
