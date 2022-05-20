


def main():
	import sys

	arguments = sys.argv
	if len(arguments) == 0:
		print('error: please provide a commit reason')
	if len(arguments) > 1:
		print(f'error: expected 1 argument, {len(arguments)} given')


if __name__ == '__main__':
	main()