"""
Use Python Dictionary to Solve DNA Sequence matching. Use dictionary to 
track which 10-digit sequences occur more than once. Lastly, Prune duplicates
with Python Set Data-Structure.
"""

import unittest

# @param s, a string
# @return a list of strings
def findRepeatedDnaSequences(text, n = 10):
    if(len(text) < n): return [] #If text is shorter than pattern,stop here
    output = list()
    needles_dict = dict()        #'Key'=pattern, 'Value'=offset in text
    for i in range(0, len(text)):
        needle = text[i:i+n]     #Each 10-digit seq is a potential needle
        if(len(needle) == n):
            if(needle not in needles_dict): #new needle
                needles_dict[needle] = i    #add needle to dictionary
            else:
                output.append(needle) #Don't worry about duplicates, keep
    #After finding all needles which occur more than once, remove duplicates
    output = list(set(output))        #Prune duplicates from output
    return output



class TestRepeatedDnaSequences(unittest.TestCase):
    def test_one_full_match(self):
        print "Test if a single match can be found:",
        text = "AAAAAAAAAAAAAAAAAAAA"
        self.assertEqual(text[0:10], findRepeatedDnaSequences(text)[0])
        print "Passed"

    def test_big_match(self):
        print "Test if a big sequence (1000 chars) can be parsed quickly:",
        text = "TGCTCCTGTCACAACTTCTTTACCAGCCTGTTTTTCTAGAGTCGGCTCAAAACCTGCCTTTATGCGCAGCTGTCCACGAGAATTTCATGTTATCGAGGACCGCGATATACCCAATCGCGCGCCCCAGAAAAAAGAGTCTTACCAGATGTATACGGTGACGACCCAGTGGGTAAGACCGCTCTGCTCAGCGACCCGTCCATACCCACAGTCAGCCATGTGTGACATATCAGCGTGCATTCTTGATCTGTATGGGTGCGCTGCCCCCGCACTTGATGGGGTATGTGATGACTCCGCTCGGTAAGCAAGACCCTGGGGGTTCGGACGTAGGGTATACCCGAACTTCACGTATGCGGACACCAACGCACGTGCCAATTTATCTAACGTATGTCTCCATGCCGCCCAGAAGGTTAAAGTGGACCGCCGTTCGTATACTGTTTCTGCAATTGTGTGCGGCAGCACCAGGTAGAGAGCATTCTATTTCGCTAGCTAGTAAATCTACTTCACCGAGTCTGGAAGCTCCAATCGCTGTTTACAAACTTTTTGCCCCTGCGTGGGTCAGGCCATGTCCCGTTCCCGAGGATTCTAGCACTGACCTAGCCCTATATCACGAGCCGGGTTTTCTTAAAATAGAGATCGGGACGTTAAGGTCTTATGAACGGCTTCAGCTATCTTCCGCTTACCAACTGAGCCGAACTATCTCCGGGTGTTACATGGATCCTAAAATGCTCTCCAATTTTGCCCCTGCATGGTATTTCTCTTGAGACTACTGGATCTACCTGGGTTGTGCATGTTTCGTGTCTCTTCCGACGTTCGACAATTGGGGGCGACGCTTTAAGTTCTACTACGGTGAGATGCACATCCCACGGACGCCCTTTTCCTTTGGCTCTTCCTACGTTCGCGAGCGGTCCTGTAGGACAGTTGCTTTATGCCAACTTTTACGAGGGTGGAATACAGTATCGCCATGACACTCTGAAAAAGGATGGAAGACCTGAGATTCACC"
        self.assertEqual(3, len(findRepeatedDnaSequences(text)))
        print "Passed"

if __name__ == '__main__':
    unittest.main()
