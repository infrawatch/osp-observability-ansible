#! /bin/sh -l

ls
pwd

rpmdev-setuptree

VERSION=0
RELEASE=0
UPSTREAM_VERSION=master

# TODO: make upstream_version, release and specfile configurable
spectool -g --define 'upstream_version master' --define 'version 0' --define 'release 0' --directory $HOME/rpmbuild/SOURCES/ collectd-config-ansible-role.spec

rpmbuild -bb --define 'upstream_version master' --define 'version 0' --define 'release 0' collectd-config-ansible-role.spec

ls /usr/share/ansible/roles/

ls -R $HOME/rpmbuild

ls $HOME/rpmbuild/RPMS/noarch/
dnf install -y $HOME/rpmbuild/RPMS/noarch/ansible-collectd-config-${VERSION}-${RELEASE}.noarch.rpm

ls /usr/share/ansible/roles/
