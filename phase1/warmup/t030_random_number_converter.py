def temp_converter( ):
    while True:
        print("You can choose 1 for C to F and 2 for F to C")
        choice = int(input("Enter your choice:"))
        temp = int(input("Enter the number"))

        if choice == 1:
            print("celcius to fahrenheit is", (temp*1.8)+32)
        
        elif choice == 2:
            print(" fahrenheit to celcius is", (temp-32)/1.8)

        else:
            print("You can either choose 1 or 2")
    

temp_converter()