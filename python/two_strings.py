#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.


def twoStrings(s1, s2):
    if set(s1) & set(s2):
        return "YES"

    return "NO"


if __name__ == '__main__':
    s1 = "hello"
    s2 = "world"
    print(twoStrings(s1, s2))
    s1 = "hi"
    s2 = "world"
    print(twoStrings(s1, s2))
