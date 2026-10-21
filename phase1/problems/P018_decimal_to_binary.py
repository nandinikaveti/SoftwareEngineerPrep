def dec_to_binary(n, base):
    remainder = []
    left_over = 0
    remain = 0
    while n >0:
        remain = n % base
        remainder.append(remain)
        left_over = n//base
        n = left_over
        
    print(remainder[::-1])
    


dec_to_binary(4, 2)
dec_to_binary(255, 2)
dec_to_binary(255, 16)

