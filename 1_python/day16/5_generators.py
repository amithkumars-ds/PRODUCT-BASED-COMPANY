def counter(limit):
    current = 0

    while current < limit:
        yield current
        current += 1

numbers = counter(5)

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
    
