#!/usr/bin/env python
# coding: utf-8

# # Python Assignment - 1
# #### Carries 30 marks

# ### Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

# In[6]:


def sum_of_three(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c


# In[8]:


print(sum_of_three(5, 5, 6))


# ### Write a Python program to test whether a passed letter is a vowel or not.

# In[11]:


def check_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter.lower() in vowels:
        return True
    else:
        return False


# In[12]:


print(check_vowel('a'))


# ### Write python program that swap two number with temp variable and without temp variable.

# In[14]:


def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b


# In[13]:


def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


# In[16]:


num1 = 5
num2 = 10

print("Before swapping: num1 =", num1, ", num2 =", num2)

num1, num2 = swap_with_temp(num1, num2)
print("After swapping with temp variable: num1 =", num1, ", num2 =", num2)

num1, num2 = swap_without_temp(num1, num2)
print("After swapping without temp variable: num1 =", num1, ", num2 =", num2)


# ### Write a Python program to calculate the length of a string.

# In[17]:


OP = ("coffe","mixer","griender")
len(OP)


# ### Write a Python program to find whether a given number is even or odd,print out an appropriate message to the user.

# In[18]:


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
result = check_even_odd(number)

if result == "Even":
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


# ### write a programme to find biggest number of given three values.

# In[19]:


def find_biggest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

biggest = find_biggest(a, b, c)
print(f"The biggest number of {a}, {b}, and {c} is {biggest}.")


# ### Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

# In[21]:


def check_values(a, b):
    if a == b:
        return True
    if a + b == 5:
        return True
    if abs(a - b) == 5:
        return True
    return False

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = check_values(a, b)
print(f"The result is {result}.")


# ### Write a python program to sum of the first n positive integers.

# In[22]:


def sum_of_n_positive_integers(n):
    return n * (n + 1) // 2

n = int(input("Enter a positive integer: "))
result = sum_of_n_positive_integers(n)
print(f"The sum of the first {n} positive integers is {result}.")


# ### Write a Python program to calculate the length of a string.

# In[23]:


OP = ("coffe","mixer","griender")
len(OP)


# ### What is the purpose continue statement in python?

# The purpose of the `continue` statement in Python is to skip the rest of the code inside the loop for the current iteration only. It does not stop the entire loop, but continues with the next iteration of the loop.

# ### Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

# In[29]:


def add_suffix(word):
    if len(word) < 3:
        return word
    elif word.endswith('ing'):
        return word + 'ly'
    else:
        return word + 'ing'


# In[30]:


print(add_suffix('run'))
print(add_suffix('swim'))
print(add_suffix('jump')) 
print(add_suffix('eat')) 
print(add_suffix('go')) 
print(add_suffix('fly'))
print(add_suffix('work'))
print(add_suffix(''))
print(add_suffix('a'))
print(add_suffix('ab'))


# ### Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

# In[31]:


def find_and_replace(s):
    not_index = s.find('not')
    poor_index = s.find('poor')

    if not_index == -1 or poor_index == -1 or not_index > poor_index:
        return s

    good_substring = s[poor_index:poor_index+4]
    s = s.replace(good_substring, 'good')

    return s


# In[32]:


print(find_and_replace('The poor knight was not able to finish the quest.'))
print(find_and_replace('The poor knight was able to finish the quest.'))
print(find_and_replace('The knight was not able to finish the quest.'))
print(find_and_replace(''))
print(find_and_replace('a'))
print(find_and_replace('ab'))


# ### Write a Python function to insert a string in the middle of a string.

# In[33]:


def insert_string(original_string, string_to_insert, position):
    """
    This function inserts a string in the middle of a string.

    :param original_string: The original string.
    :param string_to_insert: The string to insert.
    :param position: The position where the string will be inserted.
    :return: The resulting string.
    """
    return original_string[:position] + string_to_insert + original_string[position:]


# In[34]:


print(insert_string('Hello, World!', 'beautiful ', 7))


# ### reverses a string if its length is a multiple of 4.

# In[51]:


def reverse_string(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s


# In[54]:


UO = ("working","youtube","facebook","instagram","whatsapp")
reverse_string(UO)


# ### Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

# In[56]:


def get_string(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]


# In[58]:


print(get_string('Python is fun!'))


# ### Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

# In[63]:


def swap_first_two_characters(str1, str2):
    swapped_str1 = str2[:2] + str1[2:]
    swapped_str2 = str1[:2] + str2[2:]
    return swapped_str1 + " " + swapped_str2


# In[65]:


print(swap_first_two_characters("Hello", "World"))
print(swap_first_two_characters("Python", "Programming"))
print(swap_first_two_characters("123456", "789012"))


# ### Write a Python program to get the Fibonacci series of given range.

# In[66]:


def fibonacci_series(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

def get_fibonacci_range(start, end):
    fib_series = fibonacci_series(end)
    return fib_series[start:end]


# In[67]:


print(get_fibonacci_range(5, 10))


# ### Write a Python program to get the Factorial number of given number

# In[68]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# In[70]:


print(factorial(5))


# ### Write a Python program to check if a number is positive, negative or zero

# In[71]:


def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


# In[72]:


print(check_number(5))


# ##  How memory is managed in Python?
# 

# In Python, memory management is handled by the Python Memory Manager (PMM). The PMM is responsible for allocating and deallocating memory for Python objects.
# 
# When a Python program is executed, the PMM allocates a block of memory for each object that is created. This memory block is used to store the object's data and attributes.
# 
# When an object is no longer needed, the PMM deallocates the memory block associated with that object. This process is known as garbage collection.
# 
# Python uses a reference counting system to track the number of references to an object. When the reference count of an object drops to zero, the object is considered "garbage" and is deallocated.
# 
# However, Python's reference counting system is not perfect. It does not handle circular references, where two or more objects reference each other, creating a cycle of references that cannot be broken.
# 
# To address this issue, Python uses a cyclic garbage collector (GC). The GC periodically scans the memory and identifies objects that are part of a circular reference. It then deallocates these objects and breaks the cycle of references.
# 
# In summary, Python's memory management system involves allocating and deallocating memory for objects, using a reference counting system to track object references, and employing a cyclic garbage collector to handle circular references.

# In[ ]:




