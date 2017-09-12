#!/usr/bin/env python
# -*- coding=utf-8 -*-

from ansible.module_utils.basic import *
import commands

module = AnsibleModule(
        argument_spec = dict(),
)
status,output = commands.getstatusoutput('''nova hypervisor-stats''')
if status == 0:
    result = dict(module='timezone', stdout=output, changed=False, rc=0)
    module.exit_json(**result)
else:
    result = dict(msg='execute failed', rc=status)
    module.fail_json(**result)