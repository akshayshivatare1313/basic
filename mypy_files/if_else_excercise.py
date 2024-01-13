# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# else:
#     print("Negative")
#
#
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
#
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# if a > b:
#     print("The first number is larger")
# else:
#     print("The second number is larger")
#


# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")
#
# num = int(input("Enter a number: "))
# if num == 0:
#     print("Zero")
# elif num > 0:
#     print("Positive")
# else:
#     print("Negative")
#
#
# a = int(input("Enter the length of side a: "))
# b = int(input("Enter the length of side b: "))
# c = int(input("Enter the length of side c: "))
# if a == b == c:
#     print("Equilateral triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")
#
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")
#
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# max_num = max(num1, num2, num3)
# print("The maximum number is:", max_num)
#
#
# char = input("Enter a character: ")
# if char.lower() in 'aeiou':
#     print("Vowel")
# else:
#     print("Consonant")



score = int(input("Enter your score: "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")
