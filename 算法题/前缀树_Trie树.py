class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = 0
        c = self.tree
        while cur < len(word) and word[cur] in c:
            c = c[word[cur]]
            cur += 1

        for i in range(cur, len(word)):
            c[word[i]] = {}
            c = c[word[i]]
        c[0] = 0

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        c = self.tree
        for i in word:
            if i not in c:
                return False
            c = c[i]
        if 0 in c:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        c = self.tree
        for i in prefix:
            if i not in c:
                return False
            c = c[i]
        return True

t = Trie()
word = 'adasd'
t.insert(word)
print(t.search(word))
print(t.startsWith('ad'))