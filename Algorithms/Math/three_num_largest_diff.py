"""
Input 3 numbers from user, sort them and decide whether the smallest
or largest is further away from the remaining number 
"""

#from sys import stdin

def three_int_largest_diff(iv_list):
    iv = [];
    for n in iv_list: iv.append(int(n));
    low = min(iv)                              #Smallest
    high = max(iv)                             #Largest
    mid = iv[0] + iv[1] + iv[2] - (low + high) #Solve for 3rd int
    print "Sorted:", low, mid, high
    ans = 0
    if(high - mid > mid - low): ans = high
    else:                       ans = low
    print "Ans:", ans

def input_three_integers():
    inp_str = raw_input('Enter three numbers (seperated by space) ')
    inp_vec = inp_str.split()
    if(len(inp_vec) != 3):
        print "Error: expecting only 3 integers !"
        return None
    return inp_vec

while(1):
    int_vec = input_three_integers()
    if(int_vec != None):
        three_int_largest_diff(int_vec)



