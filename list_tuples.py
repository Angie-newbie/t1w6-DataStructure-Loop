# List - Array- ordered collaction of values- mutable
numbers = [13, 2, 23, 53]
print(numbers)
print(numbers[3])

numbers[2] = 17
print(numbers)

# numbers[4] = 80
# print(numbers)

print(numbers[-1])

# numbers[4] = 80
# print(numbers)

numbers.append(42)
print(numbers)

numbers.insert(3, 99)
print(numbers)

pop_value = numbers.pop(0)
print(numbers)
print(pop_value)

numbers.remove(2)
print(numbers)

numbers.append(17)
print(numbers)
numbers.remove(17)
print(numbers)

numbers.append(101)
numbers.sort(reverse=True)
print(numbers)

print(numbers.count(99))

names = ["John", "Jane", "Mike", "Mary"]
print(names)
print(type(names))

print(names[1])
print(names.index('Jane'))

print(len(names))