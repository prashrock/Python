"""
Rabin-Karp is a Linear expected-time algorithm for string matching.
This approach involves comparing the hash of the pattern at each position
of the input string. The hash value is updated (not re-calculated) for each
character in the input string. This approach is better suited when number 
of matches is low and the pattern is bigger(long). A good rolling hash 
function can help avoid unnecessary false positives
Time Complexity, Average = O(n + m) Worst = O(nm)
"""

import unittest
import sys
sys.path.append('../../../Python/Algorithms/Hash')
from RollingHash import RollingHash

#@param text    - input stream of length n
#@param pattern - search string of length m
#@param verify  - manually verify each match to avoid false-positives
#@param verbose - control verbosity of this functionm
#return a list containing all the offsets where pattern occurs in text
def Rabin_Karp_string_match(text, pattern, verify=1, verbose=0):
    num_false_positives = 0  #counts when hash matches but string does not
    n = len(text)
    m = len(pattern)
    if(n == 0 or n < m):     #Validate input first
        return None
    h_txt = h_pat = 0        #Holds hash of text and pattern respectively
    hash_fn = RollingHash(roll_length = m) #Initialize Rolling Hash
    offsets = list()         #Hold starting offset of each matches
    h_pat = hash_fn.straight_hash_char(pattern)
    #print 'Hash of "' + pattern + '" = ' + str(h_pat)
    #Add first 'm-1' chars into rolling hash
    for i in range(0, m): hash_fn.append(ord(text[i]))
    h_txt = hash_fn.digest()
    for i in range(m, n+1):  #n-m+1 hash comparisons required
        if(h_txt == h_pat):
            if(verify == 0): #Do not worry about false positives
                offsets.append(i)
            elif((text[i-m:i]) == pattern): 
                offsets.append(i)
            else: 
                num_false_positives += 1
        if(i == n): break
        hash_fn.append(ord(text[i]))
        hash_fn.remove(ord(text[i - m]))
        h_txt = hash_fn.digest()
    if(verbose > 0):
        print ("Found %d matches and %d false positives" % \
                   (len(offsets), num_false_positives))
    return offsets


class TestRabinKarp(unittest.TestCase):
    def test_no_match(self):
        print 'Test for no match: ',
        text = "abcdef"
        pattern = "g"
        offs = Rabin_Karp_string_match(text, pattern)
        self.assertEqual(len(offs), 0)
        print 'Passed'

    def test_all_match(self):
        text = "what what what what what what"
        print 'Test for all word match: ',
        pattern = "what"
        offs = Rabin_Karp_string_match(text, pattern)
        self.assertEqual(len(offs), 6)
        print 'Passed'

    def test_two_match(self):
        text = "king, are you glad you are king"
        print 'Test for only 2 specific words: ',
        pattern = "king"
        offs = Rabin_Karp_string_match(text, pattern)
        self.assertEqual(len(offs), 2)
        print 'Passed'
if __name__ == '__main__':
    unittest.main()
