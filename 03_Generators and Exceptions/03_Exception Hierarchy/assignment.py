number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number:"))
    number2 = int(input("Enter another number:"))
except ValueError:
    print("A number was not given somewhere")
    


try:
    answer = number1/number2
    print("The quotient of",number1 ,"divided by", number2, "equals", answer)
   

except ZeroDivisionError:
    print("You can't divide by 0")  

    
