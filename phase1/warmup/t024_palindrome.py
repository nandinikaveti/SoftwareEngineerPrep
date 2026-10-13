def palindrome(x:str):
    l, r = 0, len(x)-1
    print(l, r)
    while l < r:
        if x[l] == x[r]:
            l+=1
            r-=1
        else:
            return False
    return True
    
x = "racecarz"
print(palindrome(x))
y = "racecar"
print(palindrome(y))