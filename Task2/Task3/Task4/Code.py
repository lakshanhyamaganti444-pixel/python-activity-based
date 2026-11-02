
capacity = int(input("Enter bus capacity: "))

passengers = int(input("Enter initial passengers: "))

stops = int(input("Enter number of stops: "))

violations = 0

for i in range(stops):

    print("\nStop", i + 1)

    boarding = int(input("Enter boarding passengers: "))

    alighting = int(input("Enter alighting passengers: "))

    passengers = passengers - alighting
    passengers = passengers + boarding

    print("Total Passengers:", passengers)
    if passengers > capacity:
        print("Warning: Capacity Exceeded!")
        violations = violations + 1
    else:
        print("Bus Capacity is Normal")

print("\nFinal Passenger Count:", passengers)
print("Total Capacity Violations:", violations)

