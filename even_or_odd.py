def even_or_odd(num):
    if num % 2 == 0:
        return"even"
    else:
        return"odd"

print(even_or_odd(3))
result = even_or_odd(55)
print(f"55 is {result}")