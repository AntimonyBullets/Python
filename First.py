name = input('What is your name? ')
if len(name)<3:
    print("The name must have at least 3 characters")
elif len(name)>50:
    print("The name can only have a maximum of 50 characters")
else:
    print("The name looks good!")
