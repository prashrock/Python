#!/usr/bin/python
#http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2008/recitations/recitation06.pdf
import unittest


class RollingHash:
    """
    Weak but efficient(faster) hash computation for a rolling sequence of 
    numbers. Does not store the sequence of numbers,so constant memory    
    footprint. Based on "Amnesiac RollingHash" from MIT Algorithms(6006)
    """
    def __init__(self, base = 256, prime = 1009, roll_length = 0):
        self.hash_val = 0
        self.base = base      #input value range (ASCII code size)
        self.mod = prime      #some random prime number
        self.roll_length = roll_length
        self.base_cached = None
        #if possible, pre-compute 'base ^ (roll_length - 1) % mod'
        if(self.roll_length > 0):
            self.base_cached = 1
            for i in range(0, self.roll_length): self.base_cached = \
                    (self.base * self.base_cached) % self.mod
            #print "base set as %d" % (self.base_cached)

    def digest(self):
        return self.hash_val

    # Method to compute the hash of a given input list. Does not remember
    # the calculated hash_value
    # @param inp_list, a list of integers which the user wants to insert
    # @return hash_value
    def straight_hash(self, inp_list):
        hv = 0
        for i in range(0, len(inp_list)):
            hv = (hv * self.base + inp_list[i]) % self.mod
        return hv

    # Method to compute the hash of a given input char list. Does not 
    # remember the calculated hash_value
    # @param inp_list, a list of integers which the user wants to insert
    # @return hash_value
    def straight_hash_char(self, inp_char_list):
        hv = 0
        for i in range(0, len(inp_char_list)):
            hv = (hv * self.base + ord(inp_char_list[i])) % self.mod
        return hv

    # Method to append new_val at the end of the rolling hash sequence:
    # ((hash_val * base) + new_val) % prime
    # @param new_val, new integer to be inserted into the rolling hash
    # @return hash_val
    def append(self, new_val):
        self.hash_val = (self.hash_val * self.base + new_val) % self.mod
        if(self.base_cached is None): self.roll_length += 1
        return self.digest()
    
    # Method to remove oldest integer (num@beginning of rolling sequence)
    # from the rolling hash.
    # (hash_val - old_val * (base^(roll_length) % prime)) % prime
    # @param old_val, oldest integer to be removed from the rolling hash
    # @return hash_value
    def remove(self, old_val):
        if(self.base_cached is None):
            if(self.roll_length == 0):
                print "Error: Rolling hash already empty-remove failed"
            self.hash_val = (self.hash_val + self.mod - \
                old_val * pow(self.base,self.roll_length)%self.mod) \
                % self.mod
            self.roll_length -= 1
        else:
            self.hash_val = (self.hash_val + self.mod - \
                 self.base_cached * old_val % self.mod) % self.mod
        return self.digest()


class TestRollingHash(unittest.TestCase):
    inp = [1, 1, 2, 1, 1, 2]
    def setUp(self):
        print "Input is :"
        print self.inp

    def test_hash_list(self, inp_list = None, roll_len = 2):
        if(inp_list == None): inp_list = self.inp
        h = RollingHash(roll_length = roll_len)
        hash_list = list()
        for i in range(0, roll_len):
            h.append(inp_list[i])
        hash_list.append(h.digest())
        for i in range(roll_len, len(inp_list)):
            h.append(inp_list[i])
            h.remove(inp_list[i - roll_len])
            hash_list.append(h.digest())
        print hash_list
        self.assertEqual(0, 0)
    
if __name__ == '__main__':
    unittest.main()
