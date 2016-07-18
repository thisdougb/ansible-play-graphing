#!/usr/bin/python
#
# Simple parser, version 0.0, but working.
#

import os
import sys
from collections import namedtuple

from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.playbook import Playbook
from ansible.playbook.task import Task
from ansible.utils.unicode import to_unicode

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
display = Display()

variable_manager = VariableManager()
loader = DataLoader()

inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list='./sample_hosts')
playbook_path = 'sample.yml'

if not os.path.exists(playbook_path):
    print '[INFO] The playbook does not exist'
    sys.exit()

Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])
options = Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=100, remote_user='slotlocker', private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method=None, become_user='root', verbosity=None, check=False)

variable_manager.extra_vars = {'hosts': 'mywebserver'} # This can accomodate various other command line arguments.`

passwords = {}

pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=passwords)
print pbex._playbooks

for playbook_path in pbex._playbooks:
  pb = Playbook.load(playbook_path, variable_manager=pbex._variable_manager, loader=pbex._loader)
  plays = pb.get_plays()
  for play in plays:
    print play.get_name()
    tasklist = play.get_tasks() # play.get_tasks() returns a merged list of task blocks (pre, post, etc)
    for taskBlocks in tasklist:
        for task in taskBlocks:
          changed = Task._get_parent_attribute(task, "changed_when")
          print task
          if (changed is not None):
              print "      changed_when: " + str(changed)
