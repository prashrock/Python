Given a list of non negative integers, arrange them such that they form the largest number
--------------------------------------------
- For example, given [3, 30, 34, 5, 9] the largest number formed is 9534330:
- Note: The result may be very large, so you need to return a string instead of an integer.

Solution (Time = O(n log n))
--------------------------------------------
- Reduce to a sorting problem. Change the sort comparator as below:
```
  compare(x , y):
    str_xy = concatenate(str(x), str(y))
    str_yx = concatenate(str(y), str(x))
    return (integer(str_xy) - integer(str_yx))
```