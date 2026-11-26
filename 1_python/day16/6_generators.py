def counter(start,limit):
    current = start
    while current < limit:
        yield current
        current += 1


numbers = counter(5,10)
for number in numbers:
    print(number)
