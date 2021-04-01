#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

COUNT = "count"
INDEXES = "indexes"

# Complete the countTriplets function below.
def countTriplets(arr, ratio):
    tripletCounter, alreadyIteratedCounters, notIteratedCounters = initializeCounters(arr)
    return calculateTripletsCounting(arr, ratio, notIteratedCounters, alreadyIteratedCounters)

def initializeCounters(arr):
    tripletCounter = 0
    notIteratedCounters = Counter(arr)
    alreadyIteratedCounters = Counter()
    return tripletCounter, alreadyIteratedCounters, notIteratedCounters

def calculateTripletsCounting(arr, ratio, notIteratedCounters, alreadyIteratedCounters):
    tripletCounter = 0

    for number in arr:
        tripletCounter += calculateTripletsCountingFromNumber(number, ratio, notIteratedCounters, alreadyIteratedCounters)

    return tripletCounter

def calculateTripletsCountingFromNumber(number, ratio, notIteratedCounters, alreadyIteratedCounters):
    tripletCounter = 0
    previousNumber, nextNumber = calculatePreviousAndNextNumbers(number, ratio)

    reduceNumberNotIteratedCounting(number, notIteratedCounters)

    if alreadyIteratedCounters[previousNumber] and notIteratedCounters[nextNumber] and not number % ratio:
        tripletCounter = alreadyIteratedCounters[previousNumber] * notIteratedCounters[nextNumber]

    incrementNumberAlreadyIteratedCounting(number, alreadyIteratedCounters)

    return tripletCounter

def calculatePreviousAndNextNumbers(number, ratio):
    previousNumber = number // ratio
    nextNumber = number * ratio
    return previousNumber, nextNumber

def reduceNumberNotIteratedCounting(number, notIteratedCounters):
    notIteratedCounters[number] -= 1

def incrementNumberAlreadyIteratedCounting(number, alreadyIteratedCounters):
    alreadyIteratedCounters[number] += 1


if __name__ == '__main__':
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)
