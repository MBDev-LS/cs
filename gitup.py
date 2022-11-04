
def removeItemFromList(lst: list, item) -> list:

	while item in lst:
		lst.remove(item)
	
	return lst

def main():
	import sys
	import os

	arguments = sys.argv
	if len(arguments) == 1:
		print('error: please provide a commit reason (or command, \'py gitup help\' for help)')
		exit(1)
	elif arguments[1] == 'help':
		print("""
GitUp Help

Normal Usage: py gitup.py "<commit message"
Help Command: py gitup.py help


Flags

-dontpull, -dp	: Will not pull before attempting to commit and push
-status, -s	: Will display status after attempting to push commit

		""")
		exit(0)
	elif len(arguments) > 4:
		print(f'error: expected max 3 argument, {len(arguments) - 1} given')
		exit(1)
	
	dontPull = ('-dontpull' in arguments) or ('-dp' in arguments)
	displayStatus = ('-status' in arguments) or ('-s' in arguments)

	arguments = removeItemFromList(arguments, '-dontpull')
	arguments = removeItemFromList(arguments, '-dp')
	arguments = removeItemFromList(arguments, '-status')
	arguments = removeItemFromList(arguments, '-s')
	
	if len(arguments) < 2:
		print('error: please provide a commit message (or a command, \'py gitup help\' for help)')
		exit(1)
	elif len(arguments) < 2:
		print('error: unexpected argument (\'py gitup help\' for help)')
		exit(1)


	os.system(f'{"" if dontPull else "git pull; "}git add --all; git commit -m "{arguments[1]}"; git push;')

	print()

	if displayStatus:
		os.system("git status")



if __name__ == '__main__':
	main()
