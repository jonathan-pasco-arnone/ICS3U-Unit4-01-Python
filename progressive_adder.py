#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program adds a number progressively


def main():
    # This function adds an inputted number progressively

    answer = 0
    print("")
    print("Please enter a number to be added like the example below.")
    print("")
    print("Ex: user enters 5: 1+2+3+4+5=15, so 15 is outputted")
    print("")
    number_str = input("Number: ")
    print("")

    try:
        number = int(number_str)
    except Exception:
        print("Invalid Input")
    else:
        while(number > 0):
            answer = answer + number
            number = number - 1
        answer_str = str(answer)
        print("The answer is " + answer_str)


if __name__ == "__main__":
    main()
