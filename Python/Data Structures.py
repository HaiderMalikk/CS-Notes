# radome guess
import random as rd

# def game():
#     print(f"helo welcom to gess game pick num 1-10 hehe")
#     num = (input("pick a number from 1-10: ")) # can do num(input)
#     num = int(num)
#     if num >= 1 and num <= 10:
#         rdnum = rd.randint(1, 10)
#         if rdnum == num:
#             print("you win you are the best player everrrr!!!!!")
        
#         else: print(f"you lose the num was: {rdnum}")
#     else:
#         print('please enter a valid number')
#         game()

# game()

# class Student:
#     def __init__(self, name, major, student_num):
#         self.name = name
#         self.major = major
#         self.student_num = student_num
#     def greet(self):
#         return f"hello my name is {self.name} my major is {self.major} my student id is {self.student_num}"
    
# stu1 = Student("john", "english", "23456789")


# list = [stu1.name, stu1.major, stu1.student_num]

# for i in list:
#     print(i)

# greeting = stu1.greet()
# print(greeting)

# class
# class arrays:
#     def array():
#         arr = []
#         n = int(input("how many numbers u want to add? :"))
#         for i in range(n): # for loop runs until n integer starting from 0 if n=2 the for loop runs 2 times
#             # i+1 in {} displayes the number of the number being added so on the second number it will say enter number 2 
#             # but why i+1? becuase i starts at zero like mentioned before there for on the first run the number should be num1 not 0
#             x = input(f"enter a number{i+1}: ")
#             arr.append(int(x))
#         return arr

# # list comprihention
# arr = [[1, 2, 3], [1, 3, 2], [3, 2, 1]]

# # Create a new list to store the modified sublists
# new_arr = []
# count = 0
# # the for value in sublist is the second loop 
# # if value != 3 is our condition 
# # value is just the variable like J
# # value is just a variable name that represents each element in the sublist 
# for sublist in arr:
#     new_sublist = [value for value in sublist if value != 3]
#     new_arr.append(new_sublist)

# print(new_arr)

# linked list 
# class Node: # define node
#     def __init__(self, data): # node constructer 
#         self.data = data # data part of node the acc value
#         self.ref = None # ref value of node empty to start 
#         # value of ref is none as we are just creatinf empty nodes and not linking them yet 

# class LinkedList: # creating linked list to link nodes
#     def __init__(self): 
#         self.head = None 
#         # head is start point of list if this is empty list is empty we canuse this to check if list empty
    
#     def display_LL(self):
#         if self.head is None: # if list is empty
#             print("Linked List is empty")
#         else: # if list not empty
#             n = self.head # assign a var to self to head to make calling it easy
#             # innitally n = the head withc point to the first node
#             while n is not None: # while "head" the pointer that points to the first node is not None
#                 print(n.data) #print heads data, data from node 
#                 n = n.ref # after printing the data of the first head first node n.data n is now equal to the refrance of that node that
#                 # n.ref is the refrance of the next node, stored in the first node
#                 # we just printed the data of, that refrance points to the second node now when the loop runs again
#                 # n.data is the second nodes data as n = n.ref of node 1 and ref of node one points to node 2 
#                 # n.data of (node2) is printed. this prosses reapets untill the head of node points to nothing

# LL1 = LinkedList() # creating empty linked list 
# LL1.display_LL() # callinf method to print list

class node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LL: 
    def __init__(self):
        self.head = None

    def displayLL(self):

        if self.head is None:
            print("Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref # to go to next node, assign head to value of refrence of the current node which points to next node
    # adding to start if linked list
    def add_begin(self, data): # new function for adding only takes in data as parameter
        new_node = node(data) # creating a new node using the class node
        # new node is the first node so its ref is stored in the head
        new_node.ref = self.head # the refrence of first node is now stored in head iniitally head was null
        # ref of first node in stored in head but, when we create that first node its refrence will be stored in its head that will point to the next node
        self.head = new_node # store refrence of first node in its head this refrence points to the next node

myLL = LL()
myLL.add_begin(10) # 10 is val of data
myLL.add_begin(20) # 20 is val of data its added at the start of the linked list
myLL.displayLL()


class node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    def display_LL(self):
        if self.head is None:
            print("enpty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
myLL = LinkedList()
myLL.display_LL()






