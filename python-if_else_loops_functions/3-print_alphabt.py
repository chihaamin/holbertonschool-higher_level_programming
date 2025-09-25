#!/usr/bin/python3


def print_alphabt():
    for letter in range(97, 123):
        if chr(letter) != 'q' and chr(letter) != 'e':
            print("{}".format(chr(letter)), end="")


if __name__ == "__main__":
    print_alphabt()
