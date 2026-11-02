def inspect_values(a, b):
    return type(a), type(b), a == b, a is b
    
    


print(inspect_values(2, 3.4))
print(inspect_values("hello", "hello"))

a = [1, 2, 3]
b = [1, 2, 3]
print(inspect_values(a, b))
print(inspect_values(2, 2))