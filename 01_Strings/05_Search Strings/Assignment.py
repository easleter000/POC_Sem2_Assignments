user_text = input("Enter some text:")

result = user_text.find('the')

if result == -1:
    print("The word 'the' is not in the string")
else:
    print("The word 'the' is in the string") 
    print(user_text.find('the'))








