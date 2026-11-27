def numbers():
    for i in range(5):
        yield i

gen = numbers()

for n in gen:
    print(n)  # 0, 1, 2, 3, 4

for n in gen:
    print(n)  # Nothing!

# Once a generator reaches StopIteration, it stays exhausted.
