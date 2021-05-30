# THESE ARE MODULES IMPORTED AND USED INSIDE PYTHON FILE 
from fractions import Fraction
# collections 
from collections import namedtuple
from collections import defaultdict 
from collections import ChainMap

# BEGINNING 
# Names and Namespace 
numb = 10 
address = "1 Grange Gardens"
employee = {
    'age': 28, 'role': 'CEO', 'SSN': 'SY123467C'
}
print(numb)
print(address) 
print(employee) 

# Scopes => textual region for python program inside wey we fit access the namespace.
# local scope => innermost dn contain local names 
# enclosing scope => scope wey dey any enclosing function inside 
# global scope => global names 
# built-in scope => built in names 
# How python scans when looking for names = local -> enclosing -> global -> built in 
# local vrs global scope 

def local(): 
    m = 7 # local scope 
    print(m) # prints here 

m = 5 # global scope 
print(m) # prints here 
local() 

def anotherLocal(): 
    print(m, 'printing from the local scope') # m is 5 
m = 5 # this executes first and prints 
print(m, 'printing from the global scope')
anotherLocal() # function is called and executes local scope 


def enclosing_func(): 
    m = 13 
    def local(): #inner scope
        print(m, 'printing from the local scope')
    local() 

m = 5 
print(m, 'printing from the global scope')
enclosing_func() 

# Objects and Classes in Python 
class Fowl: 
    # initialisation 
    def __init__(self, colour, size, breed):
        self.colour = colour
        self.size = size 
        self.breed = breed 
    
    # instance method 
    def sound(self): 
        print("Clucking")
local_fowl = Fowl("White", 30, "localbreed")
print(local_fowl.size)


# Built in Data Types 
# Numbers => Integers, Booleans, Reals, Complex Numbers, Fraction and Decimals 
a = 12 
b = 10 
print(a + b) # addition 
print(a - b) # subtraction 
print(a // b) # integer division 
print(a / b) # true division 
print(a * b) # multiplication 
print(a ** b) # power operator 
print(a % b) # remainder of the division 

# Booleans 
int(True) # true is 1 
int(False) # False is 0 
bool(1) 
bool(0) 
not True 
not False 
True and True # both must be the same 
False or True # atleast one must be 
boolTwo = 1 + True 
print(boolTwo) 

# Reals or Floating pt numbers 
pi = 3.1415926536

# Complex numbers => numbers that can be expressed in the form of a + ib 
# where a and b are real numbers and i is an imaginary unit 
c = 1.14 + 2.73j 
print(c.real) # real number 
print(c.imag) # imaginary unit 

# Fractions and Decimals , import fractions at the top of the file 
Fraction(10, 6) 
f = Fraction(10, 6) 
print(f.numerator)
print(f.denominator)


# Strings and Bytes 
str1 = "This is the first string" 

# Encoding and Decoding Strings 
s = "This is unicode" 
print(type(s)) 
encoded_s = s.encode('utf-8')
print(encoded_s) 

# Indexing and Slicing Strings 
s = "Jesse is a programmer and an enterprenuer" 
print(s[0]) 
print(s[5])
print(s[:10])
print(s[10:])
print(s[2:14])
print(s[2:14:3]) # start, stop and step 


# Tuples 
t = () 
print(type(t)) 

one_element_tuple = (42, )
three_element_tuple = (1, 2, 3)
a, b, c = 1, 2, 3
print(a) 
# membership testing 
3 in three_element_tuple 


# Lists 
[1,2,3]
list((1, 3, 5, 7, 9))
print(list('hello'))
# list operations 
a = [1, 2, 1, 3]
a.append(13) 
print(a) 
a.count(1) 
a.extend([5, 7])
print(a) 
a.index(2) 
a.insert(0, 17) 
print(a) 
a.pop(3) # element position 3 
# get the minimum and maximum numbers out 
min(a) 
max(a) 
len(a) 


# Sets => sets and frozen sets 
small_primes = set() 
small_primes.add(2) 
small_primes.add(3) 
print(small_primes) 
small_primes.add(10) 
small_primes.add(12) 
check = 4 in small_primes 
print(check) 

# Frozen sets => not mutable 
real_primes = frozenset([2, 3, 5, 7])
# can use operations add, remove etc on it 

# Dictionaries => key value pairs 
namesandages = dict(jesse=28, jessica=24) 
namesandage = {'Jesse': 28, 'Jessica': 24}
# an empty dictionary 
d = {} 
d['a'] = 1 
d['b'] = 2 
len(d) 
print(d) 
letscheck = 'c' in d 

realdict = dict(zip('hello', range(5)))
print(realdict)
realdict.keys() 
realdict.values() 


# The Collections Module
# namedtuple() => import above 
Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8) 
print(vision[0])
print(vision.left)
print(vision.right) 

# Default dict => import above 
dd = defaultdict(int) 
dd['age'] += 1 
print(dd) 
dd['age'] = 39 
dd['age'] += 1 
print(dd)

# ChainMap => import above 
default_connection = {'host': 'localhost', 'port': 3000}
connection = {'port': 4000}
conn = ChainMap(connection, default_connection)
print(conn['port'])
print(conn['host'])
print(conn.maps)
conn['host'] = "jesse.com"
print(conn.maps)


# How to Choose Data Structures 
# 1. Access, Operations, will data change over time, any modifications etc 


