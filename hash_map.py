# Name: John-Francis Caccamo
# Date: 6 / 9 / 20
#
# Description: This is the hash_map.py file
# ===================================================
# This file will implement a hash map with chaining.
# Functions will clear, get and put values from /
# into the hash map contingent of the assigned hash
# function . Other functions will return empty
# buckets, load factor, and perform hash map resizing.
# ===================================================

class SLNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_front(self, key, value):
        """Create a new node and inserts it at the front of the linked list
        Args:
            key: the key for the new node
            value: the value for the new node"""
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    def remove(self, key):
        """Removes node from linked list
        Args:
            key: key of the node to remove """
        if self.head is None:
            return False
        if self.head.key == key:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        cur = self.head.next
        prev = self.head
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                self.size = self.size - 1
                return True
            prev = cur
            cur = cur.next
        return False

    def contains(self, key):
        """Searches linked list for a node with a given key
        Args:
        	key: key of node
        Return:
        	node with matching key, otherwise None"""
        if self.head is not None:
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    return cur
                cur = cur.next
        return None

    def __str__(self):
        out = '['
        if self.head != None:
            cur = self.head
            out = out + str(self.head)
            cur = cur.next
            while cur != None:
                out = out + ' -> ' + str(cur)
                cur = cur.next
        out = out + ']'
        return out


def hash_function_1(key):
    hash = 0
    for i in key:
        hash = hash + ord(i)
    return hash


def hash_function_2(key):
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


class HashMap:
    """
    Creates a new hash map with the specified number of buckets. Will have
    a initialization function and other functions that will hash values,
    determine empty buckets and load factor, and clear all buckets.

    Args:
        capacity: the total number of buckets to be created in the hash table
        function: the hash function to use for hashing values
    """

    def __init__(self, capacity, function):
        self._buckets = []
        for i in range(capacity):
            self._buckets.append(LinkedList())
        self.capacity = capacity
        self._hash_function = function
        self.size = 0

    def return_buckets(self):
        """Getter function which will return member variable buckets."""
        return self._buckets

    def return_hash_function(self):
        """ Will access the member variable hash function."""
        return self._hash_function

    def call_hash_function(self, key):
        """Will call the member variable hash function modulo'd by the hash map capacity."""
        return self._hash_function(key) % self.capacity

    def clear(self):
        """
        Empties out the hash table deleting all links in the hash table.

        The function determine if a bucket in the hash map is associated
        with a linked list with values. If so, the linked list will be set
        to None and its size set to 0.
        """
        # FIXME: Write this function

        """for linked_list in self.return_buckets():  # iterate through the buckets
            if linked_list.head is not None:  # if the linked list associated with bucket has value(s)
                linked_list.head = None  # set ll to none
                linked_list.size = 0  # set size to 0"""
        self._buckets = []  # reinitialize buckets to an empty hash map
        self.size = 0  # set size of hash map to 0
        return

    def get(self, key):
        """
        Returns the value with the given key. The function will hash the input key,
        iterate through the associated linked list and return the associated value
        corresponding to the key.

        Args:
            key: the value of the key to look for
        Return:
            The value associated to the key. None if the link isn't found.
        """
        # FIXME: Write this function

        if self.contains_key(key):  # if a key corresponds to a bucket with ll values
            ll_ptr = self.return_buckets()[self.call_hash_function(key)].head  # create a pointer to the head

            while ll_ptr is not None:  # while the pointer hasn't reached the end of the ll
                if ll_ptr.key == key:  # if the argument key matches the ll key
                    return ll_ptr.value  # return that value
                ll_ptr = ll_ptr.next  # otherwise, proceed with iteration

        return None

    def resize_table(self, capacity):
        """
        Resizes the hash table to have a number of buckets equal to the given
        capacity. All links need to be rehashed in this function after resizing.
        A new hash map will be created based on the capacity parameter and linked
        lists will be rehashed to this new map with its new capacity.

        Args:
            capacity: the new number of buckets.
        """
        # FIXME: Write this function

        old_buckets = self._buckets  # hold the old buckets
        old_size = self.size  # hold the old size
        self._buckets = []  # initialize an empty hash map to member variable buckets
        self.capacity = capacity  # update capacity

        for i in range(capacity):  # refill hash maps with empty linked lists
            self._buckets.append(LinkedList())

        for bucket in old_buckets:  # iterate through old buckets
            if bucket.head:  # if there are ll values associated with the old bucket
                ll_ptr = bucket.head  # create pointer at the head

                while ll_ptr is not None:  # while the pointer is not at end of linked list
                    self.put(ll_ptr.key, ll_ptr.value)  # call put function on key and its value
                    ll_ptr = ll_ptr.next  # proceed with iteration

        del old_buckets  # delete old buckets
        self.size = old_size  # reassign old size to new hash table

        return

    def put(self, key, value):
        """
        Updates the given key-value pair in the hash table. If a link with the given
        key already exists, this will just update the value and skip traversing. Otherwise,
        it will create a new link with the given key and value and add it to the table
        bucket's linked list.

        Args:
            key: they key to use to has the entry
            value: the value associated with the entry
        """
        # FIXME: Write this function

        if self.contains_key(key):  # if the key exists in the hash map
            if self.return_buckets()[self.call_hash_function(key)].remove(key):  # call the ll remove function
                self.size -= 1  # if duplicate key has been found and removed, decrement size

        self.return_buckets()[self.call_hash_function(key)].add_front(key, value)  # add the parameter key, value
        self.size += 1  # increment size

        return

    def remove(self, key):
        """
        Removes and frees the link with the given key from the table. If no such link
        exists, this does nothing. Remember to search the entire linked list at the
        bucket.

        Args:
            key: they key to search for and remove along with its value
        """
        # FIXME: Write this function

        if self.contains_key(key):  # if key exists in the hash map
            self.return_buckets()[self.call_hash_function(key)].remove(key)  # call linked list remove function
            self.size -= 1  # decrement size

        return

    def contains_key(self, key):
        """
        Searches to see if a key exists within the hash table. If a key exists
        with linked list values, the function will return True.

        Returns:
            True if the key is found False otherwise

        """
        # FIXME: Write this function

        if self.return_buckets()[self.call_hash_function(key)].head:  # if there is a linked list with values
            return True

        return False  # if empty linked list

    def empty_buckets(self):
        """
        Will iterate through the hash maps encountering buckets with associated
        linked list values. Once the total has been calculated, this total will be
        subtracted from the capacity of the hash map.

        Returns:
            The number of empty buckets in the table
        """
        # FIXME: Write this function

        bucket_value = 0  # count variable

        for bucket in self.return_buckets():  # iterate through hash map
            if bucket.head:  # if the bucket has linked list values
                bucket_value += 1  # increment bucket_value

        return self.capacity - bucket_value  # subtract capacity by bucket_value

    def table_load(self):
        """
        Will calculate table load via dividing size (the total number of
        key-value pairs) by the capacity of the hash map.

        Returns:
            the ratio of (number of links) / (number of buckets) in the table as a float.
        """
        # FIXME: Write this function

        return self.size / self.capacity  # divide size by capacity

    def __str__(self):
        """
        Prints all the links in each of the buckets in the table.
        """

        out = ""
        index = 0
        for bucket in self._buckets:
            out = out + str(index) + ': ' + str(bucket) + '\n'
            index = index + 1
        return out


"""student_map = HashMap(10, hash_function_1)
student_map_func2 = HashMap(10, hash_function_2)

first_node = ("test_val", 5)
collision_node = ("test_5", 5)

student_map.put(first_node[0], first_node[1])
student_map_func2.put(first_node[0], first_node[1])

student_map.put(first_node[0], -5)

student_map.put(collision_node[0], collision_node[1])

print(student_map.get("test_5") + 1)

print(student_map)

print(student_map.size)"""


# resize


"""def get_keys_from_map(map):
    to_return = []
    for bucket in map._buckets:
        cur_node = bucket.head
        while cur_node is not None:
            to_return.append(cur_node.key)
            cur_node = cur_node.next
    return to_return


test_values = [("test_5", 5), ("test_-5", -5), ("test_5_", 5), ("diff_word", 15), ("another_word", 20),
               ("set", 10), ("anotha_one", -7), ("completely_different", 5), ("getting_there", -1)]
student_map = HashMap(10, hash_function_1)
for key, value in test_values:
    student_map.put(key, value)

keys_before_resize = get_keys_from_map(student_map)
size_before_resize = student_map.size
print(student_map)

student_map.resize_table(50)
keys_after_resize = get_keys_from_map(student_map)
size_after_resize = student_map.size
print(student_map)"""