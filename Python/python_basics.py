# python basics
## - topic 
# - note(commment)

# "=" is to assign, "==" is to check, != is dose not equal
# any var class function is public by default to make it protected use "_" to make it private use "__" before the name EX "__name"

## nested if statements 
# sourcery skip: remove-dict-keys, use-itertools-product
x = 10
y = 5
# each if stament has a else stament connected to it 
if x > y:
    print("x is greater than y")
    if x > 15: # this statement only runs if x > y and x > 15
        print("x is also greater than 15")
    else: # this runs if the if stament this is inside is false
        print("x is not greater than 15")
else: ## this else stament runs if the if the if statement connected to it is false 
    print("x is not greater than y")

# if "if 1" is false "else 1" runs if "if 1" is true "if 2" can run
# if "if 2" is true (which remember is only possible if "if 1" ran) "if 3" can run
# if if 2 is false "else 2" runs it is not possible for "else 3" or "else 1" to run 
# same way if "if 1" is false only the "else 1" runs 
#if1
#    if2 
#        if3
#        else3
#    else2
#else1 

## elif/ else if 
# if you plan to have multiple conditionals true use elif 
# think of elif like and if so if "if" is true and elif is true do "this" 
# but rememeber elif can run even if "if" dose not run and if elif runs else will not run, nested conditionals vary 

# if condition1:
    # Code to execute when condition1 is True
# elif condition2:
    # Code to execute when condition2 is True
# elif condition3:
    # Code to execute when condition3 is True
# ...
# else:
    # Code to execute when none of the conditions are True

# as case and switch 
#def switch_case(case_value):
#    if case_value == 1:
#        print("This is case 1")
#    elif case_value == 2:
#        print("This is case 2")
#    elif case_value == 3:
#        print("This is case 3")
#    else:
#        print("This is the default case")

# Example usage:
#value = 2
#switch_case(value)

# In this example, we first check if x is greater than 10. If that condition is false, it proceeds to the elif clause
# and checks if x is less than 10. If both conditions are false, it falls back to the else clause.
# You can use multiple elif clauses to handle different cases or conditions in a structured way, 
# making your code more organized and easier to read.
x2 = 10
if x2 > 10:
    print("x2 is greater than 10")
elif x2 < 10:
    print("x2 is less than 10")
else:
    print("x2 is equal to 10")

## if and
x3 = 5
y3 = 7

if x3 == 5 and y3 == 7:
    print("Both conditions are true")

# using a mock swich case system
def switch_case(case_value):
    if case_value == 1:
        print("This is case 1")
    elif case_value == 2:
        print("This is case 2")
    elif case_value == 3:
        print("This is case 3")
    else:
        print("This is the default case")

# Example usage:
# sourcery skip: use-itertools-product
# sourcery skip: remove-dict-keys
value = 2
switch_case(value)

## While loops

# while loops are loops that run if a statment is true the loop will check each time it runs if statment is true 
# then they will run forever until the condition it ran on is false or the loop breaks
count = 1
while count <= 5: # loop will run until this statement is false 
    print(count)
    count += 1
    break # this will break the while loop scince the while loop only had 1 chance to run and then broke the loop will only print 1
    # Increment the count by 1 in each iteration
    # once count is 6 the loop breaks scince the loop breaks it cannot run so 6 will not be printed 

## for loops !!
#In Python, a for loop is a control structure that is used to iterate over a sequence 
# (such as a list, tuple, string, or range) or any iterable object.
# for variable in sequence:
    # Code to be executed for each item in the sequence
# Here's how a for loop works:
# the loop begins by iterating over the elements in the specified sequence.
# For each iteration, the current element from the sequence is assigned to the variable.
# The code block within the loop, indented under the for statement, is executed once for each element in the sequence.
# After executing the code block for each element in the sequence, the loop continues with the next element, 
# and so on, until all elements in the sequence have been processed.
#ex
for i in [4,8]: print(i)

# iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# iterating over string 
word = "Python"
for letter in word:
    print(letter)

# using for loop with range range just creates a list of num from 0 if no start given till the number given "5 here"
for i in range(5): # will only go till 4 as index stops one short of num given in range 
    print(i)

# iterating over a dictionarys keys or items 
person = {"name": "Alice", "age": 30}
for key in person.keys():
    print(key)

for key, value in person.items():
    print(f"{key}: {value}")

# double nested for loop
# The outer loop iterates over the values 0, 1, and 2 (specified by range(3)).
# For each iteration of the outer loop, the inner loop iterates over the values 0 and 1 (specified by range(2)).
# Inside the inner loop, we print a message that includes the current values of both the outer and inner loop indices.
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"Outer loop index: {i}, Inner loop index: {j}") # in a printf everything must be in "" a var must be in {}


## Functions

# you can define a function in Python using the def keyword, followed by the function name and a pair of parentheses. 
# Any parameters (input values) the function requires are listed inside the parentheses. 
# The function body is indented and contains the code to be executed when the function is called

# in this function called greet we have one parameter (var/ placeholder) "name" 
# this parameter can be changed like name + x but when calling function "name" the parameter must be defined
# we call this value for the parameter "var" a argument. Parameter = x argument = 5 so x=5
### NOTE the number of parentheses must equal the number if Arguments (name) =! ("alice", "chains")
# you can have zero parameters and just a function and you can define a parameter a default value (optinal paramters) 
def greet(name):
    """
    This is a docstring that provides a brief description of the function.
    """
    print(f"Hello, {name}!") # this is a f print statement format = f"String, {variable}!" "!"  & "," is part of string
    # in this statment vars must be in {} while inside the string while all string is inside ""

## Function call
greet("Alice") # function name (argument) argument meaning value or var "parenthisis"

# ex2 with a parameter and a optinal parameter. parameter 2 is defined and is 0 by default but can be changed if wanted
def add(a, b=0): # b is a default parameter if nothing is entered for be it will = 0
    """
    Function with a default argument.
    """
    return a + b

result1 = add(3, 4)  # Positional arguments, result1 = 7
result2 = add(5)     # Default argument, result2 = 5, b = 0 so 5+0=0

# ex3
def add(a, b):
    return a + b # return can be used to return something "like print" can retuen true or flase

result = add(3, 4)  # result = 7

## random random 
import random    
print(random.randint(1,5)) # (start, end)

# eecs 
"""hello"""

## lambda function (anonymous function)
# how to create a lambda function in python 
# lambda are simple functions 
square = lambda x: x ** 2
result = square(5)  # result = 25

## higher order functions
# Python supports advanced features like function decorators and higher-order functions, 
# which allow you to modify orextend the behavior of functions python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
# @mydeecorator my_decorator is a function that takes another function func as its argument. 
# Inside my_decorator, there's an inner function called wrapper. wrapper is defined inside my_decorator and 
# serves as a wrapper function that surrounds the execution of func. It performs some actions before and after calling func.
# @my_decorator is a decorator syntax in Python. When you decorate a function with @my_decorator, 
# it means that you are applying the my_decorator function to the decorated function.
#  In your example, you decorate the say_hello function with @my_decorator.
# When you call say_hello(), you are actually calling the wrapper function that my_decorator returned.
#  This is how decorators work in Python. The decorated function (say_hello) is replaced by the wrapper function, 
# which adds functionality around the original function.
@my_decorator
def say_hello(): # this is func()
    print("Hello!")

say_hello() # calling function (this one has no parameters)



## python classes
# __init__  is the constructer it initilizez the values of function
#  it allows you to set innitial vals of a object by specifing ots values
# In Python, when you want to create instance variables within a class, 
# it's essential to use self to distinguish between instance variables and local variables or function parameters. 
# In the Person class, __init__ takes two parameters: name and age. 
# These parameters are used to initialize the name and age attributes of the object.
# self is a refrence to the object itself When you create a new instance of a class, 
# such as person = Person("Alice", 30), self inside the __init__ method refers to that specific instance (in this case, person).
# self is used to access and manipulate the attributes of the object. In the __init__ method, 
# self.name and self.age are used to set the name and `age

class Person: # class Name:
# By using self, you explicitly declare the variable as an instance variable,
#  making it accessible throughout the class methods. Without self, 
# you would create a local variable with the same name, which would only exist within the specific method 
# and wouldn't be accessible elsewhere in the class.
# Using self allows each instance of the class to have its own copy of the variable. 
# If you don't use self, all instances would share the same variable, which may not be what you want. 
# Instance variables with self are unique to each object, allowing you to have different values for different instances.

#. If you used name = name, it would create a local variable within the constructor method, 
# and you wouldn't be able to access it outside that method thats why you do self.name = name
    def __init__(self, name, age): #  this function is the counstructer (__init__) means constructer 
        self.name = name # initilizing attribute/ parameter name so it can be used outside class 
        self.age = age

    def greet(self): # the self parameter allows greet to access the self parameters name and age
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# creating the objects using the cunstructer 
#object --> name = classname(parameters)
person1 = Person("Alice", 30) # the object has two parameters name, age. self is not a parameter
person2 = Person("Bob", 25)

print(person1.name)  # Output: "Alice"
print(person2.age)   # Output: 25

#Methods are functions associated with objects. You can call methods on an object using dot notation.
greeting = person1.greet()
print(greeting)  # Output: "Hello, my name is Alice and I am 30 years old."


## inheretance Inheritance allows you to create a new class that is a modified version of an existing class.
#  The new class can inherit attributes and methods from the parent class and also add its own. also called subclass
# here instred of using the student classes own name and age it borows name and age from person class using super method

# In this example, the Student class inherits from the Person class and adds its own attribute (student_id) and method (study).
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying hard."

student = Student("Carol", 22, "12345")

## class variables Class variables are shared among all instances of a class. 
# They are defined within the class but outside of any method.
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


##Encapsulation refers to the practice of restricting direct access to some of an object's components. 
# In Python, attributes and methods can be public, protected, or private. 
# Public attributes and methods can be accessed directly,
# protected attributes and methods are denoted with a single underscore (e.g., _protected_attr), 
# and private attributes and methods are denoted with a double underscore (e.g., __private_attr).

class MyClass:
    def __init__(self):
        self.public_attr = "I'm a public attribute"
        self._protected_attr = "I'm a protected attribute"
        self.__private_attr = "I'm a private attribute"

    def public_method(self): #Public members are accessible from anywhere, both inside and outside the class.
        return "I'm a public method"

    def _protected_method(self): #Protected members are not meant to be accessed from outside the class 
        # but can still be accessed if desired.
        return "I'm a protected method"

    def __private_method(self): #Private members are intended to be private and are not accessible from outside the class.
        return "I'm a private method"

## private var ex
class MyClass:
    def __init__(self):
        self.__private_var = 42

    def get_private_var(self):
        return self.__private_var

# Creating an instance of MyClass
obj = MyClass()

# Accessing the private variable using a public method
value = obj.get_private_var()
print(value)  # This will print: 42

# Attempting to access the private variable directly (not recommended)
# This will not generate an error, but it's discouraged.
# print(obj.__private_var)  # This is discouraged and not recommended


## special methods Python provides special methods (also known as magic methods or dunder methods) 
# that you can define in your classes to customize their behavior. For example, 
# you can define __str__ to control how an object is represented as a string when using str()
class MyClass: 
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value {self.value}"


## String methods 
# In Python, strings are sequences of characters enclosed in either single (') or double (") quotes """ makes a docstring 
str1 = 'Hello, World!'
str2 = "Python is awesome!"

full_string = f"{str1} {str2}" # or full_string = str1 + " " + str2
print(full_string)  # Output: "Hello, World! Python is awesome!"
    
# bultin methods

# returns legnth of string
length = len(str1)  # length = 13 

# converts upercase to lowercase and vise versa
upper_str = str1.upper()  # upper_str = "HELLO, WORLD!"
lower_str = str2.lower()  # lower_str = "python is awesome!"

# removes leading and trailing whitespaces
whitespace_str = "   Some text with spaces   "
stripped_str = whitespace_str.strip()  # stripped_str = "Some text with spaces"

# replaces occurance of substring with another substring
replaced_str = str1.replace("World", "Python")  # replaced_str = "Hello, Python!"

# splits strings into substrings based on dilimeter
words = str2.split(" ")  # words = ["Python", "is", "awesome!"] here it splits at (" ") "a space"

# combines a list of strings into one string 
word_list = ["Python", "is", "awesome!"]
joined_str = " ".join(word_list)  # joined_str = "Python is awesome!"

# find() and index(): Searches for a substring within a string and returns its index.
#  find() returns -1 if not found, while index() raises an exception.
position1 = str1.find("World")  # position1 = 7 "7 is the index of the first letter of searched string'
position2 = str2.index("is")     # position2 = 7

# to check if string starts with or ends with a letter or substring
starts_with_hello = str1.startswith("Hello")     # True
ends_with_exclamation = str2.endswith("awesome!")  # True

# counts the number of occerances of a substring within a string
count_is = str2.count("is")  # count_is = 1

# capitalize first letter of string 
capitalized_str = str1.capitalize()  # capitalized_str = "Hello, world!"

# isalpha(), isdigit(), isalnum(), isspace(): These methods check if the string contains
#  alphabetic characters, digits, alphanumeric characters, or only whitespace characters.
is_alpha = str1.isalpha()        # False (contains a comma and space)
is_digit = str1.isdigit()        # False (contains non-digits)
is_alnum = str2.isalnum()        # False (contains spaces and punctuation)
contains_spaces = str1.isspace()  # False (contains non-whitespace characters)

# To replace a substring with another substring in a Python string, you can use the str.replace()
# new_string = original_string.replace(old_substring, new_substring)
# original_string: This is the string in which you want to perform the replacement.
# old_substring: This is the substring you want to replace.
# new_substring: This is the substring that will replace the old substring.
original_string = "Hello, World!"
new_string = original_string.replace("World", "Python")
print(new_string)  # Output: "Hello, Python!"
#Keep in mind that the str.replace() method does not modify the original string; instead, 
# it returns a new string with the replacement performed. If the old substring is not found in the original string, 
# the method returns the original string unchanged.

# If you want to replace all occurrences of a substring within a string, 
# you can provide a third argument to the str.replace() method, which specifies the maximum number of replacements to make.
#  To replace all occurrences, set this argument to a large number or omit it entirely:
original_string = "This is a test. This test is important."
new_string = original_string.replace("test", "example")
print(new_string)  # Output: "This is a example. This example is important."

# reverse a array python 

