def matrix(n):
    result = []
    for i in range(1, n+1):
        row = []

        for j in range(1, n+1):
            row.append(i*j)
       
        result.append(row)

    return result
    
print(matrix(3))
print(matrix(4))


