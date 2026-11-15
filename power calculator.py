print("power calculator")

base = int(input("enter the base number: "))
exponent = int(input("enter the exponent: "))

for i in range(1, exponent + 1):
    result = base ** i

    print(base, "raised to the power of", i, "is:", result)

result = base ** exponent

print(base, "raised to the power of", exponent, "is:", result)
print("thank you for using the power calculator!")
