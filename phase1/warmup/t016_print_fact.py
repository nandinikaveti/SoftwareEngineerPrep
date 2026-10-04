def print_fact(n:int):
    if n >= 0:
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        print(fact)
    else:
        print("Factorial of negative numbers is undefined")

print_fact(5)

