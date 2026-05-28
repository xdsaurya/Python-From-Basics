# Conditional statements are used to control the flow of execution in a program based on specific conditions.
# They allow programs to execute different blocks of code depending on whether a condition evaluates to True or False.

# If Statement
# If statement is used to execute a block of code only when a specified condition evaluates to True.

x = 10
if x > 5:
    print("X is greater than 5")



# If-Else Statement
# If-else statement is used to execute one block of code if a condition is True and another block of code if the condition is False.

y = 3 

if y>10 :
    print("Y is greater than 10")
else :
   print("Y is less than 10")


# If-elif-else Statement
# elif statement is used to check multiple conditions in a program. 
# It executes a block of code when its condition evaluates to True after previous conditions evaluate to False.

age = 65

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
elif age <= 65:
    print("Adult.")
else:
    print("Old")


# Nested if-else Statement
# Nested if-else statement is an if-else statement placed inside another if or else block. It is used to check conditions within another condition.

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

# Match-Case Statement
# Match-Case statement is used to compare a value against multiple patterns and execute the matching block of code. It is similar to the switch-case statement available in other programming languages.

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")