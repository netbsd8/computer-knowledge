class Word:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Word()
        
    def addWord(self, word: str) -> None:
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = Word()
            p = p.children[c]
        p.isWord = True

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)

    def dfs(self, word, root):
        if len(word) == 0:
            return True
        if len(word) == 1:
            if word[0] in root.children:
                return root.children[word[0]].isWord == True
            if word[0] not in root.children:
                if word[0] != '.':
                    return False
                else:
                    for c in root.children:
                        if root.children[c].isWord:
                            return True
                    return False
            

        if word[0] != '.':
            return word[0] in root.children and self.dfs(word[1:], root.children[word[0]])
        else:
            for c in root.children:
                if self.dfs(word[1:], root.children[c]):
                    return True
            return False
                
                    
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)