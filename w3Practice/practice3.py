'''
@name fibbonaci 
@desc 
'''
def fibb(n):
    if n <= 1:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)

userValue = int(input("Please input the target: "))
for i in range(userValue):
    print(fibb(i))
