class TrieNode:
    def __init__(self):
        self.Trie = [None] * 128  # Adjusted size to accommodate ASCII characters
        self.isEnd = False

def insert_trie(root, s):
    temp = root
    for char in s:
        index = ord(char)
        if not temp.Trie[index]:
            temp.Trie[index] = TrieNode()
        temp = temp.Trie[index]
    temp.isEnd = True

def check_present(root, key):
    for char in key:
        index = ord(char)
        if not root.Trie[index]:
            return False
        root = root.Trie[index]
    if root.isEnd:
        return True
    return False

def darnReplace(word):
    if word.endswith("er"):
        return "darner"
    elif len(word) > 4:
        return "darn" + word[4:]
    else:
        return "darn"
