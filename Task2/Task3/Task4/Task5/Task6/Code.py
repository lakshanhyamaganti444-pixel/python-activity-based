
appliances = []

n = int(input("Enter number of appliances: "))

for i in range(n):

    print("\nAppliance", i + 1)

    name = input("Enter appliance name: ")

    before = float(input("Enter electricity usage before: "))

    after = float(input("Enter electricity usage after: "))

    saved = before - after

    if before > 0:
        percentage = (saved / before) * 100
    else:
        percentage = 0

    print("Energy Saved:", saved, "units")
    print("Savings Percentage:", percentage, "%")

    appliances.append((name, saved, percentage))

appliances.sort(key=lambda x: x[2], reverse=True)

print("\n--- Appliance Savings Ranking ---")

for i in range(len(appliances)):

    print(i + 1, appliances[i][0],
          "Savings:", round(appliances[i][2], 2), "%")

print("\nHighest Saving Appliance:",
      appliances[0][0])


