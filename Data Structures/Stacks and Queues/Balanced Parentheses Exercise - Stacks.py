#!/usr/bin/env python
# coding: utf-8

# # Balanced Parentheses Exercise

# In this exercise you are going to apply what you learned about stacks with a real world problem. We will be using stacks to make sure the parentheses are balanced in mathematical expressions such as: $((3^2 + 8)*(5/2))/(2+6).$ In real life you can see this extend to many things such as text editor plugins and interactive development environments for all sorts of bracket completion checks. 
# 
# Take a string as an input and return `True` if it's parentheses are balanced or `False` if it is not. 
# 
# Try to code up a solution and pass the test cases. 

# #### Code

# In[5]:


# Our Stack Class - Brought from previous concept
# No need to modify this
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()
    
    def is_empty(self):
        return self.size() == 0

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    
    # TODO: Intiate stack object
    Mystack = Stack()
    
    # TODO: Interate through equation checking parentheses
    for x in equation:
        if x == '(':
            Mystack.push(x)
        elif x == ')':
            if Mystack.is_empty():
                return False
            Mystack.pop()
    
    # TODO: Return True if balanced and False if not
    if Mystack.is_empty():
        return True
    return False
        
    


# #### Test Cases

# In[6]:


print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")


# <span class="graffiti-highlight graffiti-id_ky3qi6e-id_jfute45"><i></i><button>Show Solution</button></span>

# In[ ]:




