import math
def rounding(a, b):
    return ("this is a/b", a/b, "This is a//b", a//b, "this is int(a/b)",  int(a/b) , "this is math.floor", math.floor(a/b), "This is math.ceil(a/b)", math.ceil(a/b)) 

print(rounding(5,4))