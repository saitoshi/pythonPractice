# @name passwordGenerator 
# @desc A function that generates a random password that is longer than 8 characters 
# @input none 
# @return the password 

# import the necessary random modules 
import random 

def passwordGenerator():
    lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperCase = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    specialCharacter = ['!', '#','&','(',')', '%','?']
    password_list = []
    passwordLength = int(random.randrange(8, 30))
    randCharLength = int(random.randrange(3,5))
    randCapLength = int(random.randrange(1,3))
    letterLength = passwordLength - randCapLength - randCharLength
  
    # iterate through the length 
    for i in range (randCharLength): 
        password_list.append(random.choice(specialCharacter))
    for j in range (letterLength):
        password_list.append(random.choice(lowerCase))
    for k in range(randCapLength):
        password_list.append(random.choice(upperCase))
    
    random.shuffle(password_list)

    password = ""

    for char in password_list:
        password += char
    print(password)

        

passwordGenerator()