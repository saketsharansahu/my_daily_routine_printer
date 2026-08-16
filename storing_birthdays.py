#personal Goal Display

#Import the keybord module
import keyword

#create variables using valid python identifiers
person_name = input("Enter your name: ")
goal_name = input("enter your personal goal: ")
target_month = input("enter your target month:")
daily_minutes = 30

#print multiples values together
print("\nName:", person_name)
print("Goal:", goal_name)
print("Target Month:", target_month)
print("Daily practices", daily_minutes, "minutes")

#start new line using \n
print("\nMy personal goal plan\n")
print("goal status: ",  end= " ")
print("not started")

print("progress reminder: ", end= " - ")
print("practice everyday!")

#display the complete goal summary
print(
    "\n",
    person_name,
    "plans to work on",
    goal_name,
    "for",
    daily_minutes,
    "minutes everyday ",
)

#print python reseverd words
print("\nPython reseverd words are ...\n")
print(keyword.kwlist)




