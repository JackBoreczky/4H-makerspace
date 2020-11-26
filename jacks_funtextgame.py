# understanding this see https://stackoverflow.com/a/509295

import shlex
import os
import subprocess

def handle(cmd,args):
	print(cmd)
	print(args)
	return_value = subprocess.call(cmd + " " + " ".join(args))
	print("the return value is ", return_value)

def main():
	while True:
		cmdargs=shlex.split(input(os.environ.get("PYFUNTEXTPROMPT",">")))
		cmd=cmdargs[0]
		args=cmdargs[1:]
		handle(cmd,args)

if __name__ == "__main__":
	main()
