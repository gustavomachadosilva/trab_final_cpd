from .node import *

class LinkedList:

    def __init__(self):
        self.head: Node = None

    def append(self, value):
        newNode = Node(value)
        current = self.head

        if (current is None):
            self.head = newNode
        else:
            while (current.next is not None):
                current = current.next
            
            current.next = newNode
    
    def searchById(self, id):
        current = self.head
        currentId = -1

        while (currentId != id and current != None):
            currentId = current.value.id

            if (currentId != id):
                current = current.next
        
        if (currentId != id or current == -1):
            return None
        
        return current.value

