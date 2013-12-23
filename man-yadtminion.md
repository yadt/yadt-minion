% YADTminion(1) YADTminion User Manuals
% The YADT project team
% December 23rd, 2013

# NAME

yadtminion - yadt, an augmented deployment tool: the minion part

# SYNOPSIS

yadt-status

# DESCRIPTION

The *yadtminion* provides scripts and utilities used remotely by 
the *yadtshell* to orchestrate hosts and services.
These tools are (mostly) not fit for direct usage but should rather be used through appropriate *yadtshell* commands.

# STATUS COMMAND
The *yadt-status* commands yields full information about the local host on
standard output in JSON format.

Interesting parts are :

 * current_artefacts
   A list with the artefacts currently installed.
 * latest_kernel
   The latest kernel available from the configured repos.
 * next_artefacts
   Incoming artefacts that can be installed during the next update.
   This is a JSON object where keys are the updating package and values are
   the package that is going to be updated.
 * services
   JSON object where keys are service names and values are service definitions.

# CONFIGURATION
The *yadt-config-services* program can be used to determine the service configuration of the current host. This will work with either modularized services (yadt.conf.d) or monolithic services (yadt.services).

# HELPER SCRIPTS
There are several helper scripts that should usually not be called directly by users.

 * yadt-artefact-update : 
 Updates one or several artefacts without regarding service dependencies.
 * yadt-command : 
 Wrapper script that logs output and prepares environment.
 * yadt-config-services : 
 See *CONFIGURATION* above.
 * yadt-host-checkaccess : 
 Checks if the host can be accessed or if it is locked by another user.
 * yadt-host-lock : 
 Locks this host.
 * yadt-host-status : 
 Checks if the current host is up to date.
 * yadt-host-status.py : 
 Checks if the current host is up to date.
 * yadt-host-unlock : 
 Unlocks this host.
 * yadt-host-update : 
 Updates this host, optionally with a reboot afterwards.
 * yadt-service-checkaccess : 
 Checks if the service can be altered, or if it is locked or ignored.
 * yadt-service-ignore : 
 Ignores a service.
 * yadt-service-start : 
 Starts a service.
 * yadt-service-status : 
 Queries the state of a service.
 * yadt-service-stop : 
 Stops a service.
 * yadt-service-unignore : 
 Unignores a service.
 * yadt-status : 
 Queries the status of this host. See *STATUS COMMAND* above for more information.
 * yadt-status.py : 
 Queries the status of this host. See *STATUS COMMAND* above for more information.
 * yadt-yum : 
 Deprecation warning.

# SEE ALSO

the yadt project
:   http://www.yadt-project.org/

sources at github
:   https://github.com/yadt/yadt-minion

Alternatives
:   puppet, chef

# LICENSE

Licensed under the GNU General Public License (GPL), see http://www.gnu.org/licenses/gpl.txt for full license text.
