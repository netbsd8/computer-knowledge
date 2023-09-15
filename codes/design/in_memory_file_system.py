import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isFile = False
        self.content = ""
        self.name = ""

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        if path == "/":
            return sorted(self.root.children.keys())

        path_list = path.split("/")
        cur = self.root
        for p in path_list[1:]:
            cur = cur.children[p]

        if cur.isFile:
            return [cur.name]
            
        ret = []
        for dir in cur.children:
            ret.append(dir)
        return sorted(ret)

    def mkdir(self, path: str) -> None:
        cur = self.root
        path_list = path.split('/')
        
        for p in path_list[1:]:
            cur = cur.children[p]
            cur.name = p

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        path_list = filePath.split('/')

        for p in path_list[1:]:
            cur = cur.children[p]
            cur.name = p

        cur.isFile = True
        cur.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        path_list = filePath.split('/')
        for p in path_list[1:]:
            cur = cur.children[p]

        if cur.isFile:
            return cur.content
        return ""
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)