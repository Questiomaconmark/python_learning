# so I didnt do a good job of explaining functions. Functions are pretty integral to programming, its what makes code resuable.
def my_function():
    print("hello from my function")

my_function()

# so whats happening here is we are making a function with the def statement. then it is running the block of code beneath it(determined by 
# indentation. that is the function declaration. we are setting it up.
# then beneath that we are doing a function call on line 5, we can do a function call instead of rewriting that print statement

param = "DAVID IS REAL DUMB"
def my_function_with_param(param):
    print("hello from my function with the parameter: " + param)

my_function_with_param("hello")
my_function_with_param("purple people pet pterodactyls")

# Parameters go inside the () in function. In the declaration we are setting up a variable that is locally scoped inside the function. Notice it
# we never actually use the globally scoped param variable I set up before hand. When we do a function call with a parameter we put our value 
# there.
# we can have multiple parameters and values are assigned by position
def foo(a,b):
    print(a)
    print(b)

foo("aaaa","bbb")
foo("see this one went first", "then this one")

# Python uses indentation to determine code blocks, but other languages use { } and ignore white space. Some of them will also use do and end 
# keyword. a keyword is something like def in our function declarations on line 2,12, or 22. or previously words like if and else and elif
# while and for and in are also keywords
