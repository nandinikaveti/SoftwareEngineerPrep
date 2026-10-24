def significant_nums(n):
    n = str(n)
    count = 0
    started = False
    for c in n:
        if c == ".":
            print("This is the decimal point")
            continue
        if c != '0' :
            started = True
        if started:
            count +=1
    print(count)

    

n = 0.000123
significant_nums(n)
