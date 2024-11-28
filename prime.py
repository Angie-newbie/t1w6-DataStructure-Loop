# output if a number is prime

def primecheck(num):
    for i in range (2, num-1):
        if num % i == 0:
            print("it is not a prime")
            break
        else:
            print("it is a prime")
            break

primecheck(17)