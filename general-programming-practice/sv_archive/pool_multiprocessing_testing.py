
import concurrent.futures
import time

def do_something(seconds):
	print(f'Sleeping for {seconds} seconds...')
	time.sleep(seconds)

	return f'Done sleeping for {seconds} second{"" if seconds == 1 else "s"}.'

if __name__ == '__main__':
	with concurrent.futures.ProcessPoolExecutor() as executor:
		for result in executor.map(do_something, range(4)):
			print(result)

if __name__ == '__main__':
	with concurrent.futures.ProcessPoolExecutor() as executor:
		results = executor.map(do_something, range(4))

		for result in concurrent.futures.as_completed(results):
			print(result)