class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

student1 = Student("Harry", 85)
student2 = Student("Janet", 30)
did_pass = student1.check_pass_fail()
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)


class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def add(self,number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result

n1 = Complex(5, 6)
n2 = Complex(-4, 2)
result = n1.add(n2)
print("real=", result.real)
print("imag =", result.imag)