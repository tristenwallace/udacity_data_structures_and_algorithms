class TrieNode:
    def __init__(self):
        self.children = {}  # A dictionary to hold child nodes
        self.is_end_of_word = False  # To mark the end of a word

    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
            
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def suffixes(self, node, suffix=''):
        suffixes_list = []

        def _suffixes_recur(node, current_suffix):
            if node.is_end_of_word and current_suffix != '':
                suffixes_list.append(current_suffix)

            for char, next_node in node.children.items():
                _suffixes_recur(next_node, current_suffix + char)

        _suffixes_recur(node, suffix)
        return suffixes_list
    
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def autocomplete(prefix):
    prefixNode = MyTrie.find(prefix)
    if prefixNode:
        return MyTrie.suffixes(prefixNode)
    else:
        return prefix + " not found"


# Test Case 1
prefix = "ant"
print(f"Suffixes for '{prefix}': {autocomplete(prefix)}")
