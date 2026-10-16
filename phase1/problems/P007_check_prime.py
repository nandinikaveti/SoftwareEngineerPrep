def prime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n%i == 0:
            return False
       
    return True

print(prime(300))
print(prime(7919))
print(prime(9))



"""
let's say if we need to find if x is prime or not

x is not prime if it has factors. i.e; x = a*b

should we iterate a from 1 to x?
while a increases b should decrease. 
there is no point to go beyond sqrt(x)

1 4 = 4
2 2 = 4
4 1 = 4

"""
