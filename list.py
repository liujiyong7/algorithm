
##
#  Example of Skip List source code for c
##
class Node(object):
    def __init__(self, key, value=None, nextnode=None):
        self.key= key
        self.value = value
        self.nextnode = nextnode
    def setNext(self, next=None):
        self.value = next

class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.nextnode=None
        pass

    def insertNode(self, node):
        node.nextnode = self.nextnode
        self.nextnode = node
        self.length = self.length + 1
        pass
    def listAll(self):
        node = self.nextnode
        while node:
            print node.value
            node = node.nextnode
        pass

linklist = LinkedList()

linklist.insertNode(Node(1,3))
linklist.insertNode(Node(3,5))
linklist.insertNode(Node(6,8))

linklist.listAll()

