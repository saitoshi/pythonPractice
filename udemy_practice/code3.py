#@name FizzBuzz 
#@desc The program should print each number from 1 to 100 in turn and include number 100

def FizzBuzz():
    for i in range (1,101):
        if (i % 3 == 0) and (i % 5 != 0):
            print("Fizz\n")
        elif (i % 5 == 0) and (i % 3 != 0):
            print("Buzz\n")
        elif (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz\n")
        else:
            print("" + str(i) + "\n")
FizzBuzz()
        