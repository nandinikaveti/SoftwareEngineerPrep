def per_change(old: int, new:int):
    change = 0
    if old > 0:
        change = new-old
        print(change)
        return ("This is the change in percentage", (change/old)*100)


print(per_change(50, 75))
print(per_change(25, 50))


