#############################################################
# Name: Kamran Hussain
# Date: 7/27/2021
# Course: CS 3A Object-Oriented Programming Methodologies in Python
# Lab 4: Application, Spelling Digits
# Description: A console based program that searches through a dictionary to
# return the spelled out version of numbers 0-9
# ###########################################################


# Source code:
def main():
    print('***Spelling Digits!***')

    for i in range(3):
        n = int(input('Enter a digit from 0 to 9: '))

        if n < 0 or n > 9:
            n = int(input('You entered a digit out of the range, try again: '))


if __name__ == '__main__':
    main()

# Sample Run:
'''

'''