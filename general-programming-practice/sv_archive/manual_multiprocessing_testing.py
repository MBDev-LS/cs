
import multiprocessing
import time

def do_something():
    print('Sleeping for 4 seconds...')
    time.sleep(4)
    print('Done sleeping.')

if __name__ == '__main__':

    startTime = time.perf_counter()

    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join()


    endTime = time.perf_counter()

    print(f'Finished in {round(endTime - startTime, 2)} seconds')
