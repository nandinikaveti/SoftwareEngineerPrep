def convert_temp(x, y):
    print("celcius to fahrenheit is", (x*1.8)+32)
    print(" fahrenheit to celcius is", (y-32)/1.8)

convert_temp(0, 212)



def celcius_to_fahrenhiet(celcius):
    return ((celcius*1.8)+32)

def fahrenhiet_to_celcius(fahrenhiet):
    return ((fahrenhiet-32)/1.8)

print(celcius_to_fahrenhiet(9))
print(fahrenhiet_to_celcius(62))
