# understanding this see https://stackoverflow.com/a/509295

import shlex

def handle(cmd,args):
	print(cmd)
	print(args)

def main():
	while True:
		cmdargs=shlex.split(input(">"))
		cmd=cmdargs[0]
		args=cmdargs[1:]
		handle(cmd,args)

if __name__ == "__main__":
	main()
