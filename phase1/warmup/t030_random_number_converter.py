def temp_converter( ):
    print("You can choose 1 for C to F and 2 for F to C")
    choice = int(input("Enter your choice:"))
    temp = int(input("Enter the number"))

    if choice == 1:
        print("celcius to fahrenheit is", (temp*1.8)+32)
    else:
        print(" fahrenheit to celcius is", (temp-32)/1.8)

temp_converter()