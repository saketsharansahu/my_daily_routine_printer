#loop art designer
print("====star pyramid pattern designer====")

rows = int(input("enter the number of rows for the star pyramid: "))
for i in range(rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("====floydes triangle pattern designer====")
n = int(input("enter the number of rows for floydes triangle: "))
num = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num = num + 1
    print()

print("====diamond pattern designer====")

row_size = int(input("enter the number of rows for diamond pattern: "))

if row_size % 2 == 0:
    half_rows = row_size // 2
else:
    half_rows = row_size // 2 + 1

space = half_rows - 1

for i in range(1, half_rows + 1):
    for j in range(1, space + 1):
        print(" ", end="")
    space -= 1
    number = 1
    for j in range(2 * i -1):
        print(number, end="")
        number += 1
    print()

space = 1

for i in range(1, half_rows):
    for j in range(1, space + 1):
        print(" ", end="")

    space += 1
    number = 1

    for j in range(2 * (half_rows - i) - 1):
        print(number, end="")
        number += 1

    print()

print("loop art design completed")
print("you created a star pyramid, floydes triangle and diamond pattern using nested loops")
        
    
 