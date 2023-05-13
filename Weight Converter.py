weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print(f"You are {converted} Lbs")
elif unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} Kg")
else:
    print("Unit incorrect")