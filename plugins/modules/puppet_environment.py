#!/usr/bin/env python
# Copyright 2022 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from ansible.module_utils.basic import AnsibleModule
import traceback
import subprocess
import re
import sys
import json

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: puppet_environment

short_description: Loads Puppet configuration from hiera or facter

version_added: "2.9"

description:
    - "This module loads given Puppet configuration variables from hiera or
      environment variables from facter and saves it to ansible_facts"

options:
    variables:
        description:
            - List of variables to load
        required: true

author:
    - Martin Mágr (mmagr@redhat.com)
'''

EXAMPLES = '''
- name: Test module
  puppet_environment:
    variables:
      - os
      - enabled_services
      - cinder_api_network
'''

RETURN = '''
'''


puppet_hash_item = re.compile(r'(\S*) *=> *(\S+)')


def run_module():
    module = AnsibleModule(
        argument_spec={
            'variables': {
                'type': 'list',
                'required': True
            }
        },
        supports_check_mode=True
    )

    result = {}
    for var in module.params['variables']:
        result[var] = None
        if module.check_mode:
            continue
        for cmd in ('/usr/bin/lookup', '/usr/bin/hiera', '/usr/bin/facter'):
            try:
                run = subprocess.run([cmd, var], stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
            except FileNotFoundError:
                continue
            if run.returncode != 0:
                continue
            res = run.stdout.strip().decode('utf-8')
            if res in ("nil", ""):
                continue
            try:
                # json compatible hiera output
                result[var] = json.loads(res)
            except json.decoder.JSONDecodeError:
                orig = res
                if '=>' in res:
                    # facter output
                    res, n = puppet_hash_item.subn(r'"\1": \2', res)
                else:
                    # single hiera value not compatible with json
                    res = '"%s"' % res
                try:
                    result[var] = json.loads(res)
                except json.decoder.JSONDecodeError as ex:
                    trace = '\n'.join(traceback.format_tb(sys.exc_info()[2]))
                    module.fail_json(msg='Failed to decode variable %s' % var,
                                     error=str(ex), exception=trace,
                                     raw_value=orig)
                    break
    module.exit_json(changed=False, ansible_facts=result)


def main():
    run_module()


if __name__ == '__main__':
    main()
