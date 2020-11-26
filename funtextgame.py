# understanding this see https://stackoverflow.com/a/509295

import shlex
import os

def handle_jack(cmd,args):
	print(cmd)
	print(args)

## DEFINE CMDS HERE
def cmd_fly(args):
	print("i can fly!")

cmddict={}
## ADD CMDS TO CMDDICT HERE
cmddict["fly"]=cmd_fly

def handle(cmd,args):
	print(cmd)
	print(args)
	cmddict[cmd](args)


def main():
	while True:
		cmdargs=shlex.split(input(os.environ.get("PYFUNTEXTPROMPT",">")))
		if len(cmdargs)>0:
			cmd=cmdargs[0]
			args=cmdargs[1:]
			handle(cmd,args)

if __name__ == "__main__":
	main()
