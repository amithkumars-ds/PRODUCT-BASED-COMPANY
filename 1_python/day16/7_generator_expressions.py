# list comprehension
list_squares = [x*x for x in range(5)] # creates entire list immediately

# generator expression
generator_squares = (x*x for x in range(5))

# Create a generator expression that produces squares of numbers from 1 to 10.
squares = (x**2 for x in range(1,11))
print("Type of generator expression: {0}".format(type(squares)))
print(next(squares))
print(next(squares))

for num in squares:
    print(num)
