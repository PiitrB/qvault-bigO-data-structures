# Implementing a Toy Hash Map
# Let's build a toy hash map in Python. In the real world, you would almost always use the built in dictionary if you need a hash map. 
# However, just using a dictionary doesn't teach us about what's going on under the hood!
# As usual, we'll be building out a class, and we'll call it HashMap. The map will use a simple Python List underneath to store the data, 
# and we'll call that list hashmap. As you can see in the provided constructor, we are initializing the hashmap to the size provided.

# Assignment
# Before we can build the insert and get methods, we need a way to map an arbitrary key (in our case just strings) to an index in the map.
# Implement the hashing function, which we'll call key_to_index. It should:
# Take a key (string) as input
# Add the ASCII values of all the characters in the string
# Mod ( % ) the sum by the size of the hashtable to get an index which should be an int
# Return the index

class HashMap:
    def key_to_index(self, key):
        index = 0
        for char in key:
            index += ord(char)
        index = index % len(self.hashmap)
        return index

        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --
    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)


def main():
    hm = HashMap(256)
    print(hm.key_to_index("hello"))
    print(hm.key_to_index("world"))

    hm_large = HashMap(512)
    print(hm_large.key_to_index("this is a longer key"))
    print(hm_large.key_to_index("what could this possibly hash to"))


main()
