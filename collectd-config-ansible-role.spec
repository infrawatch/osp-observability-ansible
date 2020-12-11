%global srcname collectd_config_ansible_role
%global rolename collectd-config

%{!?version: %global version 0.1}
%{!?release: %global release 1}

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
#%{?_version: %global version %{_version}}

Name:           ansible-%{rolename}
Version:        %{version}
Release:        %{release}
Summary:        Ansible role for creating collectd configs

Group:          TODO
License:        ASL 2.0
URL:            https://github.com/infrawatch/collectd-config-ansible-role
Source0:        https://github.com/infrawatch/collectd-config-ansible-role/archive/%{upstream_version}/collectd-config-ansible-role-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core

Requires:       python3dist(ansible)

%description

Ansible role for creating collectd configs

%prep
%autosetup -n collectd-config-ansible-role-%{upstream_version} -S git


%build


%install
mkdir -p  %{buildroot}%{_datadir}/ansible/roles/collectd_config
cp -r ./* %{buildroot}%{_datadir}/ansible/roles/collectd_config


%files
%doc README*
%license LICENSE
%{_datadir}/ansible/roles/collectd_config
%exclude %{_datadir}/ansible/role/collectd_config/tests/*

%changelog

