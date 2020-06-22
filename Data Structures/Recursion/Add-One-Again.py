#!/usr/bin/env python
# coding: utf-8

# 
# *Let us solve a problem that we solved previously in the last lesson without using recursion. It will make you realize that recursion can make our code look simpler.*
# 
# ### Problem Statement
# You are given a non-negative number in the form of list elements. For example, the number `123` would be provided as `arr = [1, 2, 3]`. Add one to the number and return the output in the form of a new list. 
# 
# **Example 1:**
# * `input = [1, 2, 3]`
# * `output = [1, 2, 4]`
# 
# **Example 2:**
# * `input = [1, 2, 9]`
# * `output = [1, 3, 0]`
# 
# **Example 3:**
# * `input = [9, 9, 9]`
# * `output = [1, 0, 0, 0]`
# 
# ### Exercise - Write the RECURSIVE function definition here

# In[ ]:


def add_one(arr):
    if arr[0]==9:
        return [1,0]
    elif(arr[-1] < 9):
        arr[-1]+=1
    else:
         arr = add_one(arr[:-1]) + [0]

    return arr


# <span class="graffiti-highlight graffiti-id_isswxel-id_r39lv1k"><i></i><button>Show Solution</button></span>

# ### Test - Let's test your function

# In[ ]:


# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")      


# In[ ]:


# Recursive Solution
def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    # Base case 
    if arr == [9]:
        return [1, 0]
    
    # A simple case, where we just need to increment the last digit
    if arr[-1] < 9:
        arr[-1] += 1

    # Case when the last digit is 9.
    else:
        '''Recursive call'''
        # We have used arr[:-1], that means all elements of the list except the last one.
        # Example, for original input arr=[1,2,9], we will pass [1,2] in next call.
        arr = add_one(arr[:-1]) + [0]
        
    return arr


# In[ ]:


# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)


# In[ ]:


# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)


# In[ ]:


# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)

