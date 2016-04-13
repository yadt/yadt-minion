import os
import stat
import subprocess

SYSV_SCRIPT_LOCATION = "/etc/init.d"


def get_chkconfig_output():
    with open(os.devnull, 'w') as devnull:
        return subprocess.Popen(["/sbin/chkconfig"],
                                stdout=subprocess.PIPE,
                                stderr=devnull,
                                ).communicate()[0]


def is_sysv_service(service_name):
    chkconfig_output = get_chkconfig_output()
    sysv_services = []
    for line in chkconfig_output.split("/n"):
        line = line.strip()
        if not line:
            # Empty line is the start of the "xinetd based services" section.
            break
        sysv_services.append(line.split()[0])
    return service_name in sysv_services


def could_be_sysv_service(service_name):
    """Return True if /etc/init.d/<service_name> exists and is executable"""
    script_path = os.path.join(SYSV_SCRIPT_LOCATION, service_name)
    try:
        script_permissions = os.stat(script_path).st_mode
    except OSError:
        return False

    script_is_executable = script_permissions & stat.S_IXUSR
    return True if script_is_executable else False
