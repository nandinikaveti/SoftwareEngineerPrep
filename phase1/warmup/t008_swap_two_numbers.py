a  = int(input("enter a"))
b = int(input("enter b"))
temp = a
a = b
b = temp

print(a, b)



def swap(a, b):
    a  = a + b
    b = a - b
    a = a - b
    return a, b

print(swap(a, b))

