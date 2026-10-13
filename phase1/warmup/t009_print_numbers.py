def print_digits(x:int):
    x = str(x)
    for c in x:
        print(c)


print_digits(409)

def math_way(a:int):

    digits_counter = 0
    x= a
    while x:
        x=x//10
        digits_counter +=1
        print(x, digits_counter)
    while digits_counter:
        print(a//10**(digits_counter-1))
        a%=10**(digits_counter-1)
        digits_counter -= 1
        print()



math_way(34454)

        
    