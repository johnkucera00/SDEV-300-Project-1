"""
__filename__ = "min_max.py"
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

def main():
    """
    MinMax main
    """
    print('****************************************************************\n')
    print('Welcome to the Python MinMax Application!\n')
    print('This application calculates the minimum and maximum of 5 integer '
          'values entered by a user.\n')

    integer1 = int(input('Enter your first integer: \n'))
    integer2 = int(input('Enter your second integer: \n'))
    integer3 = int(input('Enter your third integer: \n'))
    integer4 = int(input('Enter your fourth integer: \n'))
    integer5 = int(input('Enter your fifth integer: \n'))

    #Using min() and max() functions to determine minimum and maximum
    minimum = min(integer1, integer2, integer3, integer4, integer5)
    maximum = max(integer1, integer2, integer3, integer4, integer5)

    print('The minimum integer you entered was', minimum, '.')
    print('The maximum integer you entered was', maximum, '.')
    print('Thanks for trying the Python MinMax application.')
    print('****************************************************************\n')
    return

if __name__ == "__main__":
    main()
