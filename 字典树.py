"""
字典树
"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.root
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]

        tree['#'] = '#'
        print(tree)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.root
        #print(tree)
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
            #print(tree)
        if '#' in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.root
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True

trie =Trie()
trie.insert("apple")
# trie.search("apple")
# trie.search("app")
# trie.startsWith("app")
# trie.insert("app")
# trie.search("app")