#!/usr/bin/env python
# coding: utf-8

# # Python Assignment - 3
# ### Carries - 30 marks

# ## What is File function in python? What is keywords to create and write file. 

# The `file` function in Python is used to create and write files. It is a built-in function that takes two arguments: the first is the file name, and the second is the mode in which the file is to be opened.

# #### Create and write a  file

# In[5]:


from io import open
file_object = open('file.txt', 'w')
file_object.write('This is an example of how to use the open function in Python.')
file_object.close()


# ## Write a Python program to read an entire text file. 

# In[6]:


with open('file.txt', 'r') as file:
    content = file.read()
    print(content)


# ## Write a Python program to append text to a file and display the text.

# In[14]:


text = "This is the text to append."
with open('file.txt', 'a') as file:
    file.write(text)
    file.write('\n')
with open('file.txt', 'r') as file:
        content = file.read()
        print(content)


# ## Write a Python program to read first n lines of a file. 

# In[13]:


def read_first_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = []
        for i, line in enumerate(file):
            if i < n:
                lines.append(line.strip())
            else:
                break
        return lines

file_path = 'file.txt'
n = 1
lines = read_first_n_lines(file_path, n)
for line in lines:
    print(line)


# ## Write a Python program to read last n lines of a file. 

# In[16]:


import os
from collections import deque

def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = deque(file, n)
        return list(lines)

# Usage
file_path = 'file.txt'
n = 1
lines = read_last_n_lines(file_path, n)
for line in lines:
    print(line.strip())


# ## Write a Python program to read a file line by line and store it into a list

# In[26]:


def read_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

file_path = 'file.txt'
lines = read_file(file_path)
for line in lines:
    print(line)


# ## Write a Python program to read a file line by line store it into a variable.

# In[23]:


def read_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

file_path = 'file.txt'
lines = read_file(file_path)
for line in lines:
    print(line)


# ## Write a Python program to copy the contents of a file to another file.

# In[1]:


import shutil
def copy_file(src_file_path, dst_file_path):
    shutil.copyfile(src_file_path, dst_file_path)
# Usage
src_file_path = 'file.txt'
dst_file_path = 'example_copy.txt'
copy_file(src_file_path, dst_file_path)


# In[ ]:





# ## Write python program that user to enter only odd numbers, else will raise an exception

# In[28]:


while True:
    try:
        num = int(input("Enter an odd number: "))
        if num % 2 == 0:
            raise ValueError("Please enter an odd number.")
        else:
            print("Valid odd number entered.")
            break
    except ValueError as e:
        print(e)


# ## Can one block of except statements handle multiple exception? 

# Yes, one block of except statements can handle multiple exceptions.

# ## Explain Exception handling? What is an Error in Python?
# 

# Exception handling is a mechanism that allows you to handle errors and exceptions in your Python code. 
# Errors are events that occur during the execution of a program that disrupt the normal flow of the program.

# ## Write a Python program to count the number of lines in a text file. 

# In[15]:


def count_lines(filename):
  try:
    with open(filename) as f:
      lines = f.readlines()
    return len(lines)
  except FileNotFoundError:
    return -1
if __name__ == "__main__":
  filename = input("Enter the name of the text file: ")
  line_count = count_lines(filename)
  if line_count >= 0:
    print(f"The number of lines in {filename} is {line_count}.")
  else:
    print(f"Error: The file {filename} could not be found.")


# ## Write a Python program to write a list to a file. 

# In[36]:


def write_list_to_file(list_name, file_name):
    with open(file_name, "w") as f:
        for item in list_name:
            f.write(str(item) + "\n")


# In[38]:


my_list = [1, 2, 3, 4, 5]
file_name = "file.txt"

write_list_to_file(my_list, file_name)


# # Explain Inheritance in Python with an example?What is init? Or What Is A Constructor In Python? 
# 
# 

# Inheritance is a mechanism in object-oriented programming that allows you to create a new class based on an existing class. 
# This means that the new class will inherit all of the properties and methods of the existing class, and you can add new properties and methods to the new class.
# For example, you could create a class called `Animal` that has properties like `name`, `age`, and `species`. You could then create a new class called `Dog` that inherits from `Animal`. The `Dog` class would have all of the properties and methods of the `Animal` class, plus you could add new properties and methods specific to dogs, such as a method called `bark()`.

# In[40]:


class Animal:
  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species
  def make_sound(self):
    print("The animal makes a sound.")
class Dog(Animal):
  def __init__(self, name, age, species, breed):
    super().__init__(name, age, species)
    self.breed = breed
  def bark(self):
    print("The dog barks.")
my_dog = Dog("Fido", 5, "Golden Retriever", "indian")
my_dog.make_sound()
my_dog.bark()


# # Write a python program to find the longest words.

# In[43]:


def find_longest_words(words_list):
  longest_word_length = max(len(word) for word in words_list)
  longest_words = []
  for word in words_list:
    if len(word) == longest_word_length:
      longest_words.append(word)
  return longest_words
if __name__ == "__main__":
  words_list = ["Hello", "world", "longest", "supercalifragilisticexpialidocious"]
  longest_words = find_longest_words(words_list)
  print(longest_words)


# # How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
# .
# 

# A class in Python is a blueprint for creating objects. It defines the attributes and methods of an object. When you create an object, you can specify the values for the attributes. The methods of an object are functions that can be called on the object.
# The `self` keyword is used to refer to the current object. It is used in methods to access the attributes of the object.

# In[47]:


class Animal:
  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species
  def make_sound(self):
    print("The animal makes a sound.")
my_dog = Animal("Fido", 5, "Golden Retriever")
my_dog.make_sound()


# # Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

# In[54]:


class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def area(self):
    return self.length * self.width


# In[61]:


my_rectangle = Rectangle(5, 10)
print(my_rectangle.area())


# ## Explain Exception handling? What is an Error in Python?

# an exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
# Exceptions are handled by the `try-except` statement. The `try` block contains the code that might raise an exception, and the `except` block contains the code that will be executed if an exception occurs.
# The `except` block can specify the type of exception that it will handle. If the exception that occurs is not of the specified type, the `except` block will be skipped and the next `except` block will be tried.
# If no `except` block matches the exception that occurs, the program will crash.

# An error is a problem that occurs during the execution of a program that prevents the program from continuing. Errors are typically caused by incorrect syntax or logic in the program.

# ## How many except statements can a try-except block have? Name Some built-in exception classes: 

#  A try-except block can have multiple except statements. Each except statement can handle a different type of error. 
#     Some built-in exception classes in Python include:
# * `ArithmeticError`
# * `AssertionError`
# * `AttributeError`
# * `EOFError`
# * `FloatingPointError`
# * `GeneratorExit`

# ## Write python program that user to enter only odd numbers, else will raise an exception. 

# In[63]:


while True:
    try:
        num = int(input("Enter an odd number: "))
        if num % 2 == 0:
            raise ValueError("Please enter an odd number")
    except ValueError:
        print("Invalid input. Please enter an odd number.")
    else:
        break
print("The odd number you entered is:", num)


# ## Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 

# In[70]:


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


# In[71]:


circle = Circle(10)

area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

print("The area of the circle is:", area)
print("The perimeter of the circle is:", perimeter)


# ## Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python? 

# Inheritance is a mechanism in object-oriented programming that allows you to create a new class based on an existing class. This means that the new class will inherit all of the properties and methods of the existing class, and you can add new properties and methods to the new class.

# The `__init__()` method is the constructor for a class. It is called when a new instance of the class is created. The `__init__()` method can take arguments, which are used to initialize the properties of the new instance.

# ## What is Instantiation in terms of OOP terminology?
# 
# 

# Instantiation is the process of creating a new instance of a class. When a class is instantiated, the __init__() method of the class is called. The __init__() method can take arguments, which are used to initialize the attributes of the new instance.
