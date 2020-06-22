#!/usr/bin/env python
# coding: utf-8

# # Reversed Queue
# Write a function that takes a queue as an input and returns a reversed version of it. 

# In[1]:


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


        
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def front(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


# In[6]:


def reverse_queue(queue):
    """
    Reverese the input queue

    Args:
       queue(queue),str2(string): Queue to be reversed
    Returns:
       queue: Reveresed queue
    """
    
    # TODO: Write reversed queue function
    temp1 = None
    temp2 = None
    temp = queue.head
    while(temp):
        temp2 = temp1
        temp1 = temp
        temp = temp.next
        temp1.next = temp2
    queue.head = temp1
    return queue


# In[7]:


def test_function(test_case):
    queue = Queue()
    for num in test_case:
        queue.enqueue(num)
    
    reverse_queue(queue)
    index = len(test_case) - 1
    while not queue.is_empty():
        removed = queue.dequeue()
        if removed != test_case[index]:
            print("Fail")
            return
        else:
            index -= 1
    print("Pass")
    


# In[8]:


test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)


# In[9]:


test_case_2 = [1]
test_function(test_case_2)


# <span class="graffiti-highlight graffiti-id_8lnr8ur-id_7ltw82e"><i></i><button>Show Solution</button></span>
