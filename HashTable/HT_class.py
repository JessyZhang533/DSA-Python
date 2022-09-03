# Should always have a prime number of addresses: increases the randomness of distribution & reduces collisions.

class HashTable:
    def __init__(self, size=7):  # '...=...': set the default value if not passing an argument
        " Constructor "
        self.data_map = [None] * size

    def __hash(self, key):
        " Pass/Input the key, determine/output the address "
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            # ord(): Get the ASCII (America Standard Code for Information Interchange) number for each letter
            # 23: Can be any prime number
            # %: Get the remainder. 'len(self.data_map)' is 7, so the remainder can only be 0-6.
            return my_hash

    def print_table(self):
        " Print items in the hash table one by one "
        for i, val in enumerate(self.data_map):  # enumerate: https://www.programiz.com/python-programming/methods/built-in/enumerate
            print(i, ": ", val)
            # i: the address
            # val: the item/key-value pair at the address


my_hash_table = HashTable()
my_hash_table.print_table()
