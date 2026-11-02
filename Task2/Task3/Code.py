
total_bill = 0
high_users = 0

n = int(input("Enter number of households: "))

for i in range(n):

    print("\nHousehold", i + 1)

    name = input("Enter household name: ")
    units = int(input("Enter water consumption in litres: "))

    if units <= 1000:
        bill = (units / 100) * 2

    elif units <= 2000:
        bill = (1000 / 100) * 2
        bill = bill + ((units - 1000) / 100) * 3

    else:
        bill = (1000 / 100) * 2
        bill = bill + (1000 / 100) * 3
        bill = bill + ((units - 2000) / 100) * 5

    fixed_fee = 50

    if units > 2000:
        penalty = 100
        high_users = high_users + 1
    else:
        penalty = 0

    final_bill = bill + fixed_fee + penalty

    print("Household Name:", name)
    print("Water Consumption:", units, "litres")
    print("Water Charge:", bill)
    print("Fixed Fee:", fixed_fee)
    print("Penalty:", penalty)
    print("Final Bill:", final_bill)

    total_bill = total_bill + final_bill

print("\nTotal Water Bill Collection:", total_bill)
print("Number of Excessive Users:", high_users)

