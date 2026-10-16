def comp_interest(p, r, t, n):
    monthly_interst_rate = 0
    increment = 0
    c_i = 0
    if p > 0:
        monthly_interst_rate = (r/100)/n
        print(monthly_interst_rate)
        increment = (1+monthly_interst_rate)** (t*n)
        print(increment)
        c_i = p * increment
        print(c_i)


comp_interest(2000, 5, 3, 12)
comp_interest(5000, 10, 10, 6)