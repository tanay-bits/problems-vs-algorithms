## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        out = []

        if len(self.children.keys()) == 0:
            return out

        for char in self.children:
            new_suffix = suffix + char
            new_node = self.children[char]

            if new_node.is_word:
                out.append(new_suffix)

            out.extend(new_node.suffixes(new_suffix))

        return out


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]

        return current_node

# Tests:

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Test 1
prefix = "f"
prefixNode = MyTrie.find(prefix)
print('\n'.join(prefixNode.suffixes())) if prefixNode else print(prefix + " not found")
# un
# unction
# actory

# Test 2
prefix = "trig"
prefixNode = MyTrie.find(prefix)
print('\n'.join(prefixNode.suffixes())) if prefixNode else print(prefix + " not found")
# ger
# onometry

# Test 3
prefix = "anto"
prefixNode = MyTrie.find(prefix)
print('\n'.join(prefixNode.suffixes())) if prefixNode else print(prefix + " not found")
# nym

# Test 4
prefix = "antonym"
prefixNode = MyTrie.find(prefix)
print('\n'.join(prefixNode.suffixes())) if prefixNode else print(prefix + " not found")
# "" (empty string)

# Test 5
prefix = "antonyma"
prefixNode = MyTrie.find(prefix)
print('\n'.join(prefixNode.suffixes())) if prefixNode else print(prefix + " not found")
# antonyma not found

# Test 6
prefix = "xe"
prefixNode = MyTrie.find(prefix)
print('\n'.join(prefixNode.suffixes())) if prefixNode else print(prefix + " not found")
# xe not found

# Test 7
prefix = ""
prefixNode = MyTrie.find(prefix)
print('\n'.join(prefixNode.suffixes())) if prefixNode else print(prefix + " not found")
# ant
# anthology
# antagonist
# antonym
# fun
# function
# factory
# trie
# trigger
# trigonometry
# tripod
