# Iterable: is any python object that you can loop over
# Iterator: is an object that produces values one at a time

numbers = [10,20,30]
print(type(numbers))

iterator = iter(numbers)
print(type(iterator))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

