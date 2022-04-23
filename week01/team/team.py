"""
Course: CSE 251
Lesson Week: 01 - Team Acvitiy
File: team.py
Author: Brother Comeau

Purpose: Find prime numbers

Instructions:

- Don't include any other Python packages or modules
- Review team acvitiy details in I-Learn

"""

from datetime import datetime, timedelta
import threading


# Include cse 251 common Python files
from cse251 import *

# Constants
NUM_OF_THREADS = 10

# Global variable for counting the number of primes found
prime_count = 0
numbers_processed = 0


def is_prime(n: int) -> bool:
    global numbers_processed
    numbers_processed += 1

    """Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def t_func(start, end, index):
    global prime_count

    for i in range(start + index, start + range_count, NUM_OF_THREADS):
        if is_prime(i):
            prime_count += 1
    #         print(i, end=", ", flush=True)
    # print(flush=True)


if __name__ == "__main__":
    log = Log(show_terminal=True)
    log.start_timer()

    start = 10000000000
    range_count = 100000

    threads = []

    for i in range(NUM_OF_THREADS):
        t = threading.Thread(target=t_func, args=(start, range_count, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Should find 4306 primes
    log.write(f"Numbers processed = {numbers_processed}")
    log.write(f"Primes found      = {prime_count}")
    log.stop_timer("Total time")
