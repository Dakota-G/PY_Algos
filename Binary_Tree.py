# Given the root node of a binary tree, write a function that prints out the tree’s content with a breadth first traversal without using recursion.
# You have to define the tree yourself.
# Any additional data structure you need, you will need to create/define as well.

# Node class that will contain its value as well as binary directional attributes
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  
        self.right = None

# Perhaps unnecessary, because essentially any collection of nodes is a tree, but this could be useful for organizing those nodes into specific trees, defined by the root node
class Tree:
    def __init__(self, node):
        self.root = node

# The Queue class instantiates itself as an empty list. Because nodes in a binary tree are connected top-down and not laterally, using a queue is a good method for creating
# 'anchors' for traversal to sibling nodes. Enqueue will add an item to the 0 index (head) of the queue, while dequeue uses the pop method to return the last item.
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

# The fetch_content function will take the root of a binary tree and perform a breadth-first traversal
# It starts by placing the root into the queue and, while the queue has something in it, the function dequeues, 
# prints what was just been dequeued, and then uses it as an anchor to access and add the children to the queue.
# As long as there are children nodes to add to the queue, the while-loop will continue, until reaching the end of the tree.
def fetch_content(root):
    if root == None:
        return None
    New_Q = Queue()
    New_Q.enqueue(root)
    while len(New_Q.items) > 0:
        select = New_Q.dequeue()
        print(select.value)
        if select.left != None:
            New_Q.enqueue(select.left)
        if select.right != None:
            New_Q.enqueue(select.right)

# Create an inverted tree by swapping the right side with the left side. It's important to make the recursive
# calls before making the switch, so the function is swapping sides as it goes up the call stack, ensuring
# that no parts of the tree get scrambled.
def invert(node):  
    if (node == None): 
        return
    else: 
        temp = node  
        # recursive calls
        invert(node.left)  
        invert(node.right)  
        # swap the pointers in this node
        temp = node.left  
        node.left = node.right  
        node.right = temp  