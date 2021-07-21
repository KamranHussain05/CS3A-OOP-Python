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
    MIN_VALUE=0
    MAX_VALUE=9

    spelled_numbers = {0:'zero',
                       1:'one',
                       2:'two',
                       3:'three',
                       4:'four',
                       5:'five',
                       6:'six',
                       7:'seven',
                       8:'eight',
                       9: 'nine'}

    print('***Spelling Digits***')
    for i in range (10):
        print(i.__str__() + ' ' + spelled_numbers[i])

    for i in range(3):
        n = (input('Enter a digit from 0 to 9: '))

        while True:
            try:
                n = int(n)
            except ValueError:
                n = input(
                    'The value you entered is a character, please enter an ' +
                    'integer: ')
            else:
                if n < MIN_VALUE or n > MAX_VALUE:
                    n = int(input(
                        'You entered a digit out of the range, try again: '))
                else:
                    break

        print(n.__str__()+ ' spelled out is: '+spelled_numbers[n])


if __name__ == '__main__':
    main()

# Sample Run:
'''
***Spelling Digits***
0 zero
1 one
2 two
3 three
4 four
5 five
6 six
7 seven
8 eight
9 nine
Enter a digit from 0 to 9:  
The value you entered is a character, please enter an integer: -1
You entered a digit out of the range, try again: 10
You entered a digit out of the range, try again: 2
2 spelled out is: two
Enter a digit from 0 to 9: 4
4 spelled out is: four
Enter a digit from 0 to 9: 8
8 spelled out is: eight
'''