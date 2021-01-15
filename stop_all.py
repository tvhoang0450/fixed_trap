import os
import time
import random

def run_opencanary():
	os.system(' sudo ansible-playbook plbook_stop_opencanary.yml'),
def run_honeypy():
	os.system(' sudo ansible-playbook plbook_stop_honeypy.yml'),
def run_dionaea():
	os.system(' sudo ansible-playbook plbook_stop_dionaea.yml'),
def run_cowrie():
	os.system(' sudo ansible-playbook plbook_stop_cowrie.yml'),
run_opencanary()
run_honeypy()
run_dionaea()
run_cowrie()
