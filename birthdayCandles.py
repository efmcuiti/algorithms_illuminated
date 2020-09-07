#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    blowable, taller = 1, ar[0]
    
    for candle in ar[1:]:
        if candle > taller:
            blowable, taller = 1, candle
        elif candle == taller:
            blowable += 1
    return blowable
