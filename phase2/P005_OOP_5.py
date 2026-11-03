def slicing(n):
    res = []
    odd_nums = []
    dictionary = {}

    for i in n:
        if i**2 % 3 == 0:
            res.append(i**2)

        if i % 2 != 0:
            odd_nums.append(i)
        dictionary[i] = i**2

            

    return res, odd_nums, dictionary
    
    
        

n = [1, 2, 3, 4, 5]
print(slicing(n))