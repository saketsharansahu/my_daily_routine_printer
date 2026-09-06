#homework completion tracker

total_homework = 4
original_homework = total_homework
print(f"you have {original_homework} homework to complete")

completed_count = 0
task_num = 1

while task_num <= total_homework:

    if task_num == 1:
        next_task = "math worksheet"
    elif task_num == 2:
        next_task = "science reading"
    elif task_num == 3:
        next_task = "english writing"
    else:
        next_task = "coding practice"

    answer = input(f"have you completed your {next_task}? (yes/no): ")
    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("great job ! homework task completed.")
    else:
        print("okay, finish it and check it again.")
        
    print("homework task remaining:", total_homework - completed_count)
    print()

print("=== All homework tasks completed! Well done! ===")
print("great job finishing your homework today!")

print("now lets lets safely peek at an infinite loop...")
test_value =0
safty_counter = 0

while test_value <= 0:
    print("this statement will run forever unless we break it")
    safty_counter += 1

    if safty_counter == 10:
        print("breaking the infinite loop...")
        break

print("\n===homework completion summary===\n")
print("homework assigned:", original_homework)
print("homework completed:", completed_count)
print("homework remaining:", total_homework - completed_count)
print("======================================")