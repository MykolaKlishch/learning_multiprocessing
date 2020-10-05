import concurrent.futures
import time


def do_something(seconds=1):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping {seconds} second(s)...'


if __name__ == "__main__":

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
