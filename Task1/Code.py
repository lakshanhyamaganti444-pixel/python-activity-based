
total_amount = 0

n = int(input("Enter number of passengers: "))

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = int(input("Enter distance in km: "))

    print("1. Sleeper")
    print("2. AC")
    print("3. First Class")

    choice = int(input("Select travel class: "))

  
    if distance <= 100:
        rate = 1
    elif distance <= 300:
        rate = 2
    else:
        rate = 3

    
    if choice == 1:
        class_rate = 1
    elif choice == 2:
        class_rate = 2
    else:
        class_rate = 3

    basic_fare = distance * rate * class_rate


    if age < 12:
        concession = basic_fare * 0.50
    elif age >= 60:
        concession = basic_fare * 0.30
    else:
        concession = 0

    reservation_fee = 50

    final_fare = basic_fare - concession + reservation_fee

    print("\nPassenger Name:", name)
    print("Basic Fare:", basic_fare)
    print("Concession:", concession)
    print("Reservation Fee:", reservation_fee)
    print("Ticket Fare:", final_fare)

    cancel = input("Cancel ticket? (yes/no): ")

    if cancel == "yes":
        penalty = final_fare * 0.25
        refund = final_fare - penalty
        print("Cancellation Penalty:", penalty)
        print("Refund Amount:", refund)
        total_amount += 0
    else:
        print("Ticket Confirmed!")
        total_amount += final_fare

print("\nTotal Booking Amount:", total_amount)

