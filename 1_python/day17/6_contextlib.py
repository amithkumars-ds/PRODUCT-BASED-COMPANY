# context manager + decorators

# class FileManager:
#     def __enter__(self):
#         self.file = open(self.filename, "r")
#         return self.file
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.file.close()

# above implementation can be achieved with contextlib library as well
import csv
from contextlib import contextmanager

@contextmanager
def file_manager(filename):
    file = open(filename, "r")
    try:
        yield file
    finally:
        file.close()


if __name__ == "__main__":
    with file_manager("../../docs/employees.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

        raise ValueError
