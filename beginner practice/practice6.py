# Problem - Given an integer x, return true if x is a palindrome, and false otherwise.

"""
@function isPalindrome 
@desc Determine whether the input is a Palindrome or not 
@input input 
@return true if it is a palindrome or not
"""
def isPalindrome(userInput):
    #declare a flag 
    inputList = [char for char in userInput]
    reverseList = inputList.reverse()

    for x in range(len(inputList)):
        if inputList[x] != reverseList[x]:
            return False 