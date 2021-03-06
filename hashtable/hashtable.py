class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


    def __str__(self):
        return f'{self.key}, {self.value}'
# Hash table can't have fewer than this many slots

class HashLinkedList:
    def __init__(self):
        self.head = None
    
    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current
            
            current = current.next
        
        return None

    def add_to_head(self, key, value):
        node = HashTableEntry(key, value)

        if self.head is not None:
            node.next = self.head

        self.head = node

    def delete(self, key):
        current = self.head

        # if there is nothing to delete
        if current is None:
            return None

        # when deleting head
        if current.key == key:
            self.head = current.next
            return current

        # when deleting something else
        else:
            previous = current
            current = current.next

            while current is not None:
                if current.key == key: # found it!
                    previous.next = current.next  # cut current out!
                    return current # return our deleted node

                else:
                    previous = current
                    current = current.next
            return None # if we got here, nothing was found!

    
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY
        
        self.table = [None] * capacity
        self.capacity = capacity

        for num in range(self.capacity):
            self.table[num] = HashLinkedList()



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        byte_array = key.encode()

        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #Get the hash_index
        hash_index = self.hash_index(key)

        #Store it in our list
        self.table[hash_index].add_to_head(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Get the hash index
        hash_index = self.hash_index(key)
        # Delete from the LL and save the result 
        result = self.table[hash_index].delete(key)

        if result is None:
            print("Sorry! key not found!")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Get the hash index
        hash_index = self.hash_index(key)
        # Save the result 
        result = self.table[hash_index].find(key)

        if result is None:
            return None

        return result.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
