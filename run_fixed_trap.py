import os
import time
import random
#while 1:
#	os.system(' sudo ansible-playbook plbook_start.yml')
#	time.sleep(60)
#	os.system(' sudo ansible-playbook plbook_stop.yml')
#	time.sleep(60)

def run_opencanary():
	os.system('python3 stop_all.py'),
	os.system(' sudo ansible-playbook plbook_start_opencanary.yml'),
def run_honeypy():
	os.system('python3 stop_all.py'),
	os.system(' sudo ansible-playbook plbook_start_honeypy.yml'),
def run_dionaea():
	os.system('python3 stop_all.py'),
	os.system(' sudo ansible-playbook plbook_start_dionaea.yml'),
def run_cowrie():
	os.system('python3 stop_all.py'),
	os.system(' sudo ansible-playbook plbook_start_cowrie.yml'),

def run_random_opencanary():
	os.system('python3 stop_all.py'),
	os.system(' sudo ansible-playbook plbook_start_random_opencanary.yml'),
def run_random_honeypy():
	os.system('python3 stop_all.py'),
	os.system(' sudo ansible-playbook /home/host/plbook_start_random_honeypy.yml'),
def run_random_dionaea():
	os.system('python3 stop_all.py'),
	os.system(' sudo ansible-playbook plbook_start_random_dionaea.yml'),
def run_random_cowrie():
	os.system('python3 stop_all.py'),
	os.system(' sudo ansible-playbook plbook_start_random_cowrie.yml'),
 

def choice_trap():
	print(	'0: Opencanary',
        	'1: HoneyPy',
		'2: Dionaea',
		'3: Cowrie'	)
	int2 = int(input())
	switcher={
		0: run_opencanary,
                1: run_honeypy,
		2: run_dionaea,
		3: run_cowrie
             }
	func = switcher.get(int2,lambda :"Invalid choice")
	return func()


def random_trap():
	while(1):
		int2 = random.randint(0,3)
		#int2=1
		switcher={
			0: run_random_opencanary,
                	1: run_random_honeypy,
			2: run_random_dionaea,
			3: run_random_cowrie
             	}
		func = switcher.get(int2,lambda :"Invalid choice")
		return func()
		#time.sleep(30)

def rd1():
	while(1):
		random_trap()

def choice(i):
	switcher={
		#0: random_trap,
		0: rd1,
                1: choice_trap
             }
	func = switcher.get(i,lambda :"Invalid choice")
	return func()

print(	'0: Random',
        '1: Select trap',)

# input
int1 = int(input()) 
print(choice(int1))



