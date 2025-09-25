#!/usr/bin/python3
import random
number = random.randint(-10, 10)


def positive_or_negative(i):
    if i < 0:
        print(f"{i} is negative")
    elif i == 0:
        print(f"{i} is zero")
    else:
        print(f"{i} is positive")
    return


positive_or_negative(number)
