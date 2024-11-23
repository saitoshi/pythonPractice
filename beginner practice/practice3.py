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
    
