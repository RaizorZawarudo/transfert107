#!/usr/bin/python3

import math
import sys



def print_usage():
    print("USAGE\n\t./107transfer [num den]*\n")
    print("DESCRIPTION")
    print("\tnum\t\tpolynomial numerator defined by its coefficients")
    print("\tden\t\tpolynomial denominator defined by its coefficients")

def check_input():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print_usage()
        sys.exit(0)

    if len(sys.argv) == 1:
        print("Wrong number of arguments")
        sys.exit(84)

    if len(sys.argv) % 2 == 0:
        print("Wrong number of arguments")
        sys.exit(84)

def main():
    check_input()

    result = 1.0
    x = 0.000
    i = 1

    while x <= 1.001:
        while i  < (len(sys.argv) - 1):
            try:
                numerator_array = [int(a) for a in sys.argv[i].split('*')]
                denumerator_array = [int(a) for a in sys.argv[i + 1].split('*')]
            except ValueError:
                print("Invalid value in numerator or denumerator\n")
                sys.exit(84)
            numerator_value = sum(numerator_array[n] * x ** n for n in range(len(numerator_array)))
            denumerator_value  = sum(denumerator_array[n] * x ** n for n in range(len(denumerator_array)))
            if (numerator_value == denumerator_value):
                result = result * 1
            else:
                if (denumerator_value == 0):
                    sys.exit(84)
                result = result * (float(numerator_value) / float(denumerator_value))
                i = i + 2
        print("%.3f" " -> " "%.5f" %(x, result))
        x += 0.001
        i =1
        result = 1.0
    sys.exit(0)

if __name__ == '__main__':
    main()