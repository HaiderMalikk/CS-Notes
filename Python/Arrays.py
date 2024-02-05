print("hello world")
# start of journy

## - subtopic 
# - note

# arrays using arrays 
from array import array
#You can create an array by specifying its type code and initializing it with elements. 
# The type code determines the data type of the elements in the array. Here are some common type codes:

#'i': Signed integer (e.g., array('i', [1, 2, 3]))
#'f': Floating-point (e.g., array('f', [1.0, 2.0, 3.0]))
#'d': Double-precision floating-point (e.g., array('d', [1.0, 2.0, 3.0]))
#'u': Unicode character (e.g., array('u', 'hello'))

#ex 
int_array = array('i', [1, 2, 3, 4, 5])

# accesing elemts 
print(int_array[0])  # Output: 1
print(int_array[2])  # Output: 3

# modifying elemets 
int_array[1] = 99

# unlike lists arrays have a fixed size . If you need to add more elements, 
# you'll have to create a new array with a larger size and copy the elements from the old array to the new one.
int_array = array('i', [1, 2, 3])  # Creating an array with size 3
new_int_array = array('i', [0] * 6)  # Creating a new array with size 6 [0] * 6 makes a array with 6 [0] elements 
new_int_array[:3] = int_array  # Copying elements from the old array to the new one
int_array = new_int_array  # Updating the reference

#Arrays support various methods for common operations, including slicing, concatenation, 
# and searching for elements. You can refer to the Python documentation for the array module for more details.
sub_array = int_array[1:4]  # Slicing: creates a new array with elements 2, 3, 4
concatenated_array = int_array + array('i', [6, 7, 8])  # Concatenation
index = int_array.index(3)  # Searching for the index of element 3

# 2d arrays is a array within a array it has 2 indexes matrix[0][0] is 1 [1][2] is 6
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][0])


### arrays [this, is, a, array]
# use numpy library to work with arrays
import numpy as np
## use [] to create and store array elemnts  
my_array = np.array([1,2,3,4,5]) #name = np.function([elements])
my_array_float = np.array([1.1, 2.2, 3.3, 4.4, 5.5], dtype=np.float64) #[array elements], data type (dont have to declare data type)

## now you have created a array to accese its elemets using a index
# starts at 0, to accese the array end to start use -1, -1 is the last element in a array
print(my_array[0]) # first element
# output: 1
print(my_array[2]) # if i wanted to print the third element i would stop i index before here thats 2
#output: 3
print(my_array[-1]) # accese last element -2 would give me the sencond last and so on
#output: 5

## to modify a array (change a element)
my_array[3] = 10 # simply assign the element using the [index] and setting it = to the new value
print (my_array)
# output: [1, 2, 3, 10, 5]

## Modifing entire arrays
array1 = np.array([1,2,3,4,5]) 
array2 = np.array([6,7,8,9,10]) 
# a simple operation is to add the two arrays element wise
# this adds each element in the array (array1[0] + array2[0])
result = array1 + array2
print(result)
# output [7, 9, 11, 13, 15]
# thier are also other operations ex multiply divide etc...

## finding values in arrays  
min_value = np.min(my_array)
print(min_value)
# output: 1 

max_value = np.max(my_array)
print(max_value)
# output: 10 

## sorting arrays using np.sort
my_array_tosort = [5,3,1,4,2]
sorted_array = np.sort(my_array_tosort)
print(sorted_array)
# output: [12345] # sort smallest to largest
# to reverse the array use np.flip func
reversed_array = np.flip(my_array_tosort)
print(reversed_array)
# output: [24135]
# to sort the list in decending order first sort the array then flip it
decending_array = np.flip(sorted_array)
print(decending_array)
# output [54321]

## mean (avg) and median(mid val) of array
mean_val = np.mean(my_array)
print(mean_val)
# output 3.0
median_val = np.median(my_array)
print(median_val)
# output 3.0

## matrix multiplication 2d array

matrix1 = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
matrix2 = np.array([[7.7, 8.8,], [9.9, 10.10], [11.11, 12.12]])
#multiplying 
result = np.dot(matrix1, matrix2)
print(result)
# output:
# [[66.913 71.896]
# [161.656 174.262]]

## trasposing a matrix to swap its rows and columns 
matrix = np.array([[1,2,3], [4,5,6]])
#trasposing the matrix
trasposed_matrix = np.transpose(matrix)
print(trasposed_matrix)
#output:
# [[1 4]
# [2 5]
# [3 6]]
# element of 2d arrays first element corrisponds to sub array second to the element of subarray
print("at matrix subarray 2 elemet 2:", matrix[1][1])

##### other usefull Stuff #####
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)  # Prints (5,) - a 1D array with 5 elements
print(arr.dtype)  # Prints int64 - data type of elements
print(arr.size)   # Prints 5 - total number of elements
print(arr.ndim)   # Prints 1 - number of dimensions (1 for 1D)

# index slicing, arrayname[start index:end index] 
# this creats a new array same as original exept only has elements 1 to 4 dose not modify original array
print(arr[1:4])  # Slice from index 1 to 3 (2, 3, 4)

# element addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a + b  # Element-wise addition

## there are so many things you can do with np library
data = np.array([1, 2, 3, 4, 5])
print(np.sum(data))  # Sum of all elements

arr = np.array([[1, 2], [3, 4]])
reshaped_arr = arr.reshape((4, 1)) # this reshapes the format 4 = rows, 1 = column so arr goes from 2x2 -> 4x1
transposed_arr = arr.T # The T attribute transposes the array, swapping rows and columns. 
print(reshaped_arr) 
print(transposed_arr)
# print(arr) # this is the new "arr" we nammed another array "arr" previously so it updates and this becomes the new arr

# to create a array without typing every single element
my_array_shortcut = list(range(1, 11)) # prints 1-10 and index starts at 0 so goes 1 number before 11
print(my_array_shortcut)
""" comment """

## ex of func and array
def array(a, b, c):
    array = [a, b, c]
    array.sort()
    array2 = array[::-1]  # Reverse the sorted list and store it in array2
    return f"Sorted smallest to largest: {array}, Sorted largest to smallest: {array2}"

# sourcery skip: convert-any-to-in, merge-list-append, use-any, use-named-expression, use-next
result = array(5, 3, 2)
print(result)

## add arrays gpt 

### lists
my_list = [1, 2, 3, 4, 5] # simple list
mixed_list = [1, "Hello", 3.14, True, ["apple", "banana", "cherry"]] # array can have diffrent typs of elemets 

my_list = [1, 2, 3, 4, 5]

# Accessing elements by index index start at zero the last index is -1
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3

# Negative indexing to access elements from the end
print(my_list[-1])  # Output: 5
print(my_list[-2])  # Output: 4

# modifing elements of list 
my_list = [1, 2, 3, 4, 5]
# Modifying an element
my_list[2] = 99
print(my_list)  # Output: [1, 2, 99, 4, 5]

# adding stuff to lists
my_list = [1, 2, 3]

# Append an element to the end of the list
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Insert an element at a specific index replacing index
my_list.insert(1, 99) # (index num, element to be inserted)
print(my_list)  # Output: [1, 99, 2, 3, 4]

# removing stuff from lists
my_list = [1, 2, 3, 4, 5]

# Remove a specific value
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]

# Remove an element by index
popped_value = my_list.pop(2)  # Removes the element at index 2 (value 4) and returns it
print(my_list)  # Output: [1, 2, 5]
print("Popped value:", popped_value)  # Output: Popped value: 4

# to get indexof a value in 1dlist
print(my_list.index(1)) # returns position of 1 in mylist

## Array Broadcasting:
# NumPy also supports broadcasting, which allows you to perform operations on arrays of different shapes in certain cases.

## Advanced Array Operations:
# NumPy provides tools for advanced operations such as matrix multiplication (np.dot or @ operator), element-wise comparisons, and more.

## Array Manipulation Functions:
# NumPy offers functions like concatenate, split, stack, hstack, and vstack for combining, splitting, and stacking arrays.

## Array Iteration:
# You can iterate through the elements of an array using loops or NumPy-specific functions like np.nditer. 

### here add serching arrays ###########
## serching 1d arrays 
my_list = [1, 2, 3, 4, 5]

# Using a for loop to iterate over elements
for element in my_list:
    print(element)

search_element = 3 # target
found = False # found starts of as false utill target found then slips to true 
count = 0
# for loop is a loop that goes through elements of a list or array 
# for each item in my list, see if item = to target if item = target loop runs and flips found to true 
# "if found" is ran if found is true and print found
for item in my_list: # "item" = var(we just created this think of it as a int that dose +1 to itself every time the for loop runs)
    # "in" is a way to point to a list, "my list" is our list
    if item == search_element:
        found = True # if found found flips to true
        count += 1 # add 1 to count count now = 1
        break # break ends the serch by closing the for loop

if found: # if found has no condition as FOUND is only true and false so if found is true this if statement will run
    print(f"{search_element} found in the list. {count}: times")
else: # if found is false the else statement is ran
    print(f"{search_element} not found in the list.")

## second method for serching 
search_element = 3 # set a target 

if search_element in my_list: # insted of flipping a bolean to true just print
    print(f"{search_element} found in the list.")
else:
    print(f"{search_element} not found in the list.")

## 2d list serching
# making a 2d array 
# this is array 
    #[1 this is subarray 0 element 0, 2, 3] this is subarray 0,
    #[4 this is subarray 1 element 0, 5, 6] this is subarray 1,
    #[7, 8, 9 this is subarray 2 element 2] this is subarray 2
_2Darray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# serching is very simmilar to 1d serching but add a extra fpr loop 
target = 5
found = False

# the double for loop first selects the first subarray using the first for loop 
# then the second for loop itirates throught each element in the subarray selected by first for loop 
# starting from element 0 in sub array 0 row = index0 item = index0 item = 1 
for subarray in _2Darray: # this selects each sub array in the array 
    for element in subarray: #this selects each element in the sub array 
        if element == target:
            found = True
            break

if found:
    print(f"{target} found in the 2D list.")
else:
    print(f"{target} not found in the 2D list.")

# alternate to serching a 2d list
search_element = 5

found = any(search_element in row for row in _2Darray) #any 

if found:
    print(f"{search_element} found in the 2D list.")
else:
    print(f"{search_element} not found in the 2D list.")


# to get posiotion of target you have to serch each list for the element 
_2Darray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5
found = False
row_index = None
col_index = None

for row_idx, subarray in enumerate(_2Darray):
    for col_idx, element in enumerate(subarray):
        if element == target:
            found = True
            row_index = row_idx
            col_index = col_idx
            break
    if found:
        break

if found:
    print(f"{target} found in the 2D list at row {row_index}, column {col_index}.")
else:
    print(f"{target} not found in the 2D list.")

#In this code:
#We use enumerate() to get both the row index (row_idx) and the elements of each subarray, 
# and the column index (col_idx) and the elements of each subarray.
#We set row_index and col_index when we find the target element.
#We also use break statements to exit the loops once we find the target element.
#With these changes, the code will correctly print the row and 
# column indices of the target element if it's found in the 2D list.

## alternate position of target method 
_2Darray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5
found = False
row_index = None
col_index = None

for row_idx, subarray in enumerate(_2Darray):
    if target in subarray:
        col_index = subarray.index(target)
        row_index = row_idx
        found = True
        break

if found:
    print(f"{target} found in the 2D list at element {_2Darray[row_index][col_index]} (row {row_index}, column {col_index}).")
else:
    print(f"{target} not found in the 2D list.")

## Using i and j to serch lists 
# Create a 2D array (list of lists)
my_2d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Define the indices 'i' and 'j' for the element you want to access
i = 1  # Row index
j = 2  # Column index

# Check if the indices are within bounds
if 0 <= i < len(my_2d_array) and 0 <= j < len(my_2d_array[0]):
    # Access the element using 'i' and 'j'
    element = my_2d_array[i][j]
    print(f"Element at ({i}, {j}) is {element}")
else:
    print("Indices are out of bounds.")


### put this at end 
## dictionary
# You can create a dictionary by enclosing a comma-separated list of key-value pairs within curly braces {}.
#  Each key is unique and maps to a corresponding value. Keys and values can be of various data types.  
# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# You can access values in a dictionary by specifying the key in square brackets [] or by using the get() method.
# Accessing values
name = my_dict["name"]  # Using square brackets
age = my_dict.get("age")  # Using get() method

#You can change the value associated with a specific key in a dictionary.
# Modifying values
my_dict["age"] = 31  # Update age to 31

# You can add new key-value pairs to a dictionary.
# Adding items
my_dict["gender"] = "Male"

# You can remove key-value pairs from a dictionary using the del statement or the pop() method.
# Removing items
del my_dict["city"]  # Remove the "city" key
gender = my_dict.pop("gender")  # Remove and retrieve the "gender" key

# You can iterate through the keys or values, or both, in a dictionary.
# Iterating through keys
for key in my_dict:
    print(key)

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)

# You can check if a key exists in a dictionary using the in operator.
if "name" in my_dict:
    print("Name key exists")

## serching dictionays 
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Check if a key exists in the dictionary
key_to_find = "age"
if key_to_find in my_dict:
    print(f"{key_to_find} found. Value: {my_dict[key_to_find]}")
else:
    print(f"{key_to_find} not found in the dictionary.")

#method 2
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Use the get() method to access a key's value
key_to_find = "age"
value = my_dict.get(key_to_find)

if value is not None:
    print(f"{key_to_find} found. Value: {value}")
else:
    print(f"{key_to_find} not found in the dictionary.")




