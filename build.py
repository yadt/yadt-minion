#   YADT - an Augmented Deployment Tool
#   Copyright (C) 2010-2014  Immobilien Scout GmbH
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pybuilder.core import use_plugin, init, Author, task
from pybuilder.utils import assert_can_execute


use_plugin('python.core')
use_plugin('python.integrationtest')
use_plugin('python.install_dependencies')
use_plugin('python.flake8')

use_plugin('python.distutils')
use_plugin('python.pydev')

use_plugin('copy_resources')


authors = [Author('Arne Hilmann', 'arne.hilmann@gmail.com')]
description = """YADT - an Augmented Deployment Tool - The Minion Part
- yadt-status: collects all relevant information for a single host

for more documentation, visit http://www.yadt-project.org/
"""

name = 'yadt-minion'
license = 'GNU GPL v3'
summary = 'YADT - an Augmented Deployment Tool - The Minion Part'
url = 'https://github.com/yadt/yadt-minion'
version = '0.4'

default_task = ['analyze', 'publish']


@init
def set_properties(project):
    import os

    project.build_depends_on('mock')
    project.depends_on('PyYAML')
    project.depends_on('netifaces')
    project.depends_on('simplejson')
    project.depends_on('pyrpm')

    project.set_property('dir_dist_scripts', 'scripts')

    project.set_property('copy_resources_target', '$dir_dist')
    project.get_property('copy_resources_glob').append('setup.cfg')
    project.get_property('copy_resources_glob').append('docs/man/*')

    #  install man pages
    for manpage in os.listdir('docs/man/'):
        project.install_file('share/man/man1/', 'docs/man/%s' % manpage)

    project.install_file('/etc/yadt.conf.d/', 'yadtminion/00_defaults.yaml')
    project.install_file('/etc/default/', 'yadtminion/yadt')

    project.get_property('distutils_commands').append('bdist_rpm')
    project.set_property('distutils_classifiers', [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Topic :: System :: Networking',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration'
    ])


@init(environments='teamcity')
def set_properties_for_teamcity_builds(project):
    import os
    project.version = '%s-%s' % (project.version, os.environ.get('BUILD_NUMBER', 0))
    project.default_task = ['install_build_dependencies', 'publish']
    project.set_property('install_dependencies_index_url', os.environ.get('PYPIPROXY_URL'))
    project.set_property('install_dependencies_use_mirrors', False)


@task
def generate_manpage_with_pandoc(project, logger):
    import os
    import shutil
    import subprocess
    assert_can_execute(['pandoc', '-v'], 'pandoc', 'generate_manpage_with_pandoc')
    subprocess.check_output('pandoc -s -t man man-yadtminion.md -o docs/man/yadtminion.1.man', shell=True)
    subprocess.check_output('rm -f docs/man/yadtminion.1.man.gz && gzip -9 docs/man/yadtminion.1.man', shell=True)

    for script in os.listdir('src/main/scripts'):
        script_manpage = '%s.1.man.gz' % script
        shutil.copyfile('docs/man/yadtminion.1.man.gz', 'docs/man/%s' % script_manpage)
