# Integer
a = 2
print(a)
# Output: 2

# Integer
b = 9223372036854775807
print(b)
# Output: 9223372036854775807

# Floating Point
pi = 3.14
print(pi)
# Output: 3.14

# String
c = 'A'
print(c)
# Output: A

# String
name = 'Christian K.'
print(name)
# Output: Christian K.

# Boolean
q = True
print(q)
# Output: True

# Empty value or null data type
x = None
print(x)
# Output: None


# Variable assignments work from left to right so the following below won't work:

# 0 = x
# Output: SyntaxError: can't assign to literal

# You cannot use python's keywords as a valid variable name. Eg:
import keyword
print(keyword.kwlist)

# Rules for variable naming:

#  1, Variables must start with a letter or an underscore.
x = True   # valid
_y = True  # valid

# 9x = False   # starts with a numeral
# => SyntaxError: invalid syntax

# $y = False # starts with a symbol
#  => SyntaxError: invalid syntax




# 2, The remainder of your variable name may consist of letters, numbers and underscores.
has_0_in_it = 'Still Valid'




# 3, Names are case sensitive
# x = 9
# y = X * 5
# # => NameError: name 'X' is not defined




# Data Types

a = 2
print(type(a))
# Output: <type 'int'>

b = 9223372036854775807
print(type(b))
# Output: <type 'int'>

pi = 3.14
print(type(pi))
# Output: <type 'float'>

c = 'A'
print(type(c))
# Output: <type 'str'>

name = 'Christian K.'
print(type(name))
# Output: <type 'str'>

q = True
print(type(q))
# Output: <type 'bool'>

x = None
print(type(x))
# Output: <type 'NoneType'>




# When you use = to do an assignment operation, what's on the left of = is a name for the object on the right.
# Finally, what = does is assign the reference of the object on the right to the name on the left.

a_name = 'an_object' # "a_name" is now a name for the reference to the object "an_object"


# You can assign multiple values to multiple variables in one line. Note that there must be the same number of
# arguments on the right and left sides of the = operator:

a, b, c = 1, 2, 3
print(a, b, c)
# Output: 1 2 3

# not

a, b, c = 1, 2  
# Output: ValueError: need more than 2 values to unpack

# or
  
a, b = 1, 2, 3
# Output: ValueError: too many values to unpack


# The error in last example can be obviated by assigning remaining values to equal number of arbitrary variables.
# This dummy variable can have any name, but it is conventional to use the underscore (_) for assigning unwanted
# values:

a, b, _ = 1, 2, 3
print(a, b)
# Output: 1, 2

# Note that the number of _ and number of remaining values must be equal. Otherwise 'too many values to unpack
# error' is thrown.



# Cascading Assignments:

a = b = c = 1                   # all three names a, b and c refer to same int object with value 1
print(a, b, c)
# Output: 1 1 1

b = 2                            # b now refers to another int object, one with a value of 2
print(a, b, c)
# Output: 1 2 1  # so output is as expected.

# The above is also true for mutable types (like list, dict, etc.) just as it is true for immutable types (like int, string,
# tuple, etc.):

x = y = [7, 8, 9]                       # x and y refer to the same list object just created, [7, 8, 9]
x = [13, 8, 9]                          # x now refers to a different list object just created, [13, 8, 9]
print(y)                                # y still refers to the list it was first assigned
# Output: [7, 8, 9]



# Things are a bit different when it comes to modifying the object (in contrast to assigning the name to
# a different object, which we did above) when the cascading assignment is used for mutable types. Take a look
# below, and you will see it first hand:

x = y = [7, 8, 9]                       # x and y are two different names for the same list object just created, [7, 8, 9]
x[0] = 13                               # we are updating the value of the list [7, 8, 9] through one of its names, x in this case
print(y)                                # printing the value of the list using its other name
# Output: [13, 8, 9]                    # hence, naturally the change is reflected


# Nested lists are also valid in python. This means that a list can contain another list as an element.

x = [1, 2, [3, 4, 5], 6, 7]     # this is nested list
print ( x[2] )
# Output: [3, 4, 5]

print ( x[2][1] )
# Output: 4

# Variables in Python do not have to stay the same type as which they were first defined -- you can simply use
# = to assign a new value to a variable, even if that value is of a different type.

a = 2
print(a)
# Output: 2

a = "New value"
print(a)
# Output: New value