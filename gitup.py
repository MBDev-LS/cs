


def main():
	import sys
	import os

	arguments = sys.argv
	print(arguments)
	if len(arguments) == 1:
		print('error: please provide a commit reason')
		exit()
	if len(arguments) > 2:
		print(f'error: expected 1 argument, {len(arguments)} given')
		exit()

	os.system(f'git pull; git add --all; git commit -m "{arguments[1]}"; git push')


if __name__ == '__main__':
	main()