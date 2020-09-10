"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # wrap the input value in a nodex
        new_node = ListNode(value)
        if self.head is None:  # list is empty
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:  # list is non-empty
            self.head.prev = new_node
            self.length += 1
            new_node.next = self.head
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None
        elif self.head is self.tail:  # list has single element
            rv = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return rv
        else:
            value = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.length += 1
            self.tail = new_node
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None
        elif self.head is self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
            return value
        else:
            value = self.tail.value
            self.tail = self.tail.prev
            self.length -= 1
            self.tail.next = None
            return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        b = node
        a = b.prev
        c = b.next
        if a:  # if a is None
            a.next = c
        if c:  # if c is None
            c.prev = a
        self.length -= 1
        if self.head == b:
            self.head = c
        if self.tail == b:
            self.tail = a
        b.next = None
        b.prev = None
        return b

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

    def __str__(self):
        rv = ''
        current = self.head
        while current:
            rv += str(current.value)
            if current.next:
                rv += '<-->'
            current = current.next
        return rv


# myDll = DoublyLinkedList()
# myDll.add_to_head(4)
# myDll.add_to_head(8)
# myDll.add_to_head(12)
# myDll.add_to_head(16)
# print('len: ', len(myDll))
# myDll.add_to_tail(12)
# myDll.add_to_tail(15)
# myDll.add_to_tail(18)
# myDll.add_to_tail(21)
# print('len: ', len(myDll))
# myDll.remove_from_head()
# print('len: ', len(myDll))
# myDll.remove_from_tail()
# print('len: ', len(myDll))
# print('max: ', myDll.get_max())
# print('data: ', myDll)