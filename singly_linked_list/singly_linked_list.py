class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        return count

    def add_to_tail(self, value):
        current = Node(value)
        if self.head is None:
            self.head = current
            self.tail = current
        else:
            self.tail.next = current
            self.tail = current

    def remove_head(self):
        if len(self) == 0:
            rv = None
        elif len(self) == 1:
            rv = self.head.value
            self.head = None
            self.tail = None
        else:
            rv = self.head.value
            self.head = self.head.next

        return rv

    def remove_tail(self):
        if len(self) == 0:
            rv = None
        elif len(self) == 1:
            rv = self.head.value
            self.head = None
            self.tail = None
        else:
            rv = self.tail.value
            previous = None
            curr = self.head
            while curr != self.tail:
                previous = curr
                curr = curr.next
            self.tail = previous
            previous.next = None

        return rv

# 👍 ANSWER 2


class Node2:
    def __init__(self, value=None, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    def get_value(self):
        return self.value

    def get_next(self):
        return self.nextNode

    def set_next(self, newNext):
        self.nextNode = newNext


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the input value in a nodex
        new_node = Node(value, None)
        if self.head is None:  # list is empty
            self.head = new_node
            self.tail = new_node
        else:  # list is non-empty
            self.tail.set_next = new_node  # reference/pointer
            self.tail = new_node

    def remove_head(self):
        if not self.head:  # list is empty
            return None
        elif not self.head.get_next():  # list has single element
            head = self.head  # reference to the head
            self.head = None  # delete the reference
            self.tail = None  # tail isn't referring to anything
            return head.get_value()
        else:  # list has > 1 element
            value = self.head.get_value()
            self.head = self.head.get_next()  # head reference to current head's next node in the list
            return value

    def remove_tail(self):
        if not self.head:  # list has 0 elements or empty
            return None

        if self.head is self.tail:  # list has 1 element
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head

        while current.get_next() is not self.tail:  # list has more elems
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value


    def contains(self, value):
        if not self.head:
            return False

        # Recursive solution
        def search(node):
            if node.get_value() == value:
                return True
            if not node.get_next():
                return False
            return search(node.get_next())
        return search(self.head)

        # current node reference
        current = self.head
        while current:  # if current is valid or true
            if current.get_value() == value:  # current value matches target value
                return True
            current = current.get_next()  # update current node to next node in the list
        # target node isn't in the list
        return False

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()
        current = self.head.get_next()  # current node
        while current: # valid list node 
            if current.get_value > max_value:
                max_value = current.get_value()
                # update current node to next node in the list
                current = current.get_next()
        return max_value
