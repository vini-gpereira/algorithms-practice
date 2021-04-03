#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    toyPriceSum = 0
    numToys = 0

    for price in prices:

        if price + toyPriceSum > k:
            break

        toyPriceSum += price
        numToys += 1
    
    return numToys

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)
