
areas = []

food = int(input("Enter available food stock: "))
water = int(input("Enter available water stock: "))
medicine = int(input("Enter available medicine stock: "))

n = int(input("Enter number of affected areas: "))

for i in range(n):

    print("\nArea", i + 1)

    name = input("Enter area name: ")

    f = int(input("Food required: "))
    w = int(input("Water required: "))
    m = int(input("Medicine required: "))

    priority = int(input("Enter priority (1-High, 2-Medium, 3-Low): "))

    areas.append([name, f, w, m, priority])

areas.sort(key=lambda x: x[4])

print("\n--- Disaster Relief Allocation ---")

total_unmet = 0

for area in areas:

    name = area[0]

    food_given = min(area[1], food)
    food = food - food_given
    food_unmet = area[1] - food_given

    water_given = min(area[2], water)
    water = water - water_given
    water_unmet = area[2] - water_given

    medicine_given = min(area[3], medicine)
    medicine = medicine - medicine_given
    medicine_unmet = area[3] - medicine_given

    unmet = food_unmet + water_unmet + medicine_unmet
    total_unmet = total_unmet + unmet

    print("\nArea:", name)
    print("Food Allocated:", food_given)
    print("Water Allocated:", water_given)
    print("Medicine Allocated:", medicine_given)
    print("Unmet Demand:", unmet)

print("\n--- Remaining Stock ---")
print("Food:", food)
print("Water:", water)
print("Medicine:", medicine)

print("Total Unmet Demand:", total_unmet)

