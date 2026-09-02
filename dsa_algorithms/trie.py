# Trie (Prefix Tree) - efficient for string search/autocomplete, O(L) where L = word length

class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end = False  # marks end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # 1. INSERT - O(L)
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    # 2. SEARCH (exact word) - O(L)
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end  # must be end-of-word
    
    # 3. STARTS WITH (prefix) - O(L)
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    # 4. AUTOCOMPLETE - get all words with given prefix
    def autocomplete(self, prefix):
        node = self.root
        # Navigate to prefix node
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # DFS to collect all words
        results = []
        def dfs(node, path):
            if node.is_end:
                results.append(prefix + path)
            for char, child in node.children.items():
                dfs(child, path + char)
        
        dfs(node, "")
        return results

# DEMONSTRATION
trie = Trie()
words = ["apple", "app", "apricot", "banana", "bat", "ball"]
for w in words:
    trie.insert(w)

print("Search 'app':", trie.search("app"))        # True
print("Search 'apple':", trie.search("apple"))    # True
print("Search 'apples':", trie.search("apples"))  # False
print("Starts with 'ap':", trie.starts_with("ap"))  # True
print("Autocomplete 'ap':", trie.autocomplete("ap"))  # ['apricot', 'app', 'apple']
print("Autocomplete 'ba':", trie.autocomplete("ba"))  # ['banana', 'bat', 'ball']

# Real-world uses: autocomplete, spell checker, IP routing, dictionary