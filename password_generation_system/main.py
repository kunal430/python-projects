#importing required liabraries
import random
import string

#defining a function to generate a password
def password_generator(length):

    #collecting character set 
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    symbol=string.punctuation
    digit=string.digits

    #combining all characters 
    all_chr= uppercase + lowercase + symbol + digit

    #ensuring all character from each set are present to increase the strength of password
    password=[random.choice(uppercase),random.choice(lowercase),random.choice(symbol),random.choice(digit)]

    #decrementing the length because we have 4 characters allready
    length -= 4

    #generating the remaining characters of password
    for _ in range(length):
        password.append(random.choice(all_chr))
    
    #shuffling for a better random pattern
    random.shuffle(password)

    #converting the list into string 
    return "".join(password)

#getting the length of password form user to create a password
try:
    length=int(input("enter password length you want - "))
    if length <= 0:
        print("the length of the password must be grater than zero")
    else:
        password=password_generator(length)
        print("your generated password is - ",password)
except ValueError:
    print("Invalid input. Please enter an integer for the password length.")