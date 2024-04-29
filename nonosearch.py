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

# def print_suggestions(root, res):
#     if root.isEnd:
#         print(res, end=" ")
#     for i in range(128):  # Adjusted loop range
#         if root.Trie[i]:
#             res += chr(i)
#             print_suggestions(root.Trie[i], res)
#             res = res[:-1]

def check_present(root, key):
    for char in key:
        index = ord(char)
        if not root.Trie[index]:
           # print_suggestions(root, key[:len(key)-1])
            return False
        root = root.Trie[index]
    if root.isEnd:
        return True
   # print_suggestions(root, key)
    return False

def darnReplace(word):
    if word.endswith("er"):
        return "darner"
    elif len(word) > 4:
        return "darn" + word[4:]
    else:
        return "darn"

if __name__ == "__main__":
    root = TrieNode()
    with open("nono.txt", "r") as file:
        for word in file:
            insert_trie(root, word.strip())
    
    key = input("Enter a string for the key: ")

    print()
    if check_present(root, key):
        print("Key Present: YES\n")
    else:
        print("Key Present: NO\n")