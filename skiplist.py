
##
#  Example of Skip List source code for c
##
import random
import sys

minint=0
maxint=65535
class Node(object):
    def __init__(self,key=minint, value=None, level=1):
        self.key = key
        self.value = value
        self.level = 1
        self.right = None
        self.down = None

class SkipList(object):
    def __init__(self):
        self.top = Node(minint)
        self.top.right = Node(maxint)
        self.nodenum = 0
        pass

    def getNode(self, key):
        node = self.top
        while 1:
            while key >= node.right.key :
                node = node.right
            if( key == node.key):
                return node
            if node.down == None:
                return None
            node = node.down
    def findNode(self, key):
        return searchNode(self.top,key)

    def searchNode(node, key):
        while key >= node.right.key:
            node = node.right
        if key == node.key:
            return node
        if node.down == None:
            return None
        return searchNode(node.down, key)


    def insertNode(top, key, value):
        while key >= top.right.key:
            top = top.right
        if key == top.key:
            return None
        if top.down == None:
        	node = Node(key, value)
        	node.right = top.right
        	top.right = node
            return node
        downnode = searchNode(top.down, key, value)
        if downnode:
            node = Node(key, value)
            node.right = top.right
            top.right = node
            node.down = downnode
            return node
        return None





