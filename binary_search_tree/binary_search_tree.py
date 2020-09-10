"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.left = left
        self.right = right

    def __add_left__(self, value):
        self.left = BSTNode(value)

    def __add_right__(self, value):
        self.right = BSTNode(value)

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value and self.right is None:
            self.__add_right__(value)
        elif value <= self.value and self.left is None:
            self.__add_left__(value)
        elif value >= self.value and self.right is not None:
            self.right.insert(value)
        else:
            self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            print(f'Node: {target}')
            return True
        elif target > self.value:
            return self.right.contains(target)
        else:
            return self.left.contains(target)
        
    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        current = self.right
        while current:
            max_value = current.value
            current = current.right

        return max_value

    def get_min(self):
        min_value = self.value
        current = self.left
        while current:
            min_value = current.value
            current = current.left

        return min_value

    def get_min2(self):
        if not self:
            return None

        while self.left:
            self = self.left

        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    def pre_order_print(self):
        if self.value:
            print(self.value)
        if self.left:
            self.left.pre_order_print()
        if self.right:
            self.right.pre_order_print()

    def post_order_print(self):
        if self.left:
            self.left.post_order_print()
        if self.right:
            self.right.post_order_print()
        print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        bst_list = []
        bst_list.append(self)
        i = 0
        while i < len(bst_list):
            node = bst_list[i]
            if node.left:
                bst_list.append(node.left)
            if node.right:
                bst_list.append(node.right)
            i += 1
        for node in bst_list:
            print(node.value)



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        dft_stack = []
        dft_stack.append(self)  # append the root
        visited = {}
        while len(dft_stack) > 0:
            node = dft_stack[-1]
            if str(node.value) not in visited:
                print(node.value)
                visited[str(node.value)] = True
            if node.left and str(node.left.value) not in visited:
                dft_stack.append(node.left)
            elif node.right and str(node.right.value) not in visited:
                dft_stack.append(node.right)
            else:
                dft_stack.pop()



    # Stretch Goals -------------------------
    # Note: Research may be required
    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        if self.value:
            print(self.value)
        if self.left:
            self.left.pre_order_print()
        if self.right:
            self.right.pre_order_print()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_print()
        if self.right:
            self.right.post_order_print()
        print(self.value)


    def in_order_dft(self):
        if self.left:
            self.left.in_order_dft()
        print(self.value)
        if self.right:
            self.right.in_order_dft()

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
bst.dft_print()
print('----------')
bst.pre_order_print()
print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
print("bft")
bst.bft_print()