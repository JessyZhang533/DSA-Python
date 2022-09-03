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

    def set_item(self, key, value):
        " Pass two arguemnts as shown, create a key-value pair & output an address, then store the pair in a list at the address "
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []  # Create the list at the address if it hasn't been created before
        self.data_map[index].append([key, value])  # Add the pair to the list at the address


my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
