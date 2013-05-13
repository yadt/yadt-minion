import unittest
import sys
import subprocess
import os
import shutil



class SystemTests(unittest.TestCase):

    def tearDown(self):
        finish()

    def test_that_always_fails(self):
        setup_env(boxes=[('testbox1', 'yadtclient')])
        test_in_box('testbox1', 'test.py')





def execute(command):
    call_result = subprocess.call(command,
                                  stderr=open(os.devnull, 'w'),
                                  stdout=sys.stdout,
                                  shell=True,
                                  executable='/bin/bash',
                                  env=os.environ.copy())
    if call_result != 0:
        raise RuntimeError('Process "{0}"" exited with code {1}'.format(command, call_result))

def setup_env(boxes):
    execute('git clone https://github.com/yadt/yadt-vagrant-env /tmp/test-env')
    for box in boxes:
        box_name, box_role = box
        os.mkdir('/tmp/test-env/boxes/{0}'.format(box_name))

        fd = open('/tmp/test-env/boxes/{0}/role'.format(box_name), 'w')
        fd.write('{0}\n'.format(box_role))
        fd.close()

        shutil.copytree('src/systemtest', '/tmp/test-env/boxes/{0}/systemtest'.format(box_name))


    os.chdir('/tmp/test-env')
    execute('./provision-boxes')

def test_in_box(box, test_file_name):
    os.chdir('/tmp/test-env')
    os.chdir('boxes/{0}'.format(box))
    execute('vagrant ssh -c "python /vagrant/systemtest/{0}"'.format(test_file_name))

def finish():
    os.chdir('/tmp/test-env')
    execute('./destroy _all')
    shutil.rmtree('/tmp/test-env')


if __name__ == '__main__':
    unittest.main()
