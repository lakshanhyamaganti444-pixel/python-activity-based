
reports = []

n = int(input("Enter number of maintenance reports: "))

for i in range(n):

    print("\nIncident", i + 1)

    name = input("Enter incident name: ")

    print("1. High Severity")
    print("2. Medium Severity")
    print("3. Low Severity")

    severity = int(input("Enter severity: "))

    print("1. Important Location")
    print("2. Normal Location")

    location = int(input("Enter location: "))

    frequency = int(input("Enter reported frequency: "))

    if severity == 1:
        s = 3
    elif severity == 2:
        s = 2
    else:
        s = 1

    if location == 1:
        l = 2
    else:
        l = 1

    if frequency >= 5:
        f = 3
    elif frequency >= 3:
        f = 2
    else:
        f = 1

    score = s + l + f

    if score > 7:
        priority = "High"
    elif score >= 4:
        priority = "Medium"
    else:
        priority = "Low"

    reports.append([name, score, priority])

reports.sort(key=lambda x: x[1], reverse=True)

high = 0
medium = 0
low = 0

print("\n--- Campus Incident Report ---")

for report in reports:

    print("\nIncident:", report[0])
    print("Priority Score:", report[1])
    print("Priority:", report[2])

    if report[2] == "High":
        high = high + 1
    elif report[2] == "Medium":
        medium = medium + 1
    else:
        low = low + 1

print("\n--- Priority Summary ---")
print("High Priority:", high)
print("Medium Priority:", medium)
print("Low Priority:", low)

print("\nTotal Reports:", n)

