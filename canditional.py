age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Responsible Adult")
else:
    print("Senior Citizen")

fruit = "Banana"
colour = input("Enter banana colour (yellow, brown, green): ").lower()

if fruit == "Banana":
    if colour == "yellow":
        print("Ripe")
    elif colour == "brown":
        print("Over Ripe")
    elif colour == "green":
        print("Unripe")
    else:
        print("Invalid colour")
else:
    print("Not a banana") 



