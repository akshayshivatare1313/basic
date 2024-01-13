#################  1 Take values of length and breadth of a rectangle from user and check if it is square or not.

# analysis - to determine whether the given rectangle is square or not you need to compare the inputs from user
# which are length and breadth. if both are equal then the rectangle is square if not its a rectangle

# length = float(input('Enter the length of the rectangle :'))
# breadth = float(input('Enter the breadth of the rectangle :'))
#
# if length == breadth:
#     print("Its a sqaure")
# else:
#     print("Its a rectangle")


################ 2 Write a program to check whether a entered character is lowercase (a to z) or uppercase (A to Z)

# analysis - to determine whether the entered character from user is lowercase or uppercase  we can use the string methods
# called .islower() which checks charecter is lowercase and .isupper() checks if the character is uppercase.

# character = input("Enter the character :")
#
# if character.islower():
#     print("the entered character is lowercase")
# elif character.isupper():
#     print("the enterd character is uppercase")
# else:
#     print("the entered characcter is not letter")


############## 3 Write a program to get a number from the user and print whether it is positive or negative.

# analysis - to determine the entered number from user is positive or negative you can simply use if else condition
# for checking the numbers with 0


# number = float(input("Enter the number :"))

# if number > 0:
#     print("number is positve")
# elif number < 0:
#     print("number is Negative")
# else:
#     print("Number is Zero ")


########## 4 Write a program that reads a floating-point number and prints "zero" if the number is zero.
# Otherwise, print "positive" or "negative". Add "small" if the absolute value of the number is less than 1,
# or "large" if it exceeds 1,000,000.

# analysis - to determine the entered number from user is positive or negative you can simply use if else condition
# for checking the numbers with 0.
# we can use abs() function which is in built function to return the absolute value of number to deal with th condition
# less than 1 and large if exceeds 1000000

# number = float(input("Enter a number: "))
#
# if number > 0:
#     print("The entered number is positive.")
# elif number < 0:
#     print("The entered number is negative.")
# else:
#     print("The entered number is zero.")
#
# # Checking if it is small or large based on the absolute value
# if abs(number) < 1:
#     print("The absolute value of the number is small.")
# elif abs(number) > 1000000:
#     print("The absolute value of the number is large.")

########### 5 Write a program that takes a number from the user and generates an integer between 1 and 7.
# It displays the weekday name

#  random module used to generate a random integer between 1 and 7, mapping it to a
# predefined list of weekday names. The selected weekday name is then displayed to the user.
# This program demonstrates input handling, random number generation, and the practical use of lists for mapping

# import random
#
# user_number = int(input("Enter a number: "))
#
# random_day = random.randint(1, 7)
#
# weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# selected_day = weekday_names[random_day - 1]
#
# print(f"The weekday corresponding to {user_number} is {selected_day}.")


############# 6 Write a program that requires the user to enter a single character from the alphabet.
# Print Vowel or Consonant, depending on user input. If the user input is not a letter
# (between a and z or A and Z), or is a string of length > 1, print an error message.

# analysis - input a single character from the alphabet. It then determines whether the input is a vowel or a consonant
# and provides corresponding output. The program incorporates checks to handle non-letter inputs,such as digits or
# strings with lengths greater than one. If the user enters an invalid input, the program prints an error message.


# user_input = input("Enter a single character from the alphabet: ")
#
# if len(user_input) == 1 and user_input.isalpha():
#     char = user_input.lower()
#
#     if char in ['a', 'e', 'i', 'o', 'u']:
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("Error: Please enter a valid single character from the alphabet.")



############ 7 Write a program to display the cube of the given number up to an integer.

# analysis - The Python program takes a number from the user and displays the cubes of numbers up to that integer.
# Utilizing a for loop, it iterates from 1 to the user-input number, calculating and printing the cube of each iteration.

# user_number = int(input("Enter a number: "))
#
# for i in range(1, user_number + 1):
#     cube = i ** 3
#     print(f"The cube of {i} is: {cube}")


############# 8 Write a program that displays the sum of n odd natural numbers.

# analysis -
# the program prints the result, providing a simple and direct way to determine the sum of the
# specified odd natural numbers.


# n = int(input("Enter a value for n: "))
# sum_of_odd_numbers = n ** 2
# print(f"The sum of the first {n} odd natural numbers is: {sum_of_odd_numbers}")

########### 9 Write a program that accepts three numbers from the user and prints "increasing" if the numbers
# are in increasing order, "decreasing" if the numbers are in decreasing order, and "Neither increasing or d
# ecreasing order" otherwise.

# take inputs from the user. It then employs conditional if and elif statements to check the order of the numbers.
# If the numbers are in increasing order, it prints "Increasing"; if in decreasing order, it prints Decreasing.
# If neither condition is met, it prints Neither increasing nor decreasing order.

#
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
#
#
# if num1 < num2 < num3:
#     print("Increasing")
# elif num1 > num2 > num3:
#     print("Decreasing")
# else:
#     print("Neither increasing nor decreasing order")

########## 10 Write a program that prompts the user to enter three names.
# Your program should display the names in descending order.

# analysis -
# This Python program starts by using the input function to obtain three names from the user.
# The names are stored in a list, and the sort method is then applied with the reverse=True
# parameter to sort the list in descending order. Finally, the program prints the names in descending order


# name1 = input("Enter the first name: ")
# name2 = input("Enter the second name: ")
# name3 = input("Enter the third name: ")
#
# names_list = [name1, name2, name3]
# names_list.sort(reverse=True)
#
# print("Names in descending order:", names_list)


##########
# 11 Write a program to calculate the monthly telephone bills as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.

# analysis
# This Python program begins by taking input from the user for the number of calls. It then calculates the total bill
# based on the provided rules, including the minimum charge for up to 100 calls, additional charges for the next
# 50 calls at different rates, and additional charges for any call beyond 200. The result is displayed as the monthly
# telephone bill.

# num_calls = int(input("Enter the number of calls: "))
#
# minimum_charge = 200
#
# charge_per_call_50_1 = 0.60
# num_calls_50_1 = min(num_calls - 100, 50)  # Calculate calls within the first 50
#
# charge_per_call_50_2 = 0.50
# num_calls_50_2 = max(min(num_calls - 150, 50), 0)
#
# charge_per_call_beyond_200 = 0.40
# num_calls_beyond_200 = max(num_calls - 200, 0)
#
# total_bill = minimum_charge + (charge_per_call_50_1 * num_calls_50_1) + \
#               (charge_per_call_50_2 * num_calls_50_2) + (charge_per_call_beyond_200 * num_calls_beyond_200)
#
# print(f"The monthly telephone bill is: Rs. {total_bill:.2f}")


############ 12 Write a program to determine whether the year is a leap year or not.

# analysis -
# This Python program starts by taking input from the user for the year.
# It then uses conditional statements to check whether the year is a leap year .
# If the year is divisible by 4 and not divisible by 100, or If the year is divisible by 400
# f the conditions are met, the program prints that the given year is a leap year; otherwise,
# it indicates that it is not a leap year.


# year = int(input("Enter a year: "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

######## 13 Write a program that asks the user to enter 3 numbers in three variables and then displays the largest number.

# analysis -
# This Python program starts by using the input function to obtain three numerical inputs from the user.
# It then uses the max function to find the largest number among the three provided.
# Finally, the program prints the result, indicating the largest number among the user-input values.


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
#
# largest_number = max(num1, num2, num3)
#
# print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_number}")

############
# analysis -
# This Python program begins by using the input function to obtain a numerical input from the user.
# then checks whether the entered number is even or odd using the modulo operator (%).
# If the remainder when dividing by 2 is zero, the number is even; otherwise, it is odd.
# The program prints the result, indicating whether the entered number is even or odd.


# user_number = int(input("Enter a number: "))
#
# if user_number % 2 == 0:
#     print(f"{user_number} is an even number.")
# else:
#     print(f"{user_number} is an odd number.")


######### 15 A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

# analysis - This Python program begins by using the input function to obtain the number of classes held and the
# number of classes attended from the user. It then calculates the attendance percentage based on the provided inputs.
# The program then checks if the calculated attendance percentage is greater than or equal to 75%. If so,
# it prints that the student is allowed to sit in the exam; otherwise, it indicates that the student is not allowed due
# to low attendance.


# classes_held = int(input("Enter the number of classes held: "))
# classes_attended = int(input("Enter the number of classes attended: "))
#
# attendance_percentage = (classes_attended / classes_held) * 100
#
# print(f"Percentage of classes attended: {attendance_percentage:}%")
#
# if attendance_percentage >= 75:
#     print("The student is allowed to sit in the exam.")
# else:
#     print("The student is not allowed to sit in the exam due to low attendance.")


########## 16 A school has following rules for grading system:

# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# analysis - This Python program starts by using the input function to obtain marks from the user. It then uses
# a series of if and elif statements to check the provided conditions for each grade and determine the
# corresponding grade based on the user's input. Finally, the program prints the result, displaying the grade
# corresponding to the entered marks.

# marks = float(input("Enter the marks: "))
#
# if marks < 25:
#     grade = 'F'
# elif 25 <= marks < 45:
#     grade = 'E'
# elif 45 <= marks < 50:
#     grade = 'D'
# elif 50 <= marks < 60:
#     grade = 'C'
# elif 60 <= marks < 80:
#     grade = 'B'
# else:
#     grade = 'A'
#
# print(f"The corresponding grade for {marks} marks is: {grade}")

######## 17 A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

# analysis -
# This Python program begins by using the input function to obtain the user's salary and years of service.
# It then checks if the years of service are more than 5. If so, it calculates the bonus amount based on a
# 5% bonus percentage and prints a message indicating eligibility along with the net bonus amount.
# If the years of service are not more than 5, it informs the user that they are not eligible for a bonus.


# salary = float(input("Enter your salary: "))
# years_of_service = int(input("Enter your years of service: "))
#
# if years_of_service > 5:
#     bonus_percentage = 5
#     bonus_amount = (bonus_percentage / 100) * salary
#     print(f"Congratulations! You are eligible for a {bonus_percentage}% bonus.")
#     print(f"Net bonus amount: {bonus_amount:}")
# else:
#     print("Sorry, you are not eligible for a bonus.")

########### 18 Create a program to check if a number is a perfect number

########## 19 Implement a program to reverse a string without using built-in functions.

# analysis - # Analysis:
# This Python program defines a function reverse_string that takes a string as input and returns the reversed string.
# It uses a loop to iterate through each character of the input string, building the reversed string by adding each
# character to the beginning of the result string. The main part of the program takes input from the user,
# calls the function to reverse the entered string, and prints the result.

# def reverse_string(input_string):
#     reversed_string = ""
#     for char in input_string:
#         reversed_string = char + reversed_string
#     return reversed_string
#
# user_string = input("Enter a string: ")
# result = reverse_string(user_string)
#
# print(f"The reversed string is: {result}")

########## 20 Develop a program to perform matrix multiplication.

######### 22 Create a program to calculate the average of N numbers.
# analysis -This Python program takes input from the user for the number of values (N) and then takes input for N numbers.
# It calculates the sum of the entered values and the count of numbers. Finally, it calculates and prints the average i
# f at least one value is entered.

# N = int(input("Enter the number of values (N): "))
# sum_values = 0
# count = 0
#
# print("Enter the values:")
# for _ in range(N):
#     value = float(input())
#     sum_values += value
#     count += 1
#
# if count > 0:
#     average = sum_values / count
#     print(f"The average of the {N} numbers is: {average:.2f}")
# else:
#     print("No values entered. Cannot calculate the average.")
#

######## 23 Create a program to check if a number is a power of two.

# analysis -
# This Python program starts by using the input function to obtain a numerical input from the user.
# It then checks if the entered number is a power of two using a bitwise operation. If (number & (number - 1))
# is equal to 0 and the number is not 0, then the program prints that the number is a power of two; otherwise,
# it indicates that it is not a power of two.


# number = int(input("Enter a number: "))
#
# if (number & (number - 1)) == 0 and number != 0:
#     print(f"{number} is a power of two.")
# else:
#     print(f"{number} is not a power of two.")

###### 24 Create a program to calculate the compound interest.

# analysis - This Python program takes input from the user for the principal amount, rate of interest (in percentage),
# and time in years. It then calculates the compound interest using the formula

# principal = float(input("Enter the principal amount: "))
# rate_of_interest = float(input("Enter the rate of interest (in percentage): "))
# time = float(input("Enter the time in years: "))
#
# compound_interest = principal * (1 + rate_of_interest / 100) ** time - principal
#
# print(f"The compound interest is: {compound_interest:}")


######## 25 Implement a program to find the reverse of a given number.

# analysis - This Python program takes input from the user for a number and then uses a while loop to reverse the digits
# of the number. Inside the loop, it extracts the last digit of the number, adds it to the reversed number after
# multiplying it by 10, and then removes the last digit from the original number. The loop continues until the
# original number becomes 0. The result is then displayed as the reversed number.

# number = int(input("Enter a number: "))
#
# reversed_number = 0
#
# while number > 0:
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit
#     number = number // 10
#
# print(f"The reverse of the given number is: {reversed_number}")

###### 26 Write a Java program to check if a given number, is a strong number.

###### 27 Implement a program to calculate simple interest.

# analysis - This Python program takes input from the user for the principal amount, rate of interest (in percentage),
# and time in years. It then calculates the simple interest using the formula of simple interest

#
# principal = float(input("Enter the principal amount: "))
# rate_of_interest = float(input("Enter the rate of interest (in percentage): "))
# time = float(input("Enter the time in years: "))
#
# simple_interest = (principal * rate_of_interest * time) / 100
#
# print(f"The simple interest is: {simple_interest:}")

######### 28 Create a program to simulate a simple calculator with basic operations.


# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# def multiply(x, y):
#     return x * y
#
#
# def divide(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Cannot divide by zero"
#
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
#
# print("\nSelect operation:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
#
# choice = input("Enter choice (1, 2, 3, or 4): ")
#
# if choice == '1':
#     result = add(num1, num2)
#     operation = "Addition"
# elif choice == '2':
#     result = subtract(num1, num2)
#     operation = "Subtraction"
# elif choice == '3':
#     result = multiply(num1, num2)
#     operation = "Multiplication"
# elif choice == '4':
#     result = divide(num1, num2)
#     operation = "Division"
# else:
#     result = "Invalid input"
#     operation = "Unknown"
#
# print(f"{operation} result: {result}")

####### 29 Implement a program to check if a given number, is a perfect square.

# analysis - This Python program starts by using the input function to obtain a numerical input from the user.
# It then checks if the entered number is greater than 0 and if the square root of the number is an integer.
# If both conditions are true, it prints that the number is a perfect square otherwise, it indicates that
# it is not a perfect square.


# number = float(input("Enter a number: "))
#
# if number > 0 and (number**0.5).is_integer():
#     print(f"{number} is a perfect square.")
# else:
#     print(f"{number} is not a perfect square.")

######## 30 Develop a program to find the smallest among three numbers.

# analysis - This Python program starts by using the input function to obtain three numerical inputs from the user.
# It then uses the min function to find the smallest number among the three provided.
# Finally, the program prints the result, indicating the smallest number among the user-input values.

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
#
#
# smallest_number = min(num1, num2, num3)
#
# print(f"The smallest number among {num1}, {num2}, and {num3} is: {smallest_number}")

####### 31 Write a program to check if a number is an Armstrong number.

# # analysis -
# # This Python program defines a function is_armstrong to check if a number is an Armstrong number.
# # The program then takes input from the user for a number and calls the is_armstrong function to determine
# # if it's an Armstrong number. The code checks if the sum of each digit raised to the power of the number of
# # digits is equal to the original number. If it is, the number is an Armstrong number; otherwise, it is not.
# # The program then prints the result.
#
#
# def is_armstrong(number):
#     num_digits = len(str(number))
#     temp = number
#     sum_of_digits = 0
#
#     while temp > 0:
#         digit = temp % 10
#         sum_of_digits += digit ** num_digits
#         temp //= 10
#
#     return sum_of_digits == number
#
# number = int(input("Enter a number: "))
#
# if is_armstrong(number):
#     print(f"{number} is an Armstrong number.")
# else:
#     print(f"{number} is not an Armstrong number.")
#
# ########## 32 Create a program to calculate the area of different geometric shapes (circle, rectangle, triangle).
#
# import math
# def circle_area(radius):
#     return math.pi * radius**2
#
# def rectangle_area(length, width):
#     return length * width
#
# def triangle_area(base, height):
#     return 0.5 * base * height
#
# print("Select a geometric shape:")
# print("1. Circle")
# print("2. Rectangle")
# print("3. Triangle")
#
# choice = input("Enter choice (1, 2, or 3): ")
#
# if choice == '1':
#     radius = float(input("Enter the radius of the circle: "))
#     area = circle_area(radius)
#     shape = "Circle"
# elif choice == '2':
#     length = float(input("Enter the length of the rectangle: "))
#     width = float(input("Enter the width of the rectangle: "))
#     area = rectangle_area(length, width)
#     shape = "Rectangle"
# elif choice == '3':
#     base = float(input("Enter the base of the triangle: "))
#     height = float(input("Enter the height of the triangle: "))
#     area = triangle_area(base, height)
#     shape = "Triangle"
# else:
#     area = "Invalid input"
#     shape = "Unknown"
#
# print(f"\nThe area of the {shape} is: {area:.2f}")


########## 33 Write a program to convert temperature from Celsius to Fahrenheit and vice versa.

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
#
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9
#
# print("Select temperature conversion:")
# print("1. Celsius to Fahrenheit")
# print("2. Fahrenheit to Celsius")
#
# choice = input("Enter choice (1 or 2): ")
#
#
# if choice == '1':
#     celsius_value = float(input("Enter temperature in Celsius: "))
#     converted_temperature = celsius_to_fahrenheit(celsius_value)
#     print(f"{celsius_value} Celsius is equal to {converted_temperature:.2f} Fahrenheit.")
# elif choice == '2':
#     fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
#     converted_temperature = fahrenheit_to_celsius(fahrenheit_value)
#     print(f"{fahrenheit_value} Fahrenheit is equal to {converted_temperature:.2f} Celsius.")
# else:
#     print("Invalid input. Please choose 1 or 2.")

####### 34 Create a program to determine if a number is prime.

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# number = int(input("Enter a number: "))
#
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

########## 35 Develop a program to find the roots of a quadratic equation.

########## 36 Given two strings, write a program to determine whether they are anagrams.

# Function to check if two strings are anagrams
# def are_anagrams(str1, str2):
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
#     return sorted(str1) == sorted(str2)
#
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
#
# if are_anagrams(string1, string2):
#     print(f"{string1} and {string2} are anagrams.")
# else:
#     print(f"{string1} and {string2} are not anagrams.")

######### 37 Create a program to calculate the sum of digits of a given number.#

# def sum_of_digits(number):
#     return sum(int(digit) for digit in str(abs(number)))
#
# number = int(input("Enter a number: "))
#
# result = sum_of_digits(number)
#
# print(f"The sum of digits of {abs(number)} is: {result}")

######### 38 Implement a program to find the LCM of two numbers
#
# def find_gcd(x, y):
#     while(y):
#         x, y = y, x % y
#     return x
#
# def find_lcm(x, y):
#     return (x * y) // find_gcd(x, y)
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# lcm = find_lcm(num1, num2)
#
# print(f"The LCM of {num1} and {num2} is: {lcm}")

######### 39 Write a program to find the prime factors of a number.
# def prime_factors(n):
#     factors = []
#     divisor = 2
#
#     while divisor <= n:
#         if n % divisor == 0:
#             factors.append(divisor)
#             n //= divisor
#         else:
#             divisor += 1
#
#     return factors
#
# number = int(input("Enter a number: "))
#
# factors = prime_factors(number)
#
# if len(factors) > 0:
#     print(f"The prime factors of {number} are: {', '.join(map(str, factors))}")
# else:
#     print(f"{number} has no prime factors other than 1.")
#

########## 40 Create a program to check if a number is a power of two

# def is_power_of_two(number):
#     return number > 0 and (number & (number - 1)) == 0
#
# number = int(input("Enter a number: "))
#
# if is_power_of_two(number):
#     print(f"{number} is a power of two.")
# else:
#     print(f"{number} is not a power of two.")

######### 41 Develop a program to check if a number is an abundant number.

# Function to find the sum of divisors of a number
# def sum_of_divisors(number):
#     return sum(i for i in range(1, number) if number % i == 0)
#
# def is_abundant_number(number):
#     return sum_of_divisors(number) > number
#
# number = int(input("Enter a number: "))
#
# if is_abundant_number(number):
#     print(f"{number} is an abundant number.")
# else:
#     print(f"{number} is not an abundant number.")

########## 42 Write a Java program to calculate the perimeter of a square.

########## 43 A triangle is valid if the sum of all the three angles is equal to 180 degrees.
# Write a program that asks the user to enter three integers as angles and check whether a triangle is valid or not.
# Function to check if the given angles form a valid triangle

def is_valid_triangle(angle1, angle2, angle3):
    return angle1 + angle2 + angle3 == 180

angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

if is_valid_triangle(angle1, angle2, angle3):
    print("The angles form a valid triangle.")
else:
    print("The angles do not form a valid triangle.")


