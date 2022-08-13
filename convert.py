weight = input("Enter your weight:")
lbs_kilo = input("lbs or weight:")
if lbs_kilo=="l" or lbs_kilo=="L":
    print("Your weight is " + str(float(weight)*0.45) + " kilos")
elif lbs_kilo=="k" or lbs_kilo=="K":
    print("Your weight is " + str(float(weight)/0.45) + " lbs")
else:
    print("Enter a valid command!")


