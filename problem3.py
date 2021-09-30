'''
    Author: Janahan Dhushenthen (56777220)
    Date: 2021-09-29
    Description: CPEN 442 Assignment 2 - Problem 3
                 find_collision(): finds two strings that result in a CRC32 collision 
                                   (demonstrating no strong collision resistance property)
'''

import zlib
import string
from itertools import permutations
import time

class Problem3:
    def __init__(self):
        self.perms = [''.join(p) for p in permutations(string.digits)]

    def find_collision(self):
        start_time = time.time()
        strings = {}

        for perm in self.perms:
            crc = hex(zlib.crc32(perm.encode()))
            if crc not in strings:
                strings[crc] = perm
            else:
                print(perm, strings[crc])
                print("Time Elapsed: %s seconds" % (time.time() - start_time))
                break

if __name__ == "__main__":
    P3 = Problem3()
    P3.find_collision()

