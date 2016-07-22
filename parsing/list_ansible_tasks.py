#!/usr/bin/env python
#
# list out ansible tasks from a compiled playbook, including changed_when and failed_when
# conditions.   Note: this uses ansible 2.0, where conditions are string, in 2.1 they
# are lists.
#
# $ python list_ansible_tasks.py
# PLAY: test play, ROLE: common, TASK: common : update hostname, changed_when: false, failed_when: s == 1
#

import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.block import Block
from ansible.playbook.play import Play
from ansible.playbook import Playbook

# initialize needed objects

# https://github.com/ansible/ansible/blob/devel/lib/ansible/vars/__init__.py
#
# manages extra_vars, host_vars, group_vars, inventory (supplied below), options_vars, etc.
# use variable_manager.get_vars() to access vars after order of precedence was applied.
variable_manager = VariableManager()


# https://github.com/ansible/ansible/blob/devel/lib/ansible/parsing/dataloader.py
#
# Object supplying methods to load JSON or YAML from file or string, into a Python data structure.
loader = DataLoader()

# https://github.com/ansible/ansible/blob/devel/lib/ansible/inventory/__init__.py
#
# Builds the inventory as a data structure (including groups), object also caches host and group vars.
# Loader supplies JSON/YAML parsing methods, variable_manager allows object to copy (cache) vars data
inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')

# Here we simply copy back the inventory data into the central variable_manager.
variable_manager.set_inventory(inventory)

# https://github.com/ansible/ansible/blob/devel/lib/ansible/playbook/__init__.py
#
# We use the Playbook object to load and then create Play objects from YAML files.  Playbook
# will load and parse the YAML data into the Playbook.entries[] list.
# Playbook.load() is a static method that calls Playbook.__init__
playbook = Playbook.load("test/site.yml", variable_manager, loader)

# Now we have the playbook loaded we can loop through the plays.  A play is a list of roles
# and/or tasks/handler blocks to execute on a set of hosts.
# see definition: https://github.com/ansible/ansible/blob/devel/lib/ansible/playbook/play.py
for play in playbook.get_plays():
    for block in play.compile():
        if block.has_tasks():
            for task in block.block:
                if task._role in play.get_roles():
                    changed = str(task._get_parent_attribute('changed_when'))
                    failed = str(task._get_parent_attribute('failed_when'))
                    print("PLAY: %s, ROLE: %s, %s, changed_when: %s, failed_when: %s" % (play.get_name(), task._role, task, changed, failed))
