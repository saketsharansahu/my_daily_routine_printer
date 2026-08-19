# Library Visit Planner

print("=== Library Visit Planner ===")
print("Answer 3 quick questions and I will plan your library visit!\n")

day       = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather   = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
book_due  = input("Do you have a book to return? (yes / no): ").strip().lower()

print()
print(f"your library plan for", day)

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

#part 2 : AND OPERATOR - sunny AND book due
if weather == "sunny" and book_due =="yes":
    print("Libray tip : great weather. return your book and borrow a new one")

if weather == "cloudy" or weather == "rainy":
    print("Weather tip : carry an umbrella if you are going to the school")

if not (book_due == "yes"):
    print("Book status : no book return needed. You can browse new books")

if weather == "rainy" and book_due == "yes":
    print("Best plan : visit the libray carefully and return your books on time") 
elif weather == "sunny" and book_due == "yes" and not (day in("saturday", "sunday")):
    print("Best plan : stop by the libray after school and return the books in time")
elif day in ("saturday", "sunday") and weather == "sunny":
    print("Best plan : perfect day for a longer reading session in libray")
else:
    print("Best plan : check your schedule and plan a simple libray visit")

print()
print("Libray plan complete . Happy reading !")







