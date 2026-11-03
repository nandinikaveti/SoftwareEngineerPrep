def make_counter(start): 
    count = start

    def counter():
        nonlocal count

        count+=1

        return count
    return counter


counter1 = make_counter(5)
counter2 = make_counter(3)
print(counter1())
print(counter2())