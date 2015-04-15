"""
A space-efficient probabilistic data structure that is used to test whether 
an element is a member of a set.
"""
#Need to complete implementation -- Just a placeholder
from math import log, pow, ceil

class BloomFilter:
    def __init__(self, n=1000, p=0.01):
        self.n = n #Number of elements (Bloom Filter capacity)
        self.p = p #Error Probability (False positive rate)
        self.m = 0 #Bloom Filter size (number of bits in filter) (calc)
        self.k = 0 #Number of Hash functions used (calc)
    
    #(Re)Calculate the parameters based on the values of 'n' and 'p'
    def calculate_parameters(self):
        self.m = -1* self.n * log(self.p)/(pow(log(2), 2))
        self.k = log(2) * self.m / self.n
        return(int(ceil(self.m)), int(ceil(self.k)))

    def setup_bloomfilter(self):
        

bf = BloomFilter(n=3000)
print bf.calculate_parameters()

