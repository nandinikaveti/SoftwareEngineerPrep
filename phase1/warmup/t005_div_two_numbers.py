def div(a:float, b:float):
    try:
        c = a/b
        return c
    except ZeroDivisionError:
        print("cannot divide by zero")

print(div(7, 2))