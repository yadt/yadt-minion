import os
import stat

from sh import Command

SYSV_SCRIPT_LOCATION = "/etc/init.d"


def is_sysv_service(service_name):
    chkconfig = Command("/sbin/chkconfig")
    sysv_services = []
    for line in chkconfig():
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
