class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]

        p.isWord = True


    def search(self, word: str) -> bool:
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]

        return p.isWord == True
        
    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for c in prefix:
            if c not in p.children:
                return False
            p = p.children[c]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)