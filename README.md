# osp-observability-ansible

Ansible playbooks to deploy and configure client side services (Collectd,
Ceilometer, QDR etc.) on OSP nodes.

Currently PoC, with some debugging info for test-role, which displays the
params passed from TripleO to the ansible playbook.

# NOTE - QDR and Collectd code has moved
* https://github.com/infrawatch/collectd-config-ansible-role
* https://github.com/infrawatch/qdr-config-ansible-role

## Setup

Install dependencies via `ansible-galaxy`.

```
ansible-galaxy install -r requirements.yml --roles-path ./roles/
```
