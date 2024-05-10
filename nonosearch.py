class TrieNode:
    def __init__(self):
        self.children = {}  # Adjusted size to accommodate ASCII characters
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_trie(self, word):
        temp = self.root
        for char in word:
            if char not in temp.children:
                temp.children[char] = TrieNode()
            temp = temp.children[char]
        temp.isEnd = True
        

    def check_present(self, key):
        matches = []
        n = len(key)
        for i in range(n):
            temp = self.root
            j = i
            while j < n and key[j] in temp.children:
                temp = temp.children[key[j]]
                if temp.isEnd:
                    matches.append((i, j))
                j += 1
        return matches
    
def darn_replace(message, trie):
    matches = trie.check_present(message)
    censored_message = list(message)
    for start, end in matches:
        replacement = darnHelper(message[start:end+1])
        censored_message[start:end+1] = list(replacement)
    return ''.join(censored_message)

def darnHelper(word):
    if word.endswith("er"):
        return "darner"
    elif len(word) > 4:
        return "darn" + word[4:]
    else:
        return "darn"

if __name__ == "__main__":
    trie = Trie()
    words = ["heck", "damn"]

    for word in words:
        trie.insert_trie(word)



    message = "what the heck"
    
    censored = darn_replace(message, trie)
    print(censored)
