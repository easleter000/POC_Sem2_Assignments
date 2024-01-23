try:
    value = int(input('Enter an integer: '))
    value_1 = int(input('Enter an 2nd integer: '))
    print('The quotient of', value ,"and", value_1, 'is', value/value_1)
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')
except:
    print("Something strange happened")
    
