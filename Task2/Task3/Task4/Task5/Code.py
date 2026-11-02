
total_prepared = 0
total_served = 0
total_leftovers = 0
waste_days = 0

days = int(input("Enter number of days: "))

limit = 10

for i in range(days):

    print("\nDay", i + 1)

    prepared = int(input("Enter meals prepared: "))
    served = int(input("Enter meals served: "))

    leftovers = prepared - served

    percentage = (leftovers / prepared) * 100

    print("Leftover Meals:", leftovers)
    print("Wastage Percentage:", percentage, "%")

    if percentage > limit:
        print("Warning: Excessive Food Waste!")
        waste_days = waste_days + 1
    else:
        print("Food Waste is Acceptable")

    total_prepared = total_prepared + prepared
    total_served = total_served + served
    total_leftovers = total_leftovers + leftovers

print("\nTotal Meals Prepared:", total_prepared)
print("Total Meals Served:", total_served)
print("Total Leftovers:", total_leftovers)
print("Days with Excessive Waste:", waste_days)

