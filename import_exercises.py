#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Exercises
# You will need to use imports to complete each exercise; 
# in addition, these exercise will strengthen your problem solving and python coding skills.

# You will be directed to create specific files in part 1, 
#for the rest you may do your work in either import_exercises.py or import_exercises.ipynb.


# In[2]:


# 1. Import and test 3 of the functions from your functions exercise file. 
# Import each function in a different way:

# a. Run an interactive python session and import the module. 
# Call the is_vowel function using the . syntax.
import function_exercises
function_exercises.is_vowel('a')


# In[3]:



# b. Create a file named import_exercises.py. 
# Within this file, use from to import the calculate_tip function directly. 
# Call this function with values you choose and print the result.
function_exercises.calculate_tip(.2, 100)


# In[4]:



# c. Create a jupyter notebook named import_exercises.ipynb. 
# Use from to import the get_letter_grade function and give it an alias. 
# Test this function in your notebook.
from function_exercises import get_letter_grade as glg


# In[5]:


glg(99)


# In[6]:


# Make sure your code that tests the function imports is run from the same directory 
# that your functions exercise file is in.


# In[7]:


# 2. Read about and use the itertools module from the python standard library 
# to help you solve the following problems:



# In[8]:


# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools
print(list(itertools.product('abc', '123', repeat=1)))


# In[9]:


# How many different combinations are there of 2 letters from "abcd"?
print(list(itertools.combinations('abcd', 2)))
# 6


# In[10]:


# How many different permutations are there of 2 letters from "abcd"?
print(list(itertools.permutations('abcd', 2)))


# In[11]:


# 3. Use the load function from the json module to open this file.
import json
profiles = json.load(open('profiles.json'))


# In[12]:


# Total number of users
type(profiles)
user_count = 0
for profile in profiles:
    user_count += 1
user_count
    


# In[13]:


# Number of active users
active_count = 0
for profile in profiles:
    if profile['isActive'] == True:
        active_count += 1
active_count


# In[15]:


# Number of inactive users
inactive_count = user_count - active_count
inactive_count


# In[23]:


# Grand total of balances for all users
total_balance = 0
list_of_balances = []
for profile in profiles:
    balance = profile['balance'] # selects value for key:'balance'
    balance = function_exercises.handle_commas(balance) # calls function to remove commas from 'balance' value
    balance = balance.replace('$', '') # Replaces '$' with an empty space ''.
    balance = float(balance)
    list_of_balances.append(balance)
    total_balance += balance

print(total_balance)




# In[19]:


# Average balance per user
avg_balance = total_balance / user_count
round(avg_balance, 2)


# In[30]:


# User with the lowest balance
def string_to_int(b):
    b = function_exercises.handle_commas(b) # calls function to remove commas from 'balance' value
    b = b.replace('$', '') # Replaces '$' with an empty space ''.
    b = float(b)
    return b
    
    
min_balance = 3000
for profile in profiles:
    balance = string_to_int(profile['balance'])
    if balance < min_balance:
        min_balance = balance
        name = profile['name']
        index = profile['index']
print(f"User = {name}, Index = {index}, Balance = {min_balance}")

        


# In[28]:


# testing function

def string_to_int(b):
    b = function_exercises.handle_commas(b) # calls function to remove commas from 'balance' value
    b = b.replace('$', '') # Replaces '$' with an empty space ''.
    b = float(b)
    return b

type(string_to_int('$10,000.01'))


# In[31]:


# User with the highest balance
max_balance = 0
for profile in profiles:
    balance = string_to_int(profile['balance'])
    if balance > max_balance:
        max_balance = balance
        name = profile['name']
        index = profile['index']
print(f"User = {name}, Index = {index}, Balance = {max_balance}")

# Most common favorite fruit
# Least most common favorite fruit
# Total number of unread messages for all users


# In[33]:


# Most common favorite fruit
list_of_all_fruits = []
for profile in profiles:
    list_of_all_fruits.append(profile['favoriteFruit'])
    
list_of_all_fruits

def most_frequent(l):
    counter = 0
    list_item = l[0]
      
    for i in l:
        curr_frequency = l.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            list_item = i
  
    return list_item


most_frequent(list_of_all_fruits)


# In[36]:


# Least most common favorite fruit
def least_frequent(l):
    counter = 10
    list_item = l[0]
      
    for i in l:
        curr_frequency = l.count(i)
        if(curr_frequency < counter):
            counter = curr_frequency
            list_item = i
  
    return list_item, counter
least_frequent(list_of_all_fruits)


# In[59]:


# Total number of unread messages for all users
total_messages = 0

def string_to_num(string):
    numbers_list = [int(word) for word in string.split() if word.isdigit()]
    number = numbers_list[0]
    return number

type(string_to_num(profiles[1]['greeting'])) #testing function

for profile in profiles:
    total_messages += string_to_num(profile['greeting'])
    
total_messages


# In[ ]:




