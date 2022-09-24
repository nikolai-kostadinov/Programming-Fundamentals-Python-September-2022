number_of_lines = int(input())
capacity = 255
liters_in_tank = 0

for i in range(number_of_lines):
    liters_of_water = int(input())

    if liters_of_water <= capacity:
        capacity -= liters_of_water
        liters_in_tank += liters_of_water
    else:
        print("Insufficient capacity!")
print(liters_in_tank)


