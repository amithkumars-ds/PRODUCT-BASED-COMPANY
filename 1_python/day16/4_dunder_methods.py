class Counter:
    def __init__(self, start, limit):
        self.current = start
        self.limit = limit
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        raise StopIteration



counter = Counter(5,10)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
