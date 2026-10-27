class Node:

    def __init__(self, val=None):
        self.val = val
        self.children = dict()
    
    def addChild(self, val):
        newNode = Node(val)
        self.children[val] = newNode
        return newNode
    
    def getChild(self, val):
        return self.children.get(val, None)

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        n = len(word)
        i = 0
        curr = self.root
        while i < n:
            nextNode = curr.getChild(word[i])
            if nextNode:
                curr = nextNode
            else:
                curr = curr.addChild(word[i])
            i+=1
        curr.addChild("")
                

    def search(self, word: str) -> bool:
        n = len(word)
        i = 0
        curr = self.root
        while curr and i < n:
            curr = curr.getChild(word[i])
            i+=1
        if curr:
            return curr.getChild("") is not None
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        i = 0
        curr = self.root
        while curr and i < n:
            curr = curr.getChild(prefix[i])
            i+=1
        if not curr:
            return False
        else:
            return i == n
        