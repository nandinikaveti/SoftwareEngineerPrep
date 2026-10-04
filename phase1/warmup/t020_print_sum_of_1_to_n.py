def sum_1_to_n(n : int):
    sum = 0
    for i in range(0, n+1):
        
        sum +=i
        if i%2 == 0:
            print(i)
        if i%2 !=0:
            print(i)

    print(sum)

sum_1_to_n(10)
