# =========== VARIABLES =============
name = "Karen"  # the variable name stores the value Karen

# to see things in the console you must use the print() function
print(name)

# best practices
# - snake_case
user_iq = 90
# - start with lowercase or undersore (if started with underscore it means private variable)
# - letters, numbers, underscores
# - case sensitive
# - don't overwite keywords
# if you want to define a constant you must write the name in capitals so other programmers know that
PI = 3.14

# you can use a shorthand way to asign values to a variable
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# augmented addignment operator
some_value = 5
some_value += 2
print(some_value)


# FUNDAMENTAL DATA TYPES
# ============ NUMBERS ==============
#  - int -> integer
2
100
23501

# you can o mathematical operations
2 + 4
2 - 4
2 * 4
2 / 4

# to know the type of a data you can use the function type()
type(4)
type(2 * 4)


#  - float -> floating point number
print(type(2 / 4))
# floating numbers ocupate more space in memory

# there is the idea of double ** and //
print(2**3)
print(2 // 3)
print(2 % 3)  # is used to represent the reminder of a division

# there are math functions built in python
print(round(2.5))  # round down the number
print(abs(-20))  # absolute value of a number

# operator precedence
print(20 - 3 * 4)
# ()
# **
# * /
# + -

# the bin() function retuirns a binary representation of the number
print(bin(5))

# to convert a string binary into a decimal number
print(int("0b101", 2))


# ============= STRINGS ============
#  - str
print(type("hello world"))

# you can use double quote, single quote o tripple quotes
long_string = """
WOW
0 0
---
"""
print(long_string)

# you can concatenate strings with the + sing
name = "karen"
last_name = "gil"
print(name + " " + last_name)

# to convert a number into string
num = 5
print(type(str(num)))

# escape sequence
wearher = 'It\'s "kind of" sunny'

# tab
wearher = '\t It\'s "kind of" sunny'

# new line
wearher = '\n It\'s "kind of" sunny'

# formated strings
name = "Karen"
age = 33
print(f"hi {name}. You are {age} years old")

# string indexes
# you can access different parts of a string
numbers = "0123456789"
print(numbers[0])
print(numbers[1])
print(numbers[0:5])
print(numbers[-2])

# length of  string
print(len(numbers))


# ============ BOOLEANS ================
True
False
