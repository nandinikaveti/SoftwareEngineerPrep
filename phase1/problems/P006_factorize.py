def factorize(n):
    count = {}
    i=2
    while n > 1:
        if n % i == 0:
            if i in count:
                count[i]+=1
            else:
                count[i]= 1  
            n//=i
        else:
            i+=1

    return count
print(factorize(12))
print(factorize(360))
