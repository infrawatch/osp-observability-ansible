FROM fedora:33

WORKDIR /opt

RUN dnf install -y rpmdevtools git-core

# RUN rpmdev-setuptree

COPY collectd-config-ansible-role.spec collectd-config-ansible-role.spec
COPY qdr-config-ansible-role.spec qdr-config-ansibe-role.spec

# RUN rpmbuild -bb collectd-config-ansible-role.spec

COPY build_rpms.sh entrypoint.sh

ENTRYPOINT ["/bin/bash", "/opt/entrypoint.sh"]
