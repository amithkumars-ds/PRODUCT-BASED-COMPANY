class A:
    def show(self):
        return f"class A"

class B(A):
    def show(self):
        return f"class B" + super().show()

class C(A):
    def show(self):
        return f"class C" + super().show()

class D(B,C):
    def show(self):
        return f"class D" + super().show()



if __name__ == "__main__":
    object_d = D()
    print(object_d.show())


