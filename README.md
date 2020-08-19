# osp-observability-ansible

Ansible playbooks to deploy and configure client side services (Collectd,
Ceilometer, QDR etc.) on OSP nodes.

Currently PoC, with some debugging info for test-role, which displays the
params passed from TripleO to the ansible playbook.

## Setup

Install dependencies via `ansible-galaxy`.

```
ansible-galaxy install -r requirements.yml --roles-path ./roles/
```
