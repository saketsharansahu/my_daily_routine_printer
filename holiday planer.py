#holiday planer
print("=============================")
print("welcome to holiday picker")
print("=============================")

print("step 1 : pick your hoilday type")
print("1. beach")
print("2. mountain")

choice = int(input("enter 1 or 2"))
if choice == 1:
    print("step 2 : pick your beach activity")
    print("1. swimming ")
    print("2. sandcastle building")

    beach_activity = int(input("enter 1 or 2"))
    if beach_activity == 1:
        print("you have choosen swimming")
        print("best time : morning")
        print("remember : carry sunscreen and a water bottle")
    else:
        print("you have choose sandcastle building")
        print("best time : evening")
        print("remember : carry a bucket and a spade")
elif choice == 2:
    print("step 2 : pick your mountain activity")
    print("1. hiking")
    print("2. camping")

    mountain_activity = int(input("enter 1 or 2"))
    if mountain_activity == 1:
        print("you have choosen hiking")
        print("best for : exploring trails ")
        print("remember : wear comfortable shoes")
    else:
        print("you have chosen camping")
        print("best for : staying close to nature")
        print("remember : carry a tent and flashlight")

    