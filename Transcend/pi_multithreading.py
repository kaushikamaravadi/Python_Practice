import multiprocessing
import random
import math
import time
start = time.time()


def montey_carlo(n, circle=0):

    for count in range(n):
        d = math.hypot(random.random(), random.random())
        if d < 1:
            circle += 1
        count += 1
    print(4.0 * circle / count)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=montey_carlo(100000000))
    p2 = multiprocessing.Process(target=montey_carlo(100000000))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

stop = time.time()
print(start - stop)
