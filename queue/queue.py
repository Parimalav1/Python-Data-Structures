"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) > 0:
#             rv = self.storage[0]
#             del self.storage[0]
#             return rv
#         else:
#             return None

#     def __str__(self):
#         return f'Data in the queue: {self.storage}'
# myQ = Queue()
# print(myQ)
# print(len(myQ))
# myQ.enqueue(5)
# myQ.enqueue(11)
# myQ.enqueue(16)
# print(len(myQ))
# myQ.dequeue()
# print(len(myQ))
# print(myQ)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr['next']
        
        return count

    def enqueue(self, value):
        current = {
            'value': value,
            'next': None
        }
        if self.head == None:
            self.head = current
            self.tail = current
        else:
            self.tail['next'] = current
            self.tail = current

    def dequeue(self):
        if len(self) == 0:
            rv = None
        elif len(self) == 1:
            rv = self.head['value']
            self.head = None
            # self.head = self.head['next']
            self.tail = None
            #  self.tail = self.head
        else:
            rv = self.head['value']
            self.head = self.head['next']

        return rv

    def __str__(self):
        curr = self.head
        rv = ''
        while curr:
            rv += str(curr['value'])
            curr = curr['next']

        return rv
