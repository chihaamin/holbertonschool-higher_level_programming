#!/usr/bin/python3


def print_hexa():
    for number in range(0, 99):
        print("{} = {}".format(number, hex(number)))


if __name__ == "__main__":
    print_hexa()
