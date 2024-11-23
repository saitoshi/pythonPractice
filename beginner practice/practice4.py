"""
@Problem Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
"""

"""
@name removeDuplicate 
@desc Removes the duplicate of a given list 
@return the cleaned up version 
@error if the input is not a list 
"""
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