class Node:
    def __init__(self, value):
        self.value = value
        self.children = dict()

    def addChild(self, value):
        child = Node(value)
        self.children[value] = child
        return child

class WordDictionary:

    def __init__(self):
        self.root = Node('')

    def addWord(self, word: str) -> None:
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                nextNode = currNode.addChild(char)
            else:
                nextNode = currNode.children[char]
            currNode = nextNode
        currNode.addChild('-')

    def search(self, word):
        return self.searchRecur(word, 0, self.root)

    def searchRecur(self, word: str, i, currNode) -> bool:
        if i == len(word):
            if '-' in currNode.children:
                return True
            return False
        
        char = word[i]
        if char == '.':
            for child in currNode.children:
                result = self.searchRecur(word, i+1, currNode.children[child])
                if result:
                    return True
            return False
        else:
            if char not in currNode.children:
                return False
            return self.searchRecur(word, i+1, currNode.children[char])
