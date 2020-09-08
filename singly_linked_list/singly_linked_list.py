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
