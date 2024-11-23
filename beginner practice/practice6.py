# Problem - Given an integer x, return true if x is a palindrome, and false otherwise.

"""
@function isPalindrome 
@desc Determine whether the input is a Palindrome or not 
@input input 
@return true if it is a palindrome or not
"""
def isPalindrome(userInput):
    reverseInput = ''.join(reversed(userInput))

    if (userInput == reverseInput):
        return True 
    return False 

userInput = input("Place a string you would like to check if it is a palindrome: ")
print(isPalindrome(userInput))