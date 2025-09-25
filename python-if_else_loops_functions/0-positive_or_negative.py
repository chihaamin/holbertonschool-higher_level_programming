#!/usr/bin/python3
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
def positive_or_negative(i):
    """Prints whether a number is positive or negative.
    Args:
        i (int): The number to evaluate.
    """
    if i < 0:
        print(f"{i} is negative")
    else:
        print(f"{i} is positive")
    return
positive_or_negative(number)
