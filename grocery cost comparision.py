#grocery cost comparision

rice_price = 12
milk_price = 4
fruit_price = 8
number_of_basket = 2
family_member = 4

basket_cost_price_per_person = (rice_price + milk_price + fruit_price * number_of_basket / family_member)

print("grocory cost per person:", basket_cost_price_per_person)

total_item = int(input("\nenter the total number of grocery item "))

people = int(input("enter the number of family member"))

if total_item % people == 0:
    print(
        total_item,
        "items can be divided into",
        people,
        "people"
    )
else:
    print(
        total_item,
        "items cannot be divided into",
        people,
        "people"
    )

recored_average = 65
wrong_week_cost = 50
correct_week_cost = 80
total_weeks = 4

recored_total = recored_average * total_weeks

print("\n recorded total is:", recored_total)

corrected_total = (recored_total - wrong_week_cost + correct_week_cost)

corrected_avrage = (corrected_total/total_weeks)

print("corrected weekly total:", corrected_total)

store_a_avarage = 70
store_b_avarage = 75
store_c_avarage = 80

print("store a average:", store_a_avarage)
print("store b avarage:", store_b_avarage)
print("store c avarage:", store_c_avarage)

if(
    corrected_avrage < store_a_avarage and
    corrected_avrage < store_b_avarage and
    corrected_avrage < store_c_avarage
):
    print("your corrected avrage is lower than all three stores avrages")
elif(
    corrected_avrage > store_a_avarage and
    corrected_avrage > store_b_avarage and
    corrected_avrage > store_c_avarage
):
    print("your corrected avrage is higher than all three store avrages")
else:
    print("your correted grocery is between the three store avarage")

