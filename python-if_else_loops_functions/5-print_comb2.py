#!/usr/bin/python3


def print_comb2():
    for number in range(0, 100):
        if number == 99:
            print("{:02}".format(number))
        else:
            print("{:02}".format(number), end=", ")
                

if __name__ == "__main__":
    print_comb2()
