#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program counts


def main(): 
    loop_counter = 0
    answer = 1

    # input
    print("This program calculates exponents.")
    str_integer = input("Enter a positive integer: ")
    str_exponent = input("Enter the exponent: ")

    # process
    try:
        int_integer = int(str_integer)
        int_exponents = int(str_exponent)
        if int_integer < 0:
            print("This is not a positive number.")
        for loop_counter in range(int_exponents):
            answer = answer * int_integer
            loop_counter = loop_counter + 1
        print("{0}^{1} = {2}".format(int_integer, int_exponents, answer))
    except ValueError:
        print("Invalid integer")
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
