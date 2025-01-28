# Booleans and conditionals (control flow)

# booleans values are true and false and is a type of math/logic invented by George Boole 
# sidenote this is exactly how logic works in hardware, 0 = True, 1 = False. Or 0 = off, 1 = on. logic gates are just condition checks
# values are True and False. Operators are mainly == (equality check) or != (inequality check), > (greater than), < (less than)
# and of course <= and >= 
# 2 == 2 is True. 2 != 2 is False. likewise 2 == 1 is False. 2 != 1 is True. 
# we can control codeflow using Boolean values and if-else statement
# if (condition is true): run this code. Else(condition was not true): run this code
# code
# if True:
#     print('Indy is cute')
# else:
#     print('Indy is Ugly')
# print('THE CODE HAS DETERMINED indy is cute')

# this will cause the code to check if the condition is true, in this case 2 == 2. it will then run the block of code (determined by indentation)
# underneath the if statement, then it will skip the else statement, and continue running code top to bottom as normal

#we also have else if statements shortened to elif, to check for another condition before running the else block
# code
# if 2 != 2:
    # print('Indy is also hot')
# elif 2<4:
    # print("Indy's got a nice butt") #notice here I must use " " around the main string to include a ' inside the string
# else:
    # print("wouldn't touch her with a 10 foot pole")
# print("The code has determined, show me your butt")
# 
#the best way to understand elif is to understand that it is a nicer way of writing code like this
# if 2 == 3:
#     print("a")
# else:
#     if 2 == 4:
#         print("b")
#     else:
#         if 2 < 4456:
#             print("c")
#         else:
#             print('going back to normal now')
# versus
# if 2 == 3:
    # print("a")
# elif 2 == 4:
    # print("b")
# elif 2 < 4456:
    # print("c")
# else:
    # print('going back to normal now')

# we can use these two to check for multiple conditions at once. when using "and" both expressions must be true for the if statement to run
# Python uses the keywords "and" and "or"
# Sidenote && is commonly used for "and" and || is commonly used for "or" in other languages 
# code
# x = int(input())
# if x < 5 and x > 2:
    # print(str(x) + ' is in between 2 and 5')
# else:
    # print(str(x) + " is not in range")

# or will let the code run if either statement is true
# code
# x = input()
# if x =="hallo" or x == "tschuss":
    # print("german")
# else:
    # print("not german")

# can even be combined with one another using parenthesis
# code
# x = int(input())
# if (x < 10 and x > 0) or (x % 2 == 0):
    # print(str(x) +" is even or within 0-10")
# else:
    # print(str(x) + " is odd and outside of 0-10")

# Final note. Python uses the "not" keyword to inverse a truth value (boolean) value
# or if its easier not flips a boolean value (from false to true, or true to false). Other languages commonly use "!" for this
# code
# print(not True)
# x = False
# print(not x)
# 
# x = int(input())X
# print(str(x) + " is less than 5 returns " + str(x < 5))
# print(str(x) + " is not less than 5 returns " + str(not x < 5))