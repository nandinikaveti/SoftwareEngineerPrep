def lcm_brute_force(a, b):
        for i in range(1, a*b + 1):
            if i%a == 0 and i%b == 0:
                return i
        return None



def gcd(a, b):
    while b!=0:
        if a % b == 0:
            return b
        else:
            a, b = b , a%b
def lcm(a, b):
     return a*b // gcd(a, b)
        

print(lcm(4, 36))
print(lcm_brute_force(4, 6))



