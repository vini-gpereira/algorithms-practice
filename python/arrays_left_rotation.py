#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.


def rotLeft(a, d):
    n = len(a)
    rot = [0 for _ in range(n)]

    for i in range(n):
        rot[(i - d) % n] = a[i]

    return rot


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    d = 4
    res = rotLeft(a, d)
    print(res)
