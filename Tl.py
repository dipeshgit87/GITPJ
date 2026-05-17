light = input("Enter traffic light color: ").lower()

match light:

    case "red" :  print("Stop")
    case "yellow" : print("Slow Down")
    case "green" : print("Go")