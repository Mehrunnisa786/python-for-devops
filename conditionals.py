day_of_week = input("Enter day of week: ",).lower() #Converting to lower letters
print(day_of_week)

day_of_week = input("Enter day of week: ").upper()
print(day_of_week)
num1 = int(input("Enter First number: ")) #str -->int type casting
num2 = int(input("Enter Second Number: "))

if day_of_week == "sunday" or day_of_week == "saturday":
    print("I will learn Devops")
else:
    print("I will practice DevOps")

choice = input("Enter the choice of operation: +, *, %, -, /: ")
if choice == "+":
    sum_of_num = num1 + num2
    print("Addition: ",sum_of_num)

elif choice == "-":
    diff_of_num = num1 - num2
    print("Substraction: ",diff_of_num)

elif choice == "*":
    product_of_num = num1 * num2
    print("Product: ",product_of_num)

elif choice == "/":
    div_of_num = num1 / num2
    print("Division: ",div_of_num)

elif choice == "%":
    mod_of_num = num1 % num2
    print("Remainder: ",mod_of_num)
else:
    print("Invalid")
