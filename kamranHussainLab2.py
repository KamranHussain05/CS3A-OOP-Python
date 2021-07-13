###########################################################
# Name: Kamran Hussain
# Date: 7/13/2021
# Course: CS 3A Object-Oriented Programming Methodologies in Python
# Lab 2: Programming with Numbers and Strings; Controlling Selection
# Description: A console based program that calculates the value of a coupon
# based on the amount of a grocery bill.
# ###########################################################

# Source code:

n = float(input('Please enter the cost of your groceries: $'))

while n<0:
    n = float(input('The value you entered is negative, please enter a '
                    'positive value: '))

if n < 10.0:
    print('You win a discount coupon of $0.00 (0% of your purchase)')
elif 10 <= n < 60:
    percentage = 0.08
    discount = n*percentage
    formatted_value = "{:.2f}".format(discount)
    print('You win a discount coupon of $' + str(formatted_value) +
          ' (8% of your purchase)')
elif 60 <= n < 150:
    percentage = 0.10
    discount = n*percentage
    formatted_value = "{:.2f}".format(discount)
    print('You win a discount coupon of $' + str(formatted_value) +
          ' (10% of your purchase)')
elif 150 <= n < 210:
    percentage = 0.12
    discount = n*percentage
    formatted_value = "{:.2f}".format(discount)
    print('You win a discount coupon of $' + str(formatted_value) +
          ' (12% of your purchase)')
elif n >= 210:
    percentage = 0.14
    discount = n*percentage
    formatted_value = "{:.2f}".format(discount)
    print('You win a discount coupon of $' + str(formatted_value) +
          ' (14% of your purchase)')

# Sample Run:
'''
Please enter the cost of your groceries: $-160
The value you entered is negative, please enter a positive value: 160
You win a discount coupon of $19.20 (12% of your purchase)
'''

