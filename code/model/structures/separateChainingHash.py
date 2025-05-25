from .linkedList import *

class SeparateChainingHash:

    def __init__(self, numValues):
        self.hashTableSize = int(numValues / 5)
        self.linkedLists: list[LinkedList] = [None] * self.hashTableSize
    
    def insertValue(self, value):
        keyHashCode = self.keyToHashCode(value.id)

        if (self.linkedLists[keyHashCode] is None):
            self.linkedLists[keyHashCode] = LinkedList()
        
        self.linkedLists[keyHashCode].append(value)

    def findById(self, id):
        keyHashCode = self.keyToHashCode(id)

        if (self.linkedLists[keyHashCode] is None):
            return None
        
        return self.linkedLists[keyHashCode].searchById(id)


    def keyToHashCode(self, key) -> int:
        return (key % self.hashTableSize)