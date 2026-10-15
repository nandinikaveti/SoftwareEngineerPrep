def prime(n):
    for i in range(2, int(n ** 0.5)):
        if n%i == 0:
            return False
       
    return True

print(prime(300))
print(prime(7919))