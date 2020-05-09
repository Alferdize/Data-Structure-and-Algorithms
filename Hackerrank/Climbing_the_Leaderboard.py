#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import *


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))
    scores = list(set(scores))
    l = len(scores)
    scores.sort()
    result = []
    for i in alice:
        result.append(l - bisect_right(scores, i) + 1)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
