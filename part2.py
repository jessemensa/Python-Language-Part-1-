# THESE ARE MODULES IMPORTED AND USED IN PYTHON FILE 
from time import sleep, time 
from enum import Enum 

# Iterating and Making Decisions 
# Conditional Programming => brancing or looping 
submission = True 
if submission: 
    print("Congrats")

submission = False 
if submission: 
    print("You will be deducted")
else: 
    print("Congrats")

# using elif 
income = 800 
if income < 1000:
    tax_coefficient = 0.0 
elif income > 1000: 
    tax_coefficient = 0.2 
else: 
    tax_coefficient = 0.45 

# ternary operation can be used in place of if and else statements. 
order_total = 247 
if order_total > 100: 
    discount = 25 
else: 
    discount = 0 
print(order_total, discount) 

# ternary operation, shorter version of if and else statements  
discount = 25 if order_total > 100 else 0 
print(order_total, discount)

# Looping => repeating a block of code until a condition set changes. 
for number in [1, 2, 3, 4]: 
    print(number) 
# iterating over a range 
for number in range(5): 
    print(number) 
# iterating over a sequence 
surnames = ["Pokua", "Mensah", "Poku"]
for position in range(len(surnames)): 
    print(position, surnames[position])
# or 
for position, surname in enumerate(surnames):
    print(position, surname)

# multiple sequences 
people = ['Sheriff', 'Olu', 'Mark', 'Patrick']
ages = [28, 30, 33, 25]
for position in range(len(people)): 
    person = people[position]
    age = ages[position]
    print(person, age) 

# or 
for position, person in enumerate(people): 
    age = ages[position] 
    print(person, age) 

# or 
for person, age in zip(people, ages): 
    print(person, age) 
# or 
thepeople = ["Manaf", "Tom", "Yuda"]
ages = [24, 25, 28]
nationalities = ["Palestine", "Italy", "Indonesia"]
for person, age, country in zip(thepeople, ages, nationalities):
    print(person, age, country)

# While Loop 
n = 10 
while n <= 10:
    print(n)

# Break and Continue in Python 
for val in "String": 
    if val == "i":
        break 
    print(val)
print("The end") 

for val in "String":
    if val == "i":
        continue 
    print(val) 
print("The end")

# Functions => Bundle of code that performs a specific task. 
# Main goal, split task into small blocks 
# readability 
# reduce duplicate code 

price = 100 
final_price1 = price * 1.2 
final_price2 = price + price / 5.0 
final_price3 = price * (100 + 20) / 100.0 
final_price4 = price + price * 0.2 

# this code is rewritten using a function 
def calculate_price_with_vat(price, vat): 
    return price * (100 + vat) / 100 
# call function 
calculate_price_with_vat(100, 10)

# Scopes and names in Functions 
def firstFunction():
    test = 1 # local scope 
    print('first_function:', test) 
test = 0 # global scope 
firstFunction() 
print("global:", test) 

def outer():
    test = 1 # outer scope 

    def inner():
        test = 2 # inner scope 
        print('inner:', test) 
    inner() 
    print('outer:', test) 
test = 0 # global scope 
outer() 
print('global:', test) 

# Input Parameters 
x = 10 
def thefunc(x):
    print(x) 
thefunc(x) 


# Input Parameters 
# Positional 
def positionalArgs(a, b, c):
    print(a, b, c)
positionalArgs(1, 2, 3)

# Keyword arguments and default values 
def KeywordArgs(a, b, c):
    print(a, b, c) 
KeywordArgs(a = 1, c = 2, b = 3)

# Default Argument 
def defaultArgs(a, b = 4, c = 88):
    print(a, b, c) 
defaultArgs(1) 
defaultArgs(b = 5, a = 7, c = 9) 
defaultArgs(42, c = 9)

# Variable positional arguments 
def minimum(*numbers):
    if numbers:
        minimumnumber = numbers[0] 
        for value in numbers[1:]:
            if value < minimumnumber: 
                minimumnumber = value 
            print(minimumnumber) 
minimum(1, 12 -10, 9) 

def theFunc(*args):
    print(args) 
values = (1, 3, -7, 9) 
theFunc(values) 
theFunc(*values) 


# Dictionary, take dictionary as input 
def dictFunc(**kwargs):
    print(kwargs) 
dictFunc(a=1, b=42)


# Keyword-only arguments 
def kwo(*a, c):
    print(a, c) 
kwo(1, 2, 3, c=7)
kwo(c=7) 

def kwo2(a, b=42, *, c):
    print(a, b, c) 
kwo2(3, b = 7, c = 99) 
kwo2(3, c = 13) 


# Combining Input Parameters 
def inputParamCombine(a, b, c = 7, *args, **kwargs):
    print('a, b, c:', a, b, c) 
    print('args:', args) 
    print('kwargs:', kwargs) 

inputParamCombine(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})

# Anonymous Functions 
# 1. Regular Functions 
def multipleOfFive(numbers):
    return not number % 5 

def getMultiplesOfFive(numbers):
    return list(filter(multipleOfFive, range(n)))
print(getMultiplesOfFive(50))

# 2. Same as above using lambda 
def getMultipleOfFive(numbers):
    return list(filter(lambda k: not k % 5, range(numbers)))
print(getMultipleOfFive(50))

# Explaining Lambda 
def adders(a, b):
    return a + b 

adders_lambda = lambda a, b : a + b 


# Saving Time & Memory 
# map, zip and filter 
print(list(map(lambda * a: a, range(3), 'abc')))

grades = [18, 23, 30, 27, 15, 9, 22] 
avgs = [22, 21, 29, 24, 18, 18, 24] 
print(list(zip(avgs, grades)))
# same as map 
print(list(map(lambda *a: a, avgs, grades)))

# Filter 
test = [2, 5, 8, 0, 0, 1, 0] 
list(filter(lambda x: x > 4, test))

# Comprehensions 
# Normal iteration 
squares = [] 
for n in range(10):
    squares.append(n ** 2)
print(list(squares))

# using a comphrension to print list of numbers squared by 2
# this is a list comphrension 
print([n ** 2 for n in range(10)]) 

# dict comprehension 
square_dict = {number: number*number for number in range(1, 11)}
print(square_dict) 

# set comprehension
word = "hello" 
letters1 = set(c for c in word)
letters2 = {c for c in word}
print(letters1) 
print(letters2) 


# Generator Functions 
def getFirstSquares(number):
    return [x ** 2 for x in range(number)]
print(getFirstSquares(10))

def getSecondSquares(number):
    for x in range(number):
        yield x ** 2 
print(list(getSecondSquares(10)))

# Enumerations => import enumerations module at the top 
# Python support for enums 
class Shake(Enum): 
    VANILLA = 7 
    CHOCOLATE = 4 
    COOKIES = 9 
    MINT = 3 

# iterations 
for shake in Shake: 
    print(shake)

print(Shake.VANILLA)
print(repr(Shake.VANILLA))
# access the name and value 
print(Shake.VANILLA.name)
print(Shake.VANILLA.value)


# Object Oriented Python 
class Person():
    species = "Human" # instance variable 

man = Person() # instance of the class 

# Another one 
class Point():
    # Instance variables 
    x = 10 
    y = 7 
p = Point() 
# Accessing the instance variables 
print(p.x) 
print(p.y) 

# Methods 
class Square():
    side = 8
    def area(self):
        return self.side ** 2 
sq = Square() 
print(sq.area())

# Initialising 
class Rectangle(): 
    def __init__(self, sideA, sideB): 
        self.sideA = sideA 
        self.sideB = sideB 

    def area(self): 
        return self.sideA * self.sideB 
r1 = Rectangle(10, 4) 
print(r1.sideA, r1.sideB) 
print(r1.area())

# Inheritance and Composition 
class Engine(): 
    def start(self):
        pass 

    def stop(self): 
        pass 
# Inherited methods in Engine 
class ElectricEngine(Engine): 
    pass 

class V8Engine(Engine): 
    pass 

class Car(): 
    engine_cls = Engine 

    def __init__(self): 
        self.engine = self.engine_cls() 

    def start(self):
        print(
            'Starting engine {0} for car {1}... Wroom wroom'.format(
                self.engine.__class__.__name__, 
                self.__class__.__name__)
        )
        self.engine.start() 

    def stop(self): 
        self.engine.stop() 

class RaceCar(Car): 
    engine_cls = V8Engine 

class CityCar(Car): 
    engine_cls = ElectricEnginee 

class F1Car(RaceCar): 
    engine_cls = V8Engine 

car = Car() 
racecar = RaceCar() 
citycar = CityCar() 
f1car = F1Car() 
cars = [ car, racecar, citycar, f1car ]
for car in cars: 
    print(car.start()) 

# Accessing a base class 
class Book: 
    def __init__(self, title, publisher, pages): 
        self.title = title 
        self.publisher = publisher 
        self.pages = pages 

class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        Book.__init__(self, title, publisher, pages)
        self.format_ = format_ 

ebook = EBook("Learn to Speak Python", "Jesse Publishing", 400, 'PDF')
#Accessing properties in the class 
print(ebook.title)
print(ebook.publisher) 

# Another better way of Accessing base class 
class Bottle: 
    def __init__(self, bottletype, shape):
        self.bottletype = bottletype 
        self.shape = shape 

class VolticBottle:
    def __init__(self, bottletype, shape, size):
        super().__init__(bottletype, shape)
        self.size = size 

volticbottle = VolticBottle("Plastic", "Cylindrical", "Small")
print(volticbottle.shape) 


# Multiple Inheritance 
class Shape:
    geotype = 'Generic Shape' 

    def area(self):
        raise NotImplementedError 

    def getgeotype(self):
        return self.geotype 

class Plotter: 
    def plot(self, ratio, topleft):
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))

class Polygon(Shape, Plotter):  # Is a 
    geotype = "Regular Polygon" 

    def __init__(self, side):
        self.side = side 


# Static and Class Methods => methods placed inside class 
# static methods, methods bound to class rather than objects for that class 
# method can be called without object for that class 
class Calculate:
    @staticmethod 
    def addNumbers(x, y):
        return x + y 

print("Product: ", Calculate.addNumbers(15, 110))

# Class Methods, bound to class rather than object 
# class method works with the class but static method knows nothing about the class 
class Individual: 
    age = 28 
    def printAge(cls):
        print("The age is: ", cls.age)
Individual.printAge = classmethod(Individual.printAge)
Individual.printAge() 

# or 
class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

    @classmethod 
    def from_tuple(cls, coords):
        return cls(*coords)

    @classmethod
    def from_point(cls, point): 
        return cls(Point.x, point.y) 

p = Point.from_tuple((3, 7))
print(p.x, p.y) 
q = Point.from_point(p)
print(q.x, q.y) 


# Exception Handling 
def try_syntax(numerator, denominator):
    try: 
        print('In the try block: {}/{}'.format(numerator, denominator))
        result = numerator / denominator 
    except ZeroDivisionError as zde:
        print(zde) 
    else: 
        print("The result is: ", result)
        return result 
    finally: 
        print('Exiting')
print(try_syntax(12, 4))
print(try_syntax(11, 0))

# DONE. 






