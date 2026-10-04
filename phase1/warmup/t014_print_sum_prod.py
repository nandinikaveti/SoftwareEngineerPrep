def sum_prod(n:int):
    n = str(n)
    total = 0
    prod = 1
    count = 0
    for c in n:
        c = int(c)
        total = total + c
        prod = prod * c
        count +=1
    print(total)
    print(prod)
    print(count)


print(sum_prod(4825))