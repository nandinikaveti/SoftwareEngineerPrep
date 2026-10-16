def ratios(a, b, total):
    parts = 0
    a_share = 0
    b_share = 0
    if total >0:
        parts = total/(a+b)
        print(parts)
        a_share = a * parts
        b_share = b * parts
        print(a_share, b_share)


ratios(3, 5 ,64)
ratios(3, 5, 10)
