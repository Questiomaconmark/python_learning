# Data types
# I will try and not be super technical here, but it is important to understand so you know whats going on
# All data must be interpreted by the computer somehow, and it only has ones and zeros. We have to set conventions
# like data types so it can be processed properly, built into the processor itself (kinda). the basic ones are generally called
# primitives, these normally include integers(155), float point values(1.55), booleans(true or false), and characters
# 
# technically in python, all data types are treated as objects internally, but the "primitives" function like 
# primitives do in other languages. This leads to some odities though. Like there are is no character data type in python, only 
# strings (although nothing stops you from making a string of one character like "a" )
#
# python infers what type the variable is assigned by what value you assign it
# we can show this using pythons built in type() function, change x's value to True, or any 'string', or a floating point value(any number
# with a decimal)
# code
# x = True
# print(type(x))

# throw errors if you try and use functions or operations that expect other data types.
# code
# x = 2
# y = "2"
# print (x + y)
# print(x + str(y)) # there are standard functions to convert data to different types to account for issues like this

# python also lets you change the type of an already declared and assigned variable by setting a new value.
# code
# x = 2
# print(type(x))
# x = "hello"
# print(type(x))

# Throwing errors when it recieves the wrong datatype is why it is "strongly" typed, and letting you reassign the variable to a diffreent
# datatype is why it is called "dynamically" typed. 