"""
@name removeEveryThird
@desc Removes every third item within the list 
@return A new list from the original list 
"""
def removeEveryThird(listInput):
    cleanList = []
    n = len(listInput)
    for i in range(len(listInput)):

        x = i + 1
        if (x % 3 != 0):
            cleanList.append(listInput[i])
    return cleanList
sampleList = [1,4,3, 5, 6, 10, 100, 200]
newlist = removeEveryThird(sampleList)
print(newlist)