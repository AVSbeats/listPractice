# Arrays or in Python is called list

saiyans = ["Goku", "Vegeta", "Broly", "Trunks"]

for fighterName in saiyans:
    print(fighterName)

print()
print(len(saiyans))
print()

saiyans.insert(1, "Gohan")
saiyans.insert(4, "Nappa")

saiyans.sort()
print(f"The total saiyans are:\n {saiyans}",)
print()
