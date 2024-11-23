# Beginner Practice Problems

<ol>
<li>Write a program that takes in a user input and determines whether it is even or not?</li>

```
# Practice 1 - Create a program that determines whetehr user input is even or not
userInput = input("Enter A Value and Will determine if it is even or not \n")
print("You have inputted: " + userInput)
digitEvaluation = ""
if (int(userInput) % 2 == 0):
    digitEvaluation = "even"
else:
    digitEvaluation = "odd"

print(userInput + " is a " + digitEvaluation + " number.")

```

<li>Write a program that determines whether the user inputs are an angaram of each other or not?

```
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
```

</li>

<li>Create a Fibonnaci Sequence function</li>

```
"""
@name fibList
@desc A function that returns the list of fibbonacci numbers based on the input n
@input n
@return list of the fibbonacci numbers
"""
def fibList(input):
    n = int(input)
    fib = []
    i = 1
    if n < 0:
        return "Error: input must be greater than 0"
    elif n == 0:
        fib = []
    elif n == 1:
        fib = [1]
    elif n == 2:
        fib = [1,1]
    else:
        fib = [1,1]
        while i < (n -1):
            fib.append(fib[i] + fib[i-1])
            i = i + 1
    return fib

userInput = input("Please input the n-th order of fibbonacci sequence you are interested in seeing\n ")
print(fibList(userInput))
```

<li>
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

```
def removeDuplicate(inputList):
    returnList = []
    if not isinstance(inputList, list):
        return "The object is not a list"
    duplicateRemoval = list(set(inputList))
    for i in duplicateRemoval:
        if i == " ":
            duplicateRemoval.remove(" ")
        elif i == ",":
            duplicateRemoval.remove(",")
    return duplicateRemoval

userInput = input("Enter a list and we will remove any duplicates from it: ")
userList = list(userInput)
print(removeDuplicate(userList))

```

</li>
<li>
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

```
# @Problem - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# @name twoSum
# @input listInt - a list of input that user has input
# @input target - the target of the two summary
# @return the position
def formatConvert(userInput):
    listInput = list(userInput)
    for i in listInput:
        if i == " ":
            listInput.remove(" ")
        elif i == ",":
            listInput.remove(",")
    return listInput

def twoSum(inputList, target):
    result = []
    target = int(target)
    # convert the input into a set of integet
    for i in range(len(inputList)):
        inputList[i] = int(inputList[i])

    for x in range(len(inputList)):
        for y in range(len(inputList)):
            if (inputList[x] + inputList[y] == target) & (x != y):
                result.append(x)
                result.append(y)
                return result

listInput = input("Place the input list: ")
listInput = formatConvert(listInput)
userTarget = input("Place your target: ")

print(twoSum(listInput, userTarget))

```

</li>
<li>
Given an integer x, return true if x is a palindrome, and false otherwise.
</li>
</ol>
