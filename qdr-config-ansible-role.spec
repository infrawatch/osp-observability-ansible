%global srcname qdr_config_ansible_role
%global rolename qdr-config

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-%{rolename}
Version:        master
Release:        1
Summary:        Ansible role for creating qdr configs

Group:          TODO
License:        ASL 2.0
URL:            https://github.com/infrawatch/qdr-config-ansible-role
Source0:        https://github.com/infrawatch/qdr-config-ansible-role/archive/%{upstream_version}/qdr-config-ansible-role-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core

Requires:       python3dist(ansible)

%description

Ansible role for creating qdr configs

%prep
%autosetup -n qdr-config-ansible-role-%{upstream_version} -S git


%build


%install
mkdir -p  %{buildroot}%{_datadir}/ansible/roles/qdr_config
cp -r ./* %{buildroot}%{_datadir}/ansible/roles/qdr_config


%files
%doc README*
%license LICENSE
%{_datadir}/ansible/roles/qdr_config

%changelog

