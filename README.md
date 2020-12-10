# osp-observability-ansible

Spec files for packaging STF client side ansible roles.

## Instructions for testing

1. Instantiate your build environment, according to https://rpm-packaging-guide.github.io/#rpm-packaging-workspace

```
   rpmdev-setuptree
```

2. Download the source files into your build environment

```
   spectool -g --define 'upstream_version master' --directory rpmbuild/SOURCES/ osp-observability-ansible/collectd-config-ansible-role.spec
   spectool -g --define 'upstream_version master' --directory rpmbuild/SOURCES/ osp-observability-ansible/qdr-config-ansible-role.spec
```

3. Build the rpms, according to https://rpm-packaging-guide.github.io/#binary-rpms

```
   rpmbuild -bb --define 'upstream_release master' osp-observability-ansible/collectd-config-ansible-role.spec
   rpmbuild -bb --define 'upstream_release master' osp-observability-ansible/qdr-config-ansible-role.spec

```

4.
```
   sudo dnf install rpmbuild/RPMS/noarch/ansible-collectd-config-0.1-1.noarch.rpm
   sudo dnf install rpmbuild/RPMS/noarch/ansible-qdr-config-0.1-1.noarch.rpm
```

Alternatively, you can use mock, and rplace steps 3 and 4 above:

3.
```
rpmbuild -bs --define 'upstream_release master' osp-observability-ansible/qdr-config-ansible-role.spec
```

4.
```
  sudo mock -r epel-7-x86_64 ~/rpmbuild/SRPMS/ansible-qdr-config-master-1.src.rpm
```
