from typing import Optional, Dict, List


class TrieNode:
    def __init__(self) -> None:
        self.word: bool = False
        self.children: dict = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        if node.word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False

        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


words = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
prefix = [[], "start", "apple", "app", "sear", "app"]

# Your Trie object will be instantiated and called as such:
obj = Trie()
for word in words:
    obj.insert(word)
param_2 = obj.search("starts")
for idx in prefix:
    param_3 = obj.startsWith(idx)
