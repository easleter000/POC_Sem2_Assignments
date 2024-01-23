try:
    value = int(input('Enter an integer: '))
    value_1 = int(input('Enter an 2nd integer: '))
    print('The quotient of', value ,"and", value_1, 'is', value/value_1)
except ValueError:
    print('You did not provide a number, so I will not calculate the quotient')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')

    
