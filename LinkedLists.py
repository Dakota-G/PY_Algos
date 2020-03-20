import random

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List():
    def __init__(self):
        self.head = None 

    def add_to_end(self, value):
        new_node = Node(value)
        pointer = self.head
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = new_node

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def reverse_list(self):
        prev = None
        current = self.head
        while current != None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev
    
    def count_nodes(self):
        counter = 0
        if self.head != None:
            pointer = self.head
            counter = 1
            while pointer.next != None:
                pointer = pointer.next
                counter += 1
        return counter

    def remove_from_end(self):
        if self.head != None:
            pointer = self.head
            while pointer.next.next != None:
                pointer = pointer.next
            pointer.next = None
        else:
            print("Error. List is empty.")

    def remove_from_front(self):
        if self.head != None:
            self.head = self.head.next
        else:
            print("Error. List is empty.")


# function to make a deep copy of a LL with .random by taking and returning only the head node
# Assume Nodes have extra attribute called .random, which points to a random node in the LL
class randoNode(Node):
    def __init__(self, value):
        Node.__init__(self, value)
        self.random = None

class RandoLL(Linked_List):
    def random_node(self):
        import random
        end = self.count_nodes()
        counter = random.randint(0, end)
        pointer = self.head
        while counter != 0:
            pointer = pointer.next
            counter -= 1
        return pointer

def deep_copy_RandoLL(headnode):
    new_head = randoNode(headnode.value)
    pointer1 = headnode
    pointer2 = new_head
    while pointer1 != None:
        pointer1 = pointer1.next
        pointer2.next = randoNode(pointer1.value)
        pointer2 = pointer2.next
    pointer1 = headnode
    pointer2 = new_head
    while pointer1 != None:
        pointer2.random = pointer1.random
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return new_head