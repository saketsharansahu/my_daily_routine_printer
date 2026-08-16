# Library Visit Planner

print("=== Library Visit Planner ===")
print("Answer 3 quick questions and I will plan your library visit!\n")

day       = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather   = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
book_due  = input("Do you have a book to return? (yes / no): ").strip().lower()

print()
print(f"your library plan for", day)
print("-", * 35)

if day in ("saturday, sunday"):
    print("day type : weekend - a good time for relaxed library vist")
elif day == "monday":
    print("dau type : start of the week - check your reading list")
elif day == "friday":
    print("day type : last school date - return books before weekend")
elif day in ("tuesday, wednesday, thursday"):
    print("day type : regular school day - plan a short libray visit")
else:
    print("day type : day type not recognised please check the spelling")
    




