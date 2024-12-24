'''
@name is_prime 
@desc Determines whether the input is a prime number or not 
@input num - The number to be determined whether it is prime or not
@return TRUE or FALSE 
'''
def is_prime(num):
    print(num)
    isPrime = True 
    if (num == 0 or num == 1):
        isPrime = False
    elif num > 1:
        for i in range (2, num):
            print(i)
            if (num % i == 0):
                isPrime = False
                break
    return isPrime
print(is_prime(5))

