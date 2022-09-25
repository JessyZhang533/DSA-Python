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
        self.children = {}
        self.is_end_of_word = False  # !!!


class Trie:
    def __init__(self):
        " Constructor "
        self.root = TrieNode("*")  # !!!

    def insert(self, word):
        " Add a word to the trie "
        temp = self.root
        for letter in word:
            if word not in temp.children:
                temp.children[letter] = TrieNode(letter)  # Creating a new node/branch: add key and value at the same time
            temp = temp.children[letter]
        temp.is_end_of_word = True

    def search(self, word):
        " Check if a word exist in the trie; return True or False "
        temp = self.root
        for letter in word:
            if letter not in temp.children:
                return False
            temp = temp.children[letter]
        return temp.is_end_of_word

    def starts_with(self, prefix):  # Same as search() except for the last line
        " Check if there is any word in the trie starting with the given prefix; return True or False "
        temp = self.root
        for letter in prefix:
            if letter not in temp.children:
                return False
            temp = temp.children[letter]
        return True


my_trie = Trie()
words = ["wait", "waitor", "shop", "shopping"]
for word in words:
    my_trie.insert(word)

print(my_trie.search("waitor"))  # Should be True
print(my_trie.search("waito"))  # Should be False
print(my_trie.starts_with("sho"))  # Should be True
