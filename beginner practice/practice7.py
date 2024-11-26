'''
@Problem - Convert Roman Numeral Into Digit 
@Input - A string of Roman Nuberal 
@Output - The converted digit 

'''

def RomanToNumeral(inputString):
    print(inputString)
    symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    value =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    num = 0
    #variable for the increment 
    i = 0
    while inputString != '':
        while inputString.startswith(symbol[i]):
            num += value[i]
            inputString = inputString[len(symbol[i])]
        i = i + 1
    return num

listInput = input("Type a sample of Roman Numeral: ")
print(RomanToNumeral(listInput))

    

