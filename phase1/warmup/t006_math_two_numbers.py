a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
def math(a, b):
    return (a+b, a-b, a/b, a//b, a%b, a**b)
res = math(a, b)
print(res)
