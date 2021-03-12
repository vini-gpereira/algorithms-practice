#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    subLen = len(s)
    l = min(subLen, n)
    occur = 0

    for j in range(l):
        if s[j] == 'a':
            occur += 1

    if n > subLen:
        occur *= (n // subLen)

        for i in range(n % subLen):
            if s[i] == 'a':
                occur += 1

    return occur


if __name__ == '__main__':
    s = 'abcab'
    n = 10
    occurences = repeatedString(s, n)
    print(occurences)
