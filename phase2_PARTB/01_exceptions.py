def exception_handling():
    res = None
    try:
         a = float(input("Enter first number: "))
         b = float(input("Enter second number: "))
         res = a / b
         
    except ZeroDivisionError:
        print("Invalid: Cannot divide by zero")

    except ValueError:
            print("Please enter a number, invalid input given")
     
    return res
print(exception_handling())

#Before we move to file handling, answer these in your own words:
#1. Why must float(input()) be inside the try block? if not it is not validating the input
#2. What's the difference between ValueError and ZeroDivisionError? first one is for checking if the value of a is valid. Second is for error when diving with zero
#3. Why did we initialize res = None? UnboudLocalError is thrown if it is not used. I can also choose to write a return stmt
#4. Why do we use return instead of print() when we want a function to give a result back? I think printing does not save it...returning does 