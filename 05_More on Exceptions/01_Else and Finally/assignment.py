#Continue with code from 3.3

number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number:"))
    number2 = int(input("Enter another number:"))
except ValueError:
    print("A number was not given somewhere")
    
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    answer = number1/number2
    print("The quotient of",number1 ,"divided by", number2, "equals", answer)

except ZeroDivisionError:
    print("You cannot divide by 0")
else:
    print("Nice number buddy!")
finally:
    print("Enter a cooler number, if you tried to enter a letter just stop")

