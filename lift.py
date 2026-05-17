floor = int(input("Enter floor number(0-10): "))
if floor <0 or floor >10:
    print("Invalid floor")
else:
    weight = int(input("Enter total weight (kg): "))
    if weight > 500:
        print("Overweight - Lift cannot move")
    else:
        door = input("Is door closed? (yes/no): ").lower()
        if door != "yes":
            print("Warning : close the door")
        else:
            print("Elevator is moving........")