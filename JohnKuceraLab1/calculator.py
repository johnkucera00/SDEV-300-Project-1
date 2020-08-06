"""
__filename__ = "calculator.py"
__coursename__ = "SDEV 300 6380 - Building Secure Web Applications (2198)"
__author__ = "John Kucera"
__copyright__ = "None"
__credits__ = ["John Kucera"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "John Kucera"
__email__ = "johnkucera00@gmail.com"
__status__ = "Test"
"""
import sys

def main():
    """
    Calculator main
    """
    print('****************************************************************\n')
    print('Welcome to the Python Calculator Application!\n')
    print('What calculation do you want to perform?\n')
    print('1) Addition (+)')
    print('2) Subtraction (-)')
    print('3) Division (/)')
    print('4) Multiplication (*)')
    print('5) Modulus (%)')

    operation = int(input('Enter 1, 2, 3, 4 or 5 indicating your selection.\n'))

    # Displaying selected operation
    if operation == 1:
        print('Addition was selected.')

    if operation == 2:
        print('Subtraction was selected.')

    if operation == 3:
        print('Division was selected.')

    if operation == 4:
        print('Multiplication was selected.')

    if operation == 5:
        print('Modulus was selected.')

    if operation > 5 or operation < 1:
        print('Please try again. Your selection here must be 1, 2, 3, 4, or 5.')
        sys.exit()

    number1 = int(input('Enter your first integer:\n'))
    number2 = int(input('Enter your second integer:\n'))

    # Exiting program if 0 is chosen as divisor
    if (operation == 3 or operation == 5) and number2 == 0:
        print('Division by 0 is not allowed. Please try again.')
        sys.exit()

    # Using mathematical operators and displaying result
    if operation == 1:
        sumnum = number1 + number2
        print('The sum of', number1, 'and', number2, 'is', sumnum, '.')

    if operation == 2:
        difference = number1 - number2
        print('The difference of', number1, 'and', number2, 'is', difference, '.')

    if operation == 3:
        quotient = number1 / number2
        print('The quotient of', number1, 'and', number2, 'is', quotient, '.')

    if operation == 4:
        product = number1 * number2
        print('The product of', number1, 'and', number2, 'is', product, '.')

    if operation == 5:
        modulus = number1 % number2
        print('The modulus of', number1, 'and', number2, 'is', modulus, '.')

    print('Thanks for trying the Python Calculator application.')
    print('****************************************************************\n')
    return

if __name__ == "__main__":
    main()
