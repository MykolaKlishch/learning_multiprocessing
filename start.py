import multiprocessing
import time


def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


if __name__ == "__main__":

    start = time.perf_counter()

    p1 = multiprocessing.Process(target=do_something, args=(), kwargs={})
    p2 = multiprocessing.Process(target=do_something, args=(), kwargs={})

    p1.start()
    p2.start()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
