from sh import Command


def is_sysv_service(service_name):
    chkconfig = Command("/sbin/chkconfig")
    sysv_services = [line.split()[0] for line in chkconfig()]
    return service_name in sysv_services
