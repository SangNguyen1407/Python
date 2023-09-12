"""
Topic: 
Desc :
"""

def format_number():
    x = 1234.56789

    # two decimal places of accuracy
    print(format(x, '0.2f'))

    # right justified
    print(format(x, '>10.1f'))

    # left justified
    print(format(x, '<10.1f'))

    # Centered
    print(format(x, '^10.1f'))

    print(format(x, 'e'))
    print(format(x, '0.2E'))
    
    # string
    print('The value is {:0,.2f}'.format(x))

    print(format(x, '0.1f'))
    print(format(-x, '0.1f'))

if __name__ == '__main__':
    format_number()