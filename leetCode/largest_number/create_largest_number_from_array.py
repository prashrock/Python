# Use a custom sort comparator to sort the integers
# Converted the sorted integer array into a string
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


# @param x, first integer
# @param y, second integer
# @return (xy - yx)
def cmp_aggregate(x, y):
    str_xy = ''.join((str(x), str(y)))
    str_yx = ''.join((str(y), str(x)))
    return int(str_xy) - int(str_yx)

#Sort with a custom comparator and get descending order
def largestNumber(num):
    sorted_num = sorted(num, key=cmp_to_key(cmp_aggregate), reverse=True)
    print sorted_num
    sorted_str = ''.join(map(str, sorted_num))
    if(int(sorted_str) == 0): return '0' 
    else: return sorted_str

num = [3, 30, 34, 5, 9]
print num
print largestNumber(num)
