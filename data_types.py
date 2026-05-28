# Data types are used to define the type of value stored in a variable.
# They determine what kind of operations can be performed on the data. In Python, everything is treated as an object and each value belongs to a specific data type.
# The following are standard or built-in data types in Python:

# There are multiple data types in python


# 1.Numeric

# Integers: value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals).
# Float: value is represented by float class. It is a real number with a floating-point representation. It is specified by a decimal point.
# Complex: It is represented by a complex class. It stores numbers with real and imaginary parts. For example: 2+3j

a = 5  # integer
b = 5.1  # float
c = 2 + 5j  # complex


print(type(a))
print(type(b))
print(type(c))


# 2. String

# Strings are used to store text data. A string is represented using the str class and can be created using single, double or triple quotes.

s = "Welcome to the Geeks World"
print(s)
print(type(s))

# access string with index
print(s[1])
print(s[-1])

print(f"""Length of s is {len(s)}""")


# 3.List
# Lists are ordered and mutable collections used to store multiple items in a single variable. Elements in a list can be of different data types and are accessed using indexing.
# Indexing of list starts from 1

listA = ["hello", "TEXT", "JAPAN", 5]

print(listA[3])
print(listA[-3])


# 4.Tuple
# Tuples are ordered and immutable collections used to store multiple items in a single variable. Once created, tuple elements cannot be modified and are accessed using indexing.

# Note: A tuple with a single element must include a trailing comma, otherwise Python treats it as a normal value instead of a tuple.
# Indexing of tuple starts from 0

tupA = ("JAPAN", "INDIA", 10, 7)
tupB = ("OSAKA",)

print(tupA[3])
print(tupB[0])


# 5.Sets are unordered and mutable collections used to store unique elements. Since sets are unordered,
# elements cannot be accessed using indexing. Elements are usually accessed by iterating through the set using a loop.

s1 = {"a", "a", "b", "c", "b"}
print(s1)

s2 = {"Geeks", "For", "Geeks"}
for i in s2:
    print(i)


# 6.Dictionaries are used to store data in key:value pairs.
# Each key in a dictionary must be unique and values are accessed using their keys with square brackets [] or get() method.


dictA = {"first": "This is the value of first", 2: "This is the value of two"}

print(dictA[2])
print(dictA.get("first"))
