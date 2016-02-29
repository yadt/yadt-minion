from sh import Command


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
