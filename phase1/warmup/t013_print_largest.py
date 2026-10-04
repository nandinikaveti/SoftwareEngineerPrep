def print_largest(a:int, b:int, c:int):
    if a >= b and a >= c:
        print("a is the largest")
    elif b >= a and b >= c:
        print("b is largest")
    else:
        print("c is largest")

print(print_largest(2, 3, 0))

def print_lar(a, b, c):
    largest = a
    if b > largest:
        largest = b
        
    elif c > largest:
        largest = c
    print(largest)

print(print_lar(5, 6, 7))


    

    