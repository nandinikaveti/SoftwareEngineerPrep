def per_change(old: int, new:int):
    change = 0
    if old > 0:
        change = new-old
        print(change)
        return ("This is the decrease in percentage", (change/old)*100)



print(per_change(90, 20))