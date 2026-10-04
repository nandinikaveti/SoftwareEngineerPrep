def fib(n):
    a = 0
    b = 1
    for i in range(0, n+1):
        print(a)
        a, b = b, a+b
        


print(fib(3))
        