a = int(input("son kiriting : "))
sum = 1
for i in range(1, a+1):
    print(i, end=" ")
    sum *= i
print()
print(f"The Multiply is : {sum}")