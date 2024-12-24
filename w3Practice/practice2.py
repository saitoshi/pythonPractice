'''
@name ReverseFullName 
@desc The function should reverse the users full name 
@return reversed full name 
'''
def reverseFullName():
    separator = ''
    firstName = input("Please type in your first name: ")
    lastName = input("\nPlease type in your last name: ")
    firstNameList =list(firstName)
    firstNameList.reverse()
    print(firstNameList)
    reversedFirstName = separator.join(firstNameList)
    print(reversedFirstName)
reverseFullName()