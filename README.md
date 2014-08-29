# [YADT-minion](http://yadt-project.org)
[![Build Status](https://travis-ci.org/yadt/yadt-minion.svg?branch=master)](https://travis-ci.org/yadt/yadt-minion)

# try-it-out

If you want to try out how ```yadt``` works, please check out our [how to](https://github.com/yadt/try-it-yourself) and the [project](http://www.yadt-project.org/) page.

## the Yadt concept

![concept yadtshell and yadtminion](https://raw.githubusercontent.com/yadt/try-it-yourself/master/images/yadtshell_to_yadtminion.png)

The ```yadtshell```(server part) controls hosts with a ```yadt-minion```(client part) via ```passwordless ssh``` with a minimal configuration, it handles service dependencies and package updates.
- A```target``` is a set of hosts which belong together [[wiki](https://github.com/yadt/yadtshell/wiki/Target)]
- A```service``` in yadt is the representation of a service on a host with a LSB compatible init script
- A```service dependency``` is the dependency between two services and its not limited to a service on the same host. (e.g httpd -> loadbalancer) [[wiki](https://github.com/yadt/yadtshell/wiki/Metatargets,-Dependencies-and-Readonly-Services)]

## developer setup

### prerequisites
- ```git```
- ```python 2.6/2.7```
- ```virtualenv```
- ```yum```
(RHEL based Operating system or install yum via package management, **no chance on macos**
)

### getting started

```bash
git clone https://github.com/yadt/yadt-minion
cd yadt-minion
virtualenv venv
. venv/bin/activate
pip install pybuilder
pyb install_dependencies
```

The yadt project is using the pybuilder as a build automation tool for python. The yadt-minion project has a clear project structure.

```
src
├── integrationtest
│   ├── python # here you can find the integration tests, the tests have to end with ```*_tests.py```
│   └── resources
│       ├── recursive_dicts
│       ├── two_nonoverlapping_dicts
│       └── two_overlapping_dicts
└── main
    ├── python
    │   └── yadtminion # here you can find the program modules
    └── scripts # for the executable scripts
```

### running the tests
```bash
pyb verify
```

### running code linting

```bash
pyb analyze
```

### generating a setup.py
```bash
pyb
cd target/dist/yadt-minion-$VERSION
./setup.py <whatever you want>
```

### running all tasks together
```bash
pyb
```

## find help

[issues page](https://github.com/yadt/yadt-minion/issues)

[twitter](https://twitter.com/yadtproject)
