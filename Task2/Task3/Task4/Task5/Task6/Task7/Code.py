
wards = []

n = int(input("Enter number of wards: "))

for i in range(n):

    print("\nWard", i + 1)

    name = input("Enter ward name: ")

    total_beds = int(input("Enter total beds: "))
    occupied_beds = int(input("Enter occupied beds: "))

    available_staff = int(input("Enter available staff: "))
    required_staff = int(input("Enter required staff: "))

    available_equipment = int(input("Enter available equipment: "))
    required_equipment = int(input("Enter required equipment: "))

    ward = [
        name,
        [total_beds, occupied_beds],
        [available_staff, required_staff],
        [available_equipment, required_equipment]
    ]

    wards.append(ward)

print("\n--- Hospital Resource Report ---")

for ward in wards:

    name = ward[0]
    beds = ward[1]
    staff = ward[2]
    equipment = ward[3]

    shortages = 0

    print("\nWard:", name)

    if beds[0] - beds[1] <= 0:
        print("Bed Shortage")
        shortages = shortages + 1
    else:
        print("Beds Available:", beds[0] - beds[1])

    if staff[0] < staff[1]:
        print("Staff Shortage")
        shortages = shortages + 1
    else:
        print("Staff Available")

    if equipment[0] < equipment[1]:
        print("Equipment Shortage")
        shortages = shortages + 1
    else:
        print("Equipment Available")

    if shortages >= 2:
        print("Priority: HIGH")
    elif shortages == 1:
        print("Priority: MEDIUM")
    else:
        print("Priority: LOW")

print("\nHospital Resource Analysis Completed")

