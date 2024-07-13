#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    prod = n
    for i in range(1, n):
        prod *= i
    print(prod)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
