#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    pairs = 0
    socks = {}
    for sock in ar:
        if sock in socks:
            socks[sock] += 1
            if socks[sock] % 2 == 0:
                pairs += 1
        else:
            socks[sock] = 1
    return pairs


if __name__ == '__main__':
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    pairs = sockMerchant(n, ar)
    print(pairs)
    n = 7
    ar = [1, 2, 1, 2, 1, 3, 2]
    pairs = sockMerchant(n, ar)
    print(pairs)
