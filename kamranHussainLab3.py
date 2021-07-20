#############################################################
# Name: Kamran Hussain
# Date: 7/20/2021
# Course: CS 3A Object-Oriented Programming Methodologies in Python
# Lab 3: Programming with Functions, Using Loops, File I/O, Exceptions
# Validating User Input, Automating Your Test Suite
# Description: A console based program that calculates the value of a coupon
# based on the amount of a grocery bill. Iterating off of lab 2,
# the program contains a tester for the main method and writes inputs to a file
# ###########################################################

# Source code:
def tester():
    main('apple')
    main('-1')
    main('0')
    main('10')
    main('70')
    main('160')
    main('222')


def main(b=None):  # alternative function name is groceryCouponCalculator
    MIN_VALUE = 0
    if b is not None:
        n = b
    else:
        n = input("Please enter the cost of your groceries: $")
    while True:
        try:
            n = float(n)
        except ValueError:
            n = input('The value you entered is a character, please enter a ' +
                      'numeric value: $')
        else:
            if n < MIN_VALUE:
                n = input(
                    'The value you entered is negative, please enter a ' +
                    'positive value: $')
            else:
                break

    if n < 10.0:
        calculated_amount = 'You won a discount coupon of $0.00 (0% of your ' \
                            'purchase) '
        writeToFile(calculated_amount)
        # print(calculated_amount)
    elif 10 <= n < 60:
        percentage = 0.08
        discount = n * percentage
        formatted_value = "{:.2f}".format(discount)
        calculated_amount = 'You won a discount coupon of $' + str(
            formatted_value) + ' (8% of your purchase)'
        writeToFile(calculated_amount)
        # print(calculated_amount)
    elif 60 <= n < 150:
        percentage = 0.10
        discount = n * percentage
        formatted_value = "{:.2f}".format(discount)
        calculated_amount = 'You won a discount coupon of $' + str(
            formatted_value) + ' (8% of your purchase)'
        writeToFile(calculated_amount)
        # print(calculated_amount)
    elif 150 <= n < 210:
        percentage = 0.12
        discount = n * percentage
        formatted_value = "{:.2f}".format(discount)
        calculated_amount = 'You won a discount coupon of $' + str(
            formatted_value) + ' (8% of your purchase)'
        writeToFile(calculated_amount)
        # print(calculated_amount)
    elif n >= 210:
        percentage = 0.14
        discount = n * percentage
        formatted_value = "{:.2f}".format(discount)
        calculated_amount = 'You won a discount coupon of $' + str(
            formatted_value) + ' (8% of your purchase)'
        writeToFile(calculated_amount)
        # print(calculated_amount)


# File writing function
def writeToFile(str):
    outfile = open('kha3out.txt', 'r+')
    outfile.readlines()
    outfile.write(str + '\n')
    outfile.close()


# program entry point
if __name__ == '__main__':
    tester()

# Sample Run
