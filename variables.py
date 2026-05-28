# Python is a high-level programming language known for its simple and readable syntax. It has the following features:

# Allows writing clean code with fewer lines.
# Supports multiple programming paradigms including object-oriented, functional and procedural programming.
# Widely used in web development, automation, data analysis, artificial intelligence and many other fields.
# Dynamically typed and has automatic garbage collection

print("Hello, World!")


# print() is a built-in Python function that instructs the computer to display text on the screen.
# "Hello, World!" is a string enclosed within quotes (either single ' or double ").
# Python uses indentation (spaces or tabs) to define code blocks instead of braces {} in C, C++ and Java .


# Assigning Values to Variables
# 1. Basic Assignment: Variables are assigned values using the = operator.

x = 5
y = 3.14
z = "Hi"

print(x, y, z)

# 2. Dynamic Typing: Python is dynamically typed, so the same variable can store different data types during execution.

x = 10
x = "Now a string"

# 3. Assigning Same Value: same value can be assigned to multiple variables in a single line.

a = b = c = 100
print(a, b, c)

# 4. Assigning Different Values: Multiple variables can also be assigned different values in a single line.

x, y, z = 1, 2.5, "Python"
print(x, y, z)


a, b, c = 100, 200, "Hellow how are you ?"

print(a, b, c)


# 1. Swapping Two Variables: Using multiple assignments, we can swap the values of two variables without needing a temporary variable.

a, b = 5, 10
a, b = b, a
print(a, b)


# 2. Counting Characters in a String: Assign the results of multiple operations on a string to variables in one line

word = "Python"
length = len(word)
print("Length of the word:", length)
