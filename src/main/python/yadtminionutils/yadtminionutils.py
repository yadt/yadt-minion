import os
from yum import YumBase


def get_files_by_template(common_name, filename_templates):
    existing_files = []
    files_to_test = [template.format(common_name)
                     for template in filename_templates]
    for file_to_test in files_to_test:
        if os.path.exists(file_to_test):
            existing_files.append(file_to_test)
    return existing_files


def get_yum_releasever(yumbase=None):
    if not yumbase:
        yumbase = YumBase()
        yumbase.doConfigSetup(init_plugins=False)
    yum_releaseversion = yumbase.conf.yumvar['releasever']
    releasever = float(yum_releaseversion.lower().replace('server', ''))
    return releasever
