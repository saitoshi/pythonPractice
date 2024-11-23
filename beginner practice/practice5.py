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

            