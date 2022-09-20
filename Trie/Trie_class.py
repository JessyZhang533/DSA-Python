# Trie: a data structure storing items (usually strings) based off of the prefixes the items share in common
# 1. every word is started with a "*", and has an end
# 2. Time complexity:
# search if a word is in a list: O(nm), n-->length of the word, m-->number of words in the list
# search if a word is in a trie: O(n), n-->length of the word
# adding a word to a trie: O(n), n-->length of word to be added
# https://www.youtube.com/watch?v=hjUJFjcrbR4


class TrieNode:
    def __init__(self, letter):
        " Constructor of nodes "
        self.letter = letter
        self.children = {}  # Here we don't use self.next, sel.left, self.right, because we are not sure how many children there are
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        " Constructor "
        self.root = TrieNode("*")  # self.root is a node

    def insert(self, word):
        " Add a word to teh trie "
        curr_node = self.root  # curr_node: current node, which is a node
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)  # curr_node.children is a dictionary, letter is the key, the new node is the value
            curr_node = curr_node.children[letter]  # Move the pointer to the next node
        curr_node.is_end_of_word = True  # End the word

    def search(self, word):
        " Check if a word exist in the trie; return True or False "
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:  # 'letter' is a key, 'curr_node.children' is a dictionary
                return False
            curr_node = curr_node.children[letter]
        return curr_node.is_end_of_word  # See if it is a 'word' or a 'path'

    def starts_with(self, prefix):  # Same as search() except for the last line
        " Check if there is any word in the trie starting with the given prefix; return True or False "
        curr_node = self.root
        for letter in prefix:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return True


my_trie = Trie()
words = ["wait", "waitor", "shop", "shopping"]
for word in words:
    my_trie.insert(word)

print(my_trie.search("waitor"))  # Should be True
print(my_trie.search("waito"))  # Should be False
print(my_trie.starts_with("sho"))  # Should be True
