# bool: A boolean value of either True or False. Logical operations like and, or, not can be performed on booleans. Eg.
x = 10
y = 20

x or y              # if x is False then y otherwise x
x and y             # if x is False then x otherwise y
not x               # if x is True then False otherwise True

# Boolean is also an int.
# The bool type is a subclass of the int type and True and False are its only instances:

issubclass(bool, int)           # True
isinstance(True, bool)          # True
isinstance(False, bool)         # True


# If boolean values are used in arithmetic operations, their integer values (1 and 0 for True and False) will be used to return an integer result

True + False == 1           # 1 + 0 == 1
True * True == 1            # 1 * 1 == 1




# Numbers

# int: integer number

a = 2
b = 100
c = 123456789
d = 38563846326424324

# Integers in Python are of arbitrary sizes.


# float: Floating point number

a = 2.0
b = 100.e0
c = 123456789.e1


# complex: Complex numbers
a = 2 + 1j
b = 100 + 10j

# The <, <=, > and >= operators will raise a TypeError exception when any operand is a complex number.



# Strings
# str: a unlcode string. The type of 'hello'
# bytes: a byte string. The type of b'hello' 


# Sequences and Collections

# Python differentiates between ordered sequences and unordered collections (such as set and dict).

# strings (str, bytes, unicode) are sequences
# reversed: A reversed order of str with reversed function

a = reversed('hello')

# tuple: An ordered collection of n values of any type (n >= 0).

a = (1, 2, 3)
b = ('a', 1, 'python', (1, 2))
b[2] = 'something else'              # returns a TypeError

# Supports indexing; immutable; hashable if all its members are hashable

# list: An ordered collection of n values (n >= 0)

a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
b[2] = 'something else'                         # allowed

# Not hashable; mutable.


# set: An unordered collection of unique values. Items must be hashable.

a = {1, 2, 'a'}



# dict: An unordered collection of unique key-value pairs; keys must be hashable.

a = {1: 'one',
    2: 'two'}

b = {'a': [1, 2, 3],
    'b': 'a string'}


# An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__()
# method), and can be compared to other objects (it needs an __eq__() method). Hashable objects which
# compare equality must have the same hash value.


# Built-in constants

# In conjunction with the built-in datatypes there are a small number of built-in constants in the built-in namespace:

# True: The true value of the built-in type bool
# False: The false value of the built-in type bool
# None: A singleton object used to signal that a value is absent.
# Ellipsis or ...: used in core Python3+ anywhere and limited usage in Python2.7+ as part of array notation. numpy and related packages use this as a 'include everything' reference in arrays.
# NotImplemented: a singleton used to indicate to Python that a special method doesn't support the specific arguments, and Python will try alternatives if available.

a = None                # No value will be assigned. Any valid datatype can be assigned later

# None doesn't have any natural ordering. Using ordering comparison operators (<, <=, >=, >) isn't supported anymore and will raise a TypeError



# Testing the type of variables

# In python, we can check the datatype of an object using the built-in function type.

a = '123'
print(type(a))
# Out: <class 'str'>

b = 123
print(type(b))
# Out: <class 'int'>


# In conditional statements it is possible to test the datatype with isinstance. However, it is usually not encouraged to rely on the type of the variable.

i = 7
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i)
i += 1


# To test if something is of NoneType:

x = None
if x is None:
    print('Not a surprise, I just defined x as None.')



# Converting between datatypes

# You can perform explicit datatype conversion. For example, '123' is of str type and it can be converted to integer using int function.

a = '123'
b = int(a)

# Converting from a float string such as '123.456' can be done using float function.

a = '123.456'
b = float(a)
c = int(a)                  # ValueError: invalid literal for int() with base 10: '123.456'
d = int(b)                  # 123


# You can also convert sequence or collection types

a = 'hello'
list(a)                   # ['h', 'e', 'l', 'l', 'o']
set(a)                    # {'o', 'e', 'l', 'h'}
tuple(a)                  # ('h', 'e', 'l', 'l', 'o')



# Explicit string type at definition of literals

# With one letter labels just in front of the quotes you can tell what type of string you want to define.

# b'foo bar': results bytes in Python 3, str in Python 2
# u'foo bar': results str in Python 3, unicode in Python 2
# 'foo bar': results str
# r'foo bar': results so called raw string, where escaping special characters is not necessary, everything is taken verbatim as you typed

normal = 'foo\nbar' # foo
                    # bar
escaped = 'foo\\nbar' # foo\nbar
raw = r'foo\nbar' # foo\nbar


# Mutable and Immutable Data Types

# An object is called mutable if it can be changed. For example, when you pass a list to some function, the list can be changed:

def f(m):
    m.append(3)             # adds a number to the list. This is a mutation.

x = [1, 2]
f(x)
x == [1, 2]                  # False now, since an item was added to the list


# An object is called immutable if it cannot be changed in any way. For example, integers are immutable, since there's no way to change them:
g = None

def bar():
    x = (1, 2)
    g(x)
    x == (1, 2)                 # Will always be True, since no function can change the object (1, 2)


# Note that variables themselves are mutable, so we can reassign the variable x, but this does not change the object that x had previously pointed to. It only made x point to a new object.
# Data types whose instances are mutable are called mutable data types, and similarly for immutable objects and datatypes.

# Examples of immutable Data Types:
int, #long, float, complex
str
bytes
tuple
frozenset


# Examples of mutable Data Types:
bytearray
list
set
dict