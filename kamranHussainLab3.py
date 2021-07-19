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
def main():  # alternative function name is groceryCouponCalculator
    try:
        n = float(input('Please enter the cost of your groceries: $'))
    except ValueError:
        n = float(input('You entered a letter instead of a number, ' +
                        'try again: $'))

    while n<0:
        n = float(input('The value you entered is negative, please enter a ' +
                        'positive value: '))

    if n < 10.0:
        print('You won a discount coupon of $0.00 (0% of your purchase)')
    elif 10 <= n < 60:
        percentage = 0.08
        discount = n*percentage
        formatted_value = "{:.2f}".format(discount)
        calculated_amount = print('You won a discount coupon of $' +
                            str(formatted_value) +' (8% of your purchase)')
        writeToFile(calculated_amount)
    elif 60 <= n < 150:
        percentage = 0.10
        discount = n*percentage
        formatted_value = "{:.2f}".format(discount)
        calculated_amount = print('You won a discount coupon of $' +
                            str(formatted_value) + ' (8% of your purchase)')
        writeToFile(calculated_amount)
    elif 150 <= n < 210:
        percentage = 0.12
        discount = n*percentage
        formatted_value = "{:.2f}".format(discount)
        calculated_amount = print('You won a discount coupon of $' +
                            str(formatted_value) + ' (8% of your purchase)')
        writeToFile(calculated_amount)
    elif n >= 210:
        percentage = 0.14
        discount = n*percentage
        formatted_value = "{:.2f}".format(discount)
        calculated_amount = print('You won a discount coupon of $' +
                            str(formatted_value) + ' (8% of your purchase)')
        writeToFile(calculated_amount)

def writeToFile(str):
    outfile = open('kha3out.txt', 'w')
    outfile.write(str)
    outfile.close()
    print('wrote to file')

# program entry point
if __name__=='__main__':
    main()