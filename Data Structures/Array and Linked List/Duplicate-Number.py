#!/usr/bin/env python
# coding: utf-8

# ### Problem Statement
# 
# You have been given an array of `length = n`. The array contains integers from `0` to `n - 2`. Each number in the array is present exactly once except for one number which is present twice. Find and return this duplicate number present in the array
# 
# **Example:**
# * `arr = [0, 2, 3, 1, 4, 5, 3]`
# * `output = 3` (because `3` is present twice)
# 
# The expected time complexity for this problem is `O(n)` and the expected space-complexity is `O(1)`.

# In[2]:


def duplicate_number(arr):
    
    return sum(arr) - (((len(arr)-2)*(len(arr)-1))/2)


# <span class="graffiti-highlight graffiti-id_t54gljc-id_6q2yj6n"><i></i><button>Show Solution</button></span>

# In[3]:


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# In[4]:


arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)


# In[5]:


arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3

test_case = [arr, solution]
test_function(test_case)


# In[6]:


arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)


# In[7]:


arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5

test_case = [arr, solution]
test_function(test_case)


# In[ ]:




