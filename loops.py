# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# while loop
number = 1
while number <= 5:
    print(number)
    number += 1

# for loop
names = ["Jone", "Jane", "Mike", "Mary"]

for i, j in enumerate(names):
    print(f"{i +1}, {j}")

# list all numbers between 10 and 100 and state whether they are odd number
# for num in range(10,101):
#     print(f"{num} is {"odd" if num % 2 else "even"}")
#     # if num % 2 == 0:
#     #     print(f"{num} is a even num")
#     # else: 
#     #     print(f"{num} is a odd num")

# for else
for i in range (10):
    print(i)
    if i == 6:
        break
else:
    print("loop finished")

# Output if a number is prime
# Numver is prime iff it is divisible by 1 and itseld only

number = 17

for i in range (2,number):
    if number % i == 0:
        print("not a prime")
        break
    else:
        print("it's prime")
        break