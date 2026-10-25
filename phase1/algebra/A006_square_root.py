def sq_roots(a, b, c):
    for p in range(-10, 11):
        for q in range(-10, 11):
            if p+q == b and p*q == c:
                return  (-p, -q)

print(sq_roots(1, -5, 6))
