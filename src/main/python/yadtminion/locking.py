import sys
import time
import yum


class CannotAcquireYumLockException(BaseException):
    pass


def try_to_acquire_yum_lock(yum_base):
    tries = 0
    max_tries = 10
    while True:
        tries += 1
        try:
            yum_base.doLock()
            return
        except yum.Errors.LockError, e:
            if e.errno:
                raise yum.Errors.YumBaseError, "Can't create yum lock file (%s); exiting" % str(e)
            if tries < max_tries:
                message = "Another app (pid %s) is currently holding the yum lock (try %d of %d)\n"
                sys.stderr.write(message % (e.pid, tries, max_tries))
                time.sleep(3)
            else:
                raise CannotAcquireYumLockException("Another app (pid %s) is currently holding the yum lock" % e.pid)
