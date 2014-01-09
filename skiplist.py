
##
#  Example of Skip List source code for c
##
minint=0
class Node(object):
    def __init__(self,key=minint,value=None):
        self.key = key
        self.value = value
        self.right = None
        self.down = None
    def __del__(self):
        self.value = None

class SkipList(object):
    def __init__(self):
        pass
