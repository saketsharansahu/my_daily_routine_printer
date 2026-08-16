# PART 1: Ask for today's temperature
temperature = int(input("enter today tempreture in celsius"))

#part 2 : decide between outdoor or indoor activity
if temperature < 20:
    activity = "indoor activity"
    print("todays tempreture is cold")
    print("do", activity)
else:
    activity = "outdoor acitivity"
    print("todays tempreture is warm")
    print("do", activity)

#part 3: ask if the weather is rainy
is_raining = input("is it raining (yes/no)")

if is_raining == "yes":
    print("do indoor activity or carry an umbrella")

#part 4 : ask for the homework time
homework_time = int(input("enter the homework time in minutes"))
if homework_time > 60:
    print("need a break")
    print("take a short break before", activity)
else:
    print("don't need a break")
    print("no long break is needed before", activity)

#part 5 : ask if they have free time today
free_time = input("do you have free time today (yes/no)")

if free_time == "yes":
    final_task = "hobby time"
    print("you have free time today")
    print("enjoy your", final_task)
else:
    final_task = "planning time"
    print("you do not have much free time today")
    print('use some time for', final_task)

#part 6: this message always print no matter what was choosen
print("daily activity check complete")

#part 7 : print the final acivity summary
print("DAILY ACTIVITY PLANER")
print("tempreture ->", temperature)
print("activity choosen ->", activity)
print("raining ->", is_raining)
print("study break needed ->",homework_time)
print("final task ->", final_task)