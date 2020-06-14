class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


def prepend(self, value):      
        node = Node(value)
        if not self.head:
            node.next = self.head
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node           
LinkedList.prepend = prepend


def append(self, value):       
    if not self.head:
        self.head = Node(value)
        self.tail = self.head      
    else:
        self.tail.next = Node(value)
        self.tail = self.tail.next
LinkedList.append = append


def search(self, value):
    node = self.head
    while(node):
        if node.value == value:
            return node
        node=node.next    
LinkedList.search = search


def remove(self, value):
    node = self.head
    temp = None
    if self.head.value == value:
        self.head = self.head.next
        return
    while(node):
        if node.value == value:
            if(node.next == None):
                  self.tail = temp
            temp.next = node.next
            break
        temp = node
        node = node.next
LinkedList.remove = remove


def pop(self):
    x = self.head.value
    self.head = self.head.next
    return x
LinkedList.pop = pop


def size(self):
    node = self.head
    count = 0
    while(node):
        count+=1
        node = node.next
    return count
LinkedList.size = size


def insert(self, value, pos):    
    if pos == 0:
        self.prepend(value)
    elif pos >self.size():
        self.append(value)
    else:
        node = self.head
        temp = Node(value)
        for i in range(pos-1):
            node = node.next
        temp.next = node.next
        node.next = temp
LinkedList.insert = insert


linked_list = LinkedList()

# Test append 
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"
