def avg_mean_median(n:list):
    sum = 0
    avg = 0
    median = 0
    for i in range(0, len(n)): 
        sum = sum + n[i]
    avg = sum/len(n)

    i = len(n)//2
    median = n[i]
    
    print(median)
    print(avg)

n = (4, 3, 2)
avg_mean_median(n)