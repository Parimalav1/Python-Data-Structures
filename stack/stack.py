"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             rv = self.storage.pop()
#             return rv
#         else:
#             None    
    
#     def __str__(self):
#         return f'Data in the stack: {self.storage}'


# myStack = Stack()
# print(myStack)
# print(len(myStack))
# myStack.push(3)
# myStack.push(6)
# myStack.push(9)
# print(myStack)
# print(len(myStack))
# myStack.pop()
# print(len(myStack))
# print(myStack)

from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size
        # return len(self.storage)

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        self.storage.remove_tail()


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        present = self.head
        count = 0
        while present:
            count += 1
            present = present['next']

        return count

    def push(self, value):
        current = {
            'value': value,
            'next': None
        }
        if self.head is None:
            self.head = current
            self.tail = current
        else:
            self.tail['next'] = current
            self.tail = current

    def pop(self):
        if len(self) == 0:
            rv = None
        elif len(self) == 1:
            rv = self.tail['value']
            self.head = None
            self.tail = None
        else:
            rv = self.tail['value']
            previous = None
            curr = self.head
            while curr != self.tail:
                previous = curr
                curr = curr['next']
            self.tail = previous
            previous['next'] = None

        return rv

    def __str__(self):
        curr = self.head
        rv = ''
        while curr:
            rv += str(curr['value'])
            curr = curr['next']

        return rv
