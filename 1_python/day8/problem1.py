class Book:
    def __init__(self,
                 title:str,
                 author:str,
                 price:int):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        return f"Book: {self.title}, Price: {self.price}, Author: {self.author}"



if __name__ == "__main__":
    book1 = Book("Toby", "Charles", 40)
    book2 = Book("Hamlet", "Shakespear", 100)

    print(book1.display_info())
    print(book2.display_info())

