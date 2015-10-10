"""
Given #people, calculate probability of atleast 2 people having same birthday
- Assume each year has 365 days (dont worry about leap years)
- Assume that with random sampling, each day in a year is equally likely.
"""

import math

def birthday_probability(n):
    num_days = 365;
    if(n > num_days):
        return 1;
    #Event = Number of ways in which atleast 2 people have the same birthday
    #Event_complement = Number of ways such that each of 'n' people have a unique 
    # birthday, i.e., Ordered Sampling without replacement = 365Pn = falling factorial
    event_complement = math.factorial(365) / math.factorial(365 - n)
    #Total_possibilities = Ordered Sampling with replacement (power)
    total_possible_outcomes = math.pow(365, n)
    probability = 1 - (event_complement / total_possible_outcomes)
    return probability;

for n in [2, 5, 10, 23, 70]:
    probability = birthday_probability(n)
    print "With ", n, " people, P(atleast 2 people having same bday) = ", probability
