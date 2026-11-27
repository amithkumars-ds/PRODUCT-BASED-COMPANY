import csv

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Entering execution!")
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting execution!")
        self.file.close()



if __name__ == "__main__":
    with FileManager("../../docs/employees.csv") as file:
        reader = csv.DictReader(file)

        raise ValueError("Simulated failure")

        for row in reader:
            print(row)
