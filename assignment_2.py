#!/usr/bin/env python
# coding: utf-8

# # Python Assignment - 2
# ### Carries - 30 marks

# ## What is List? How will you reverse a list?

# A list in Python is a collection of items that can be of different data types. It is mutable, meaning that we can modify its content. Lists are ordered, which means that the order of elements in the list is preserved.

# In[1]:


my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)


# # How will you compare two lists?

# In[4]:


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
list3 = [5, 4, 3, 2, 1]


# In[5]:


print(list1 == list2)
print(list1 == list3)


# ###  How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 

# In[16]:


list1 = [2, 33, 222, 14, 25]
last_object = list1.pop()
print(last_object)


# ### Differentiate between append () and extend () methods?

# the append() method adds a single element to the end of the list, while the extend() method adds the elements of a given iterable to the end of the list.

# ### Write a Python program to find the second smallest number in a list.

# In[18]:


def second_smallest(numbers):
    return sorted(numbers)[1]


# In[19]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(second_smallest(numbers))


# ### Write a Python program to find the length of a tuple.

# In[20]:


tuple1 = (1, 2, 3, 4, 5)
len(tuple1)


# ## Write a Python program to reverse a tuple.

# In[ ]:


tuple1 = (1, 2, 3, 4, 5)


# In[21]:


reversed_tuple = tuple1[::-1]
print(reversed_tuple)


# ### Write a Python program to remove duplicates from a list.

# In[23]:


def remove_duplicates(list1):
    set1 = set(list1)
    return list(set1)


# In[24]:


list1 = [1, 2, 3, 4, 5, 1, 2, 3]
print(remove_duplicates(list1))


# ## Write a Python function that takes a list and returns a new list with unique elements of the first list.

# In[27]:


def remove_duplicates(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
list1 = [1, 2, 3, 4, 5, 1, 2, 3]
print(remove_duplicates(list1))


# ###  Write a Python program to check a list is empty or not. 

# In[29]:


def is_list_empty(list1):
    if len(list1) == 0:
        return True
    else:
        return False
list1 = input("Enter a list: ")
if is_list_empty(list1):
    print("The list is empty.")
else:
    print("The list is not empty.")


# ### Write a Python function to get the largest number, smallest num and sum of all from a list. 

# In[2]:


def get_largest_smallest_and_sum(list1):
    largest = list1[0]
    smallest = list1[0]
    sum = 0
    for num in list1:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        sum += num
    return largest, smallest, sum


# In[3]:


number = [56,45,67,22,76,8,90]
get_largest_smallest_and_sum(number)


# ### Write a Python program to get unique values from a list

# In[9]:


def get_unique_values(list1):
    unique_values = set(list1)
    unique_values = list(unique_values)
    return unique_values


# In[8]:


list1 = [1, 2, 3, 4, 5, 1, 2, 3]
get_unique_values(list1)


# ### Write a Python program to split a list into different variables.

# In[13]:


list1 = [1, 2, 3]


# In[15]:


a, b, c = list1
print(a)
print(b)
print(c)


# ### Write a Python program to check whether an element exists within a tuple

# In[6]:


my_tuple = tuple(input("Enter a tuple: ").split())
if element in my_tuple:
    print("The element exists in the tuple.")
else:
    print("The element does not exist in the tuple.")


# ### Write a Python program to convert a list to a tuple. 

# In[7]:


list1 = [1, 2, 3, 4, 5]
tuple1 = tuple(list1)
print(tuple1)


# ### Write a Python program to find the repeated items of a tuple.

# In[14]:


def find_repeated_items_using_dictionary(tuple1):
  dict1 = {}
  for element in tuple1:
    if element in dict1:
      dict1[element] += 1
    else:
      dict1[element] = 1
  repeated_items = []
  for key, value in dict1.items():
    if value > 1:
      repeated_items.append(key)

  return repeated_items


# In[15]:


tuple1 = (1, 2, 3, 1, 4, 5, 2)
print(find_repeated_items_using_dictionary(tuple1))


# ###  Write a Python program to remove an empty tuple(s) from a list of tuples

# In[16]:


my_list = [(1,2,3), (), (4,5,6), (), (7,8,9)]
my_list = [t for t in my_list if t]
print(my_list)


# ### Write a Python program to unzip a list of tuples into individual lists. 

# In[18]:


my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
a,b,c = zip(*my_list) 
print(a)
print(b)
print(c)


# ### Write a Python function to check whether a number is in a given range

# In[26]:


def is_in_range(number, start, end):
  if start <= number <= end:
    return True
  else:
    return False


# In[27]:


is_in_range(5, 1, 10)


# ### Write a Python function that checks whether a passed string is palindrome or not 

# In[30]:


def is_palindrome(string):
  string = string.lower().replace(" ", "")
  reversed_string = string[::-1]
  return string == reversed_string


# In[31]:


is_palindrome("racecar")


# ### Write a Python program to returns sum of all divisors of a number 

# In[75]:


def sum_of_divisors(n):
  sum_of_divisors = 1
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      sum_of_divisors += i + n // i

  if int(n**0.5) * int(n**0.5) == n:
    sum_of_divisors -= int(n**0.5)

  return sum_of_divisors


# In[77]:


print(sum_of_divisors(10))
print(sum_of_divisors(12))
print(sum_of_divisors(28))


# ### Write a Python program to find the maximum and minimum numbers from the specified decimal numbers. 

# In[89]:


def find_max_and_min(numbers):
  """
  Finds the maximum and minimum numbers from a list of decimal numbers.
  Args:
    numbers: A list of decimal numbers.
  Returns:
    A tuple containing the maximum and minimum numbers.
  """
  # Initialize the maximum and minimum numbers.
  max_number = numbers[0]
  min_number = numbers[0]
  # Iterate over the remaining numbers.
  for number in numbers[1:]:
    # Update the maximum and minimum numbers if necessary.
    if number > max_number:
      max_number = number
    if number < min_number:
      min_number = number
  # Return the maximum and minimum numbers.
  return (max_number, min_number)


# In[90]:


numbers = [1.2, 3.4, 5.6, 7.8, 9.0]
max_number, min_number = find_max_and_min(numbers)
print(max_number)  
print(min_number)


# ### Write a Python program to calculate the area of a parallelogram 

# In[11]:


def area_of_parallelogram(base, height):
    return base * height


# In[12]:


area_of_parallelogram(45,7)


# ### Write a Python function to check whether a number is perfect or not. 

# In[13]:


def is_perfect_number(n):
  """
  Checks whether a number is perfect or not.
  Args:
    n: The number to check.
  Returns:
    True if the number is perfect, False otherwise.
  """
  if n <= 1:
    return False
  # Find all the factors of n.
  factors = set()
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      factors.add(i)
      factors.add(n // i)
  # Check if the sum of the factors is equal to n.
  return sum(factors) == n


# In[14]:


is_perfect_number(66)


# ### Write a Python program to convert degree to radian

# In[15]:


import math
def degrees_to_radians(degrees):
    return degrees * math.pi / 180
if __name__ == "__main__":
  degrees = float(input("Enter the angle in degrees: "))
  radians = degrees_to_radians(degrees)
  print(f"The angle in radians is {radians}.")


# ###  Write a Python program to calculate the area of a trapezoid 

# In[16]:


def area_of_trapezoid(base1, base2, height):
    return (base1 + base2) * height / 2


# In[17]:


area_of_trapezoid(23,25,8)


# ## Write a Python program to calculate surface volume and area of a cylinder 

# In[19]:


import math
def surface_area_of_cylinder(radius, height):
    return 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
def volume_of_cylinder(radius, height):
    return math.pi * radius ** 2 * height


# In[22]:


radius = 5
height = 10
surface_area = surface_area_of_cylinder(radius, height)
volume = volume_of_cylinder(radius, height)
print(f"The surface area of the cylinder is {surface_area}.")
print(f"The volume of the cylinder is {volume}.")


# In[ ]:




