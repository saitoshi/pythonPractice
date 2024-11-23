# Create a function that determines whether two strings are an anagram 
# @function valid_anagram 
# @desc A function that takes two input and determines if they are an anagram to each other 
# @return true or false 

def valid_anagram(input1, input2): 
    # check if the length of the two strings are the same 
    if (len(input1) != len(input2)): 
        return False
    # otherwise not a valid anagram 
    if (sorted(input1) == sorted(input2)): 
        return True
    # sort input1's string by character 
    else: 
        return False
    # sort input2"s string by character 

    #compare the two inputs 

    # if they are the same then they are valid anagram 

    # othersie not 

userInput1 = input("Input one string: \n")
userInput2 = input("Input another string: \n")

result = valid_anagram(userInput1, userInput2)

if (result == True):
    print(userInput1 + " and " + userInput2 + " are valid anagrams")
else: 
    print("The two strings you have inputted are not valid anagrams")
