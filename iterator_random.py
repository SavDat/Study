from random import random

class RandomIterator():    
    def __init__(self, k):
        self.k = k
        self.i = 0
    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration
    def __iter__(self):
        return self
for x in RandomIterator(10):
    print(x)