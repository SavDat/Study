#--------------------iterator_primes------------------------

import itertools
def primes():
    start = 2
    while True:
        count = 0
        for i in range(2, start+1):
            if start % i == 0:
                count += 1
        if count == 1: 
            yield start
        start += 1

#------------------- Block Input ------------------------->>>

print(list(itertools.takewhile(lambda x: x<=31, primes())))

