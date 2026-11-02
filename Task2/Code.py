
total_fine = 0
disqualification = False

n = int(input("Enter number of violations: "))

for i in range(n):

    print("\nViolation", i + 1)

    print("1. Two Wheeler")
    print("2. Four Wheeler")

    vehicle = int(input("Select vehicle category: "))

    print("\n1. Over Speeding")
    print("2. No Helmet")
    print("3. Signal Jump")
    print("4. Drunk Driving")

    offence = int(input("Select offence type: "))

    repeat = input("Is it a repeat offence? (yes/no): ")

    if offence == 1:
        fine = 1000
    elif offence == 2:
        fine = 500
    elif offence == 3:
        fine = 1000
    elif offence == 4:
        fine = 10000
    else:
        fine = 0

    if vehicle == 2:
        fine = fine + 200

    if repeat == "yes":
        fine = fine * 2
      
    if offence == 4 and repeat == "yes":
        disqualification = True

    print("Final Penalty:", fine)

    total_fine = total_fine + fine

print("\nTotal Traffic Fine:", total_fine)

if disqualification:
    print("Driver Disqualification: Required")
else:
    print("Driver Disqualification: Not Required")

