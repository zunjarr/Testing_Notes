# OOPS Concept

# Encapsulation- Wrapping up of data into single entity

class Speed:

    def __init__(self):
        self.speed = 50
        self.__speedlimit = 90

    def get_speed(self):
        return self.speed

    def get_speedlimit(self):
        return self.__speedlimit


s = Speed()
print(s.get_speed(), s.get_speedlimit())
s.speed = 70
s.__speedlimit = 100
# print(Speed.speed, Speed.__speedlimit)
# s.__speedlimit = 100
print(s.get_speed(), s.get_speedlimit())
# ---------------------------------------------------
# Abstraction- Allows only important methods to be visible

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def display(self):
        pass

class B(A):
    def display(self):
        print('This is class B method')

b = B()
b.display()
# a = A()         # TypeError: Can't instantiate abstract class A with abstract method display
# a.display()
# ---------------------------------------------------
# Method overriding

class RBI_Bank:

    def rate(self):
        return 7

class SBI(RBI_Bank):

    def rate(self):
        return 9

r = SBI()
print(r.rate())

# ---------------------------------------------------
# Polymorphism- One thing have many forms
# Method overloading
class Testing:
    def cal2(self, a, b):
        p = a + b
        print(p)

    def cal2(self, a, b, c):
        p = a * b * c
        print(p)

t = Testing()
# print(t.cal2())
# print(t.cal2(20, 5))
print(t.cal2(2, 5, 5))
# ---------------------------------------------------

# Use of Super()

class Parent:

    def __init__(self):
        print('Its a Parent class constructor')

    def hello(self):
        print('Hello of Parent class')

class Child(Parent):

    def __init__(self):
        print('Its a Child class constructor')
        super().__init__()

    def hello(self):
        super().hello()
        print('Hello of Child class')

c = Child()
c.hello()
# -----------------------------------------------------

# Call one method in another method of the same class
class Test:

    def __init__(self):
        print('This is constructor')

    def method1(self):
        print('This is method1')

    def method2(self):
        print('This is method2')
        self.method1()
        self.__init__()

t = Test()
t.method2()
# -----------------------------------------------------
class Calculator:
    number = 7  # <-- Class variable

    def __init__(self, x, y):  # <-- Constructor
        self.x = x  # <-- Instance variable
        self.y = y
        print("I will call automatically when obj created")

    def getData(self):
        print("Executed getData method inside the class")

    def sum(self):
        return self.x + self.y


obj = Calculator(5, 7)
obj.getData()
print(obj.sum())
print(obj.number)

obj1 = Calculator(6, 10)
print(obj1.sum())
print(obj1.number)
# ----------------------------------------------------
