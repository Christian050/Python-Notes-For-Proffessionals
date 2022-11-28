# Python uses indentation to define control and loop constructs.

# Python uses the colon symbol (:) and indentation for showing where blocks of code begin and end

# Python, such as functions, loops, if clauses and other constructs, have no ending identifiers. All blocks start with a
# colon and then contain the indented lines below it. Eg:

def my_function():              # this is a function definition, note the colon (:)
    a = 2                       # this line belongs to the function because it's indented
    return a                    # this line also belongs to the same function
print(my_function())            # this line is OUTSIDE the function block

# OR

a = 10
b = 20

if a > b:               # the if block starts here
    print(a)            # this is part of the if block
else:                   # else must be at the same level as if
    print(b)            # this line is part of the else block

# Blocks that contain exactly one single-line statement may be put on the same line, though this form is generally not
# considered good style:

if a > b: print(a)
else: print(b)


# Attempting to do this with more than a single statement will not work:

# if x > y: y = x
    # print(y)              # IndentationError: unexpected indent

# if x > y while y != z: y -= 1         # SyntaxError: invalid syntax


# An empty block causes an IndentationError. Use pass (a command that does nothing) when you have a block with
# no content:

def will_be_implemented_later():
    pass

# Always use 4 spaces for indentation