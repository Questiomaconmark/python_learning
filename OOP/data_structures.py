# brief overview of data structures.
# Python has 3 main ones built in, lists, dictionarys and tuples.
# Data structures are just ways to organize data and link it together.
# im only gonna go over lists and dictionarys, they are the most basic and most used 
my_list = [2, 5, 3, "hello"]
print(my_list)
# we access data within the structures in different ways determined by which data type it is. Lists use [] and an index number
# STARTING FROM 0 (0 is the first index number in the list)
print(my_list[0])
print(my_list[1])
print(my_list)
my_list[2] = 10
print(my_list)
# notice how we could change the data inside the list by accessing it using the index number

# data structures have lots of theory behind them, and are similar throughout languages. For instance python calls it a list, but most languages 
# have some similar structure for a dynamic array (array is the concept of a list of values). it differs in implementation, sometimes they are
# ordered (same position everytime), sometimes unordered, sometimes dynamic(can change size of the list) sometimes static (values can be changed,
# but size cannot). sometimes they are changable, and other times unchangable. A tuple is exactly like a list but you cannot change the value
# or size. 

# a dictionary is pythons name for a hashmap. (other languages have a similar structure, called hashmaps, maps or hashes. naming things are dumb)
my_dict = {
        "brand": "Chevy",
        "model": "Impala",
        "year": 2019
        }
print(my_dict)
print(my_dict["brand"])

# dictionarys store data in key value pairs. the left side is the key, the right side the value. We access the values through the keys. pretty much
# just labeling your data, insanely useful. an important note is that values can be the same, but keys have to be unique, no duplicates. 
# if you include a duplicate python will overwrite the value, and the previous value is lost forever in memory.  
