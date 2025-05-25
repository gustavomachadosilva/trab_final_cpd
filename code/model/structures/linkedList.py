from node import *

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        newNode = Node()
        current = self.head

        if (current is None):
            self.head = newNode
        else:
            while (current.next is not None):
                current = current.next
            
            current.next = newNode
