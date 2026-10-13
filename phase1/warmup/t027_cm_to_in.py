def in_to_cm(inches):
    return (inches * 2.54)
def cm_to_feet_inches(centimeters):
    feet = 0
    inches = 0

    feet = centimeters // 30.48
    remaining_cm = centimeters-(feet*30.48)
    inches = remaining_cm *2.54
    return feet, inches

print(in_to_cm(5.4))
print(cm_to_feet_inches(180))