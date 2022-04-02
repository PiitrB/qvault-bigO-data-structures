# Implementing a Toy Hash Map - Insert
# Assignment 1
# Complete the insert method. It takes a key (a string) and a value that can be of any type and stores them in the map as a tuple.
# Use the key_to_index method you already created to find which index the tuple should be stored in. When you create the tuple, 
# the key should be in the tuple's index 0 and the value should be in index 1
# The hashmap list will look something like this:
# [
#     (key, val),
#     None,
#     None,
#     (key, val),
#     None,
#     ...
# ]
# Where indexes with data will have a tuple, and empty indexes will be filled with None.

# Implementing a Toy Hash Map - Get
# Assignment 2
# Complete the get method. It takes a key (a string) and returns the value stored at that location (not the whole key/value tuple).
# Use the key_to_index method to find the correct index to lookup in the self.hashmap datastore, 
# and if a value doesn't exist at that index, raise the following "sorry, key not found"  exception to indicate no key was found.

class HashMap:

    def get(self, key):
        index = self.key_to_index(key)

        if self.hashmap[index] is None:
            raise Exception("sorry, key not found")
        return self.hashmap[index][1] #return only value from tuple - only second element of tuple

        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --
    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for i, v in enumerate(self.hashmap):
            if v != None:
                buckets.append("{} @ {}".format(str(v), i))
        return str(buckets)

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)


def main():
    hm = HashMap(256)
    hm.insert('brad', 'pitt')
    hm.insert('johnny', 'depp')
    hm.insert('kate', 'blanchett')
    hm.insert('emma', 'stone')
    hm.insert('emma', 'watson')
    print(hm.get('brad'))
    print(hm.get('johnny'))
    print(hm.get('kate'))
    print(hm.get('emma'))
    try:
        print(hm.get('nokey'))
    except Exception as e:
        print(e)


main()
