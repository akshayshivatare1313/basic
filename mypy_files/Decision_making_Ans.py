# Task: 1;Simple Conditional Statements
# Description: Ask students to write a Python program that takes an input from the user
# and determines if it is an even number or an odd number.

# requirements:
#     * single input is must accepted from user which is his/her Number.
#     * building a logic that is to find the entered number is even or odd.
#     * the number is even when its modulus is ZERO and if its NON ZERO or ONE then its Odd number


# num = int(input('Enter the Number :'))
# if num % 2 == 0:
#     print('Entered Number is Even')
# else:
#     print('Entered Number is Odd')


# Task:2; Multiple Conditional Statements
# Description: Have students create a program that prompts the user to enter their age.
# Based on the input, the program should display different messages according to the following conditions:
# If age is less than 18: "You are a minor."
# If age is between 18 and 65: "You are an adult."
# If age is 65 or older: "You are a senior citizen."

# Requirements:
#     * Accept a single input from the user, representing their age.
#     * Implement logic to determine the appropriate message based on the age.
#     * Display the corresponding message according to the specified conditions.

# age = int(input('Enter your age :'))
#
# if age < 18:
#     print('You are a minor.')
# elif 18 <= age < 65:
#     print('You are an adult.')
# else:
#     print('You are a senior citizen.')

# Task:3 ; Nested Conditional Statements
# Description: In this task, students should develop a program that calculates the discount amount for
#               a shopping cart based on the following conditions:
# If the total price is greater than or equal to $100, apply a 10% discount.
# If the total price is between $50 and $99.99, apply a 5% discount.
# If the total price is less than $50, no discount is applied.


# Requirements:
    #     * Accept a single input from the user, representing the total price of the shopping cart.
    #     * Implement nested conditional statements to calculate and display the discount amount.
    #     * Display the original total price, the discount amount (if any), and the final discounted price.


# total_price = float(input('Enter total amount :'))
#
# if total_price >= 100:
#     discount = total_price / 100 * 10
#     print('you have got 10% discount!! discount amount is :', discount)
# else:
#     if 50 <= total_price < 100:
#         discount = total_price / 100 * 5
#         print('you have got 5% discount!! discount amount is :', discount)
#     else:
#         discount = 0
#         print('No discount for you!')


# Task:5; Decision Making with Loops
# Description: Have students create a program that generates a random number between 1 and 100.
#         The user should guess the number, and the program should provide feedback on whether the guess is too high or too low.
#         The program should continue until the user guesses the correct number.

# Requirements:
#     * Implement proper validation for user input (e.g., non-numeric input).
#     * Generate a random number between 1 and 100.
#     * Use a loop to allow the user to make multiple guesses until they guess the correct number.
#     * Prompt the user to input their guess for the number.Provide feedback on whether the guess is too high, too low, or correct.
#     * Continue the loop until the user guesses the correct number.Display the number of attempts it took for the user to guess correctly.


# target_num = int(input('enter the number :'))
# # attempts  = 0
# user_guess = None
#
# while user_guess != target_num:
#     user_input = int(input('Enter your guess between 0 to 100 :'))
#     if user_input < target_num:
#         print('too low!!')
#     elif user_input > target_num:
#         print('too high!!')
#     else:
#         print('You have guessed Correct Number!! its :',target_num )
#         break

# Task :6 ;Calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
# Requirements:
#     * Accept three input numbers from the user.
#     * Calculate the sum of the three numbers.
#     * If the three numbers are equal, return thrice of their sum.
#     * Display the calculated sum or thrice of the sum, as appropriate.

# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter second number :"))
# num3 = int(input("Enter third number :"))
#
# sum_of_numbers = num1 + num2 + num3
#
# if num1 == num2 == num3:
#     result = sum_of_numbers * 3
#     print('thrice of numbers sum is :', result)
# else:
#     print('number sum is :', sum_of_numbers)


# Task : 7:  Python program to test whether a number is within 100 or 1000 or 2000.
# Requirements:
#     * Accept a single input number from the user.
#     * Test whether the given number is within 100 units of either 1000 or 2000.
#     * Display a message indicating whether the number is within the specified range or not.


# num = int(input('Enter the number :'))
#
# if num <= 100:
#     print('number is within 100 units')
# elif 100 < num <= 1000:
#     print('number is within 1000 units')
# elif 1000 < num <= 2000:
#     print('number is within 2000 units')
# else:
#     print('number is not within range of 100 units of either 1000 or 2000.')

# Task : 8 ; Python program to count the number 4 in a given list.

# Requirements:
#     * Create a list of numbers .
#     * Count the number of occurrences of the value 4 in the given list.
#     * Display the count of occurrences.

# user_ele = int(input('Enter no of Elements in the list :'))
# # lst = [3, 1, 9, 4, 5, 7, 4, 6, 8, 10, 4]
# user_list = []
# for i in range(user_ele):
#     elem = int(input('enter element :'))
#     user_list.append(elem)
# # count_of_4 = lst.count(4)
# count_of_4 = user_list.count(4)
# print('the number of occurances of the value 4 are :', count_of_4)


# Task : 9 ; Python program to test whether a passed letter is a vowel or not.

# Requirements:
#     * Accept a single letter as input from the user.
#     * Test whether the passed letter is a vowel (either uppercase or lowercase).
#     * Display a message indicating whether the letter is a vowel or not.

# user_letter = input('Enter a single letter :')
#
# if user_letter.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print('entered letter', user_letter, ' is a Vowel.')
# else:
#     print('entered letter', user_letter, ' is a Not Vowel.')


# Task 10: Voting Eligibility
# Description: Write a program that prompts the user to enter their age and determines if they are eligible to vote or not.
# Example Input: 21
# Example Output: "You are eligible to vote."

# Requirements:
#     * Accept a single input from the user, representing their age.
#     * Check if the user's age is eligible for voting.
#     * Display a message indicating whether the user is eligible to vote or not.


# user_age = int(input('Enter your Age :'))
#
# if user_age >= 18:
#     print('You are eligible to vote')
# else:
#     print('You are not eligible to vote')

# Task 11: Leap Year Checker
# Description: Create a program that checks if a given year is a leap year or not.
# Example Input: 2024
# Example Output: "2024 is a leap year."

# Requirements:
#     * Accept a single input from the user, representing the year.
#     * Check if the given year is a leap year.
#     * Display a message indicating whether the year is a leap year or not.

# user_year = int(input('Enter a year :'))
# if user_year % 4 == 0 and user_year % 100 != 0 or user_year % 400 == 0:
#     print('Entered year is leap year')
# else:
#     print('Entered year in not leap year')

# Task 12: Grade Calculator
# Description: Develop a program that accepts a student's score as input and returns their corresponding grade
# according to a grading scale.
# Example Input: 87
# Example Output: "Your grade is B."

# Requirements:
#     * Accept a single input from the user which is valid, representing the student's score.
#     * Determine the corresponding grade based on a predefined grading scale.
#     * Display a message indicating the student's grade.

# Grading Scale just for the reference:
#     * A: 90-100
#     * B: 80-89
#     * C: 70-79
#     * D: 60-69
#     * E: 50-59
#     * F: 0-49


# user_score = float(input('Enter your Score :'))

# if 0 <= user_score <= 100:
#     if 90 <= user_score <= 100:
#         grade = 'A'
#     elif 80 <= user_score < 90:
#         grade = 'B'
#     elif 70 <= user_score < 80:
#         grade = 'C'
#     elif 60 <= user_score < 70:
#         grade = 'D'
#     elif 50 <= user_score < 60:
#         grade = 'E'
#     else:
#         grade = "Failed!!"
#     print('Your grade is :', grade)
# else:
#     print('Enter valid Score!!')

# Task 13: BMI Calculator
# Description: Create a program that calculates a person's Body Mass Index (BMI) based on their height and weight.
# Example Input: Height = 1.75m, Weight = 68kg
# Example Output: "Your BMI is 22.2."
# Requirements:
#     * Accept two inputs from the user, representing their height (in meters) and weight (in kilograms).
#     * Calculate the BMI using the formula: BMI = weight / (height^2)
#     * Display a message indicating the calculated BMI.

#     height = float(input('Enter your height in meters :'))
#     if height > 0:
#         break
#     else:
#         print("Enter Valid Value for Height")
#
# while True:
#     weight = float(input('Enter your weight in Kilograms :'))
#     if weight > 0:
#         break
#     else:
#         print("Enter Valid Value for weight")
#
# bmi = weight / (height ** 2)
# print('Your body mass index is :', bmi)
#
# print('enter valid information')



# Task 14: Data Validation
# Description: Develop a program that validates user input to ensure it meets specific criteria (e.g., length, format).
# Example Input: "abc123"
# Example Output: "The input is valid."while True:

 # Requirements:
#     * Accept input from the user.
#     * Validate the input to ensure it meets specific criteria (e.g., length, format).
#     * Display a message indicating whether the input is valid or not.

# user_input = input("Enter your input: ")
#
#
# if len(user_input) > 5 and user_input.isalnum():
#     print("The input is valid.")
# else:
#     print("The input is not valid. Please enter a string with length greater than 5 characters and alphanumeric format.")

# Task 15: Temperature Converter
# Description: Write a program that converts a given temperature from Celsius to Fahrenheit or vice versa.
# Example Input: 32°F
# Example Output: "0°C"

# Requirements:
#     * Accept input from the user, representing a temperature with a specified unit (e.g., "32°F" or "0°C").
#     * Determine the unit of the input temperature (Celsius or Fahrenheit).
#     * Convert the temperature to the other unit using the appropriate conversion formula.
#     * Display the converted temperature in the opposite unit.

# temp_input = input('Enter the temperature value in Celcius or Fahrenheit :')
# temp_value = float(temp_input[:-1])
# temp_unit = temp_input[-1]
# converted_temp = None
# converted_unit = None
#
# if temp_unit.lower() == 'c':
#     converted_temp = (temp_value * 9/5) + 32
#     converted_unit = 'F'
#     print('The converted temperature is :', converted_temp, converted_unit)
# elif temp_unit.lower() == 'f':
#     converted_temp = (temp_value - 32) * 5/9
#     converted_unit = 'C'
#     print('The converted temperature is :', converted_temp, converted_unit)
#
# else:
#     print('Invalid input!, please! Enter the temperature value in Celcius or Fahrenheit !! ')

# Task 16: User Authentication
# Description: Create a program that verifies a user's login credentials (e.g., username and password).
# Example Input: Username = "john_doe", Password = "pass123"
# Example Output: "Login successful."

# Requirements:
#     * Define valid username and password.
#     * Accept input from the user for both username and password.
#     * Check if the entered username and password match the predefined valid credentials.
#     * Display a message indicating whether the login was successful or not.


# username = "akshay_shiv"
# password = "Pass123"
#
# input_username = input('enter your username :')
# input_password = input('enter your password :')
#
# if input_username == username and input_password == password:
#     print('Login Successfull!!')
# else:
#     print("Login failed!! Please check your username and password.")


# Task 17: String Manipulation
# Description: Develop a program that performs different operations on a given string based on user input
#               (e.g., length, reverse, uppercase).
# Example Input: "Hello, World!"
# Example Output: "The string has 13 characters."

# Requirements:
#     * Accept input from the user, representing a string.
#     * Provide a menu for the user to choose from different string operations (e.g., length, reverse, uppercase).
#     * Implement logic to perform the selected string operation.
#     * Display the result of the chosen operation.

# input_sring = input('Enter a String :')
#
# print('Menu')
# print('1. Length')
# print('2. Reverse')
# print('3. Uppercase')
#
# choice = input('Enter your choice (1/2/3) :')
#
# if choice == "1":
#     result = 'Length of string is', len(input_sring)
# elif choice == "2":
#     result = 'Reverse string is', input_sring[::-1]
# elif choice == "3":
#     result = 'Uppercase string is', input_sring.upper()
# else:
#     result ='Invalid choice!! Please enter choice as 1, 2 or 3'
# print(result)

# Task 18: Discount Calculator
# Description: Create a program that calculates the final price of a product after applying a discount.
# Example Input: Original price = $100, Discount percentage = 20%
# Example Output: "The final price is $80.

# Requirements:
#     * Accept input from the user for the original price of the product and the discount percentage.
#     * Calculate the final price after applying the discount.
#     * Display the final price.


# original_price = float(input('Enter the original price of the product :'))
# discount_percentage = float(input('Enter the discount percentage :'))
#
# discount_price = (discount_percentage / 100) * original_price
# final_prize = original_price - discount_price
#
# print('final price is :', final_prize)

# Task 19: Email Validation
# Description: Create a program that validates if a given email address is correctly formatted.
# Example Input: "john.doe@example.com"
# Example Output: "The email address is valid."

# Requirements:
#     * Accept input from the user for an email address.
#     * Implement logic to check if the entered email address is correctly formatted.
#     * Display a message indicating whether the email address is valid or not.

# email_address = input('Enter an email address :')
# if '@' in email_address and '.' in email_address:
#     print('Email is valid.')
# else:
#     print('Email is not valid, Please! enter correct format.')


# Task 20: Number System Converter
# Description: Develop a program that converts a given number from one number system to another
#               (e.g., binary to decimal).
# Example Input: Binary number = "10101"
# Example Output: "The decimal equivalent is 21."

# Requirements:
#     * Accept input from the user for a binary number .
#     * Implement logic to convert the given number to the target number system (e.g., binary to decimal).
#     * Display the result of the conversion.

# binary_number = input('Enter binary number :')
# if not all(bit in '01' for bit in binary_number):
#     print('Invalid binary number, please enter valid binary number.')
# else:
#     decimal_equi = int(binary_number, 2)
#     print('Decimal equivalrnt of binary is :', decimal_equi)

# Task 21: Rock, Paper, Scissors Game
# Description: Write a program that allows two players to play the classic game of rock, paper, scissors
#               and determines the winner.
# Example Input: Player 1: "rock", Player 2: "scissors"
# Example Output: "Player 1 wins!"
# Requirements:
#     * Accept input from two players, representing their choices (rock, paper, or scissors).
#     * Implement logic to determine the winner based on the game rules:
#         - Rock crushes scissors
#         - Scissors cut paper
#         - Paper covers rock
#         - If both players make the same choice, it's a tie.
#     * Display the result of the game.

# player_1 = input('player 1, enter your choice (rock,paper,scissors) :').lower()
# player_2 = input('player 1, enter your choice (rock,paper,scissors) :').lower()
#
# valid_choices = {"rock", "paper", "scissors"}
# if player_1 not in valid_choices or player_2 not in valid_choices:
#     result = "Invalid choice. Please enter either 'rock', 'paper', or 'scissors'."
# elif player_1 == player_2:
#     result = "It's a Tie!!"
# elif player_1 == 'rock' and player_2 == 'scissors' or \
#     player_1 == 'scissors' and player_2 == 'paper' or \
#     player_1 == 'paper' and player_2 == 'rock':
#     result = 'player 1 wins!'
# else:
#     result = 'player 2 wins'
# print(result)


# Task 22: Currency Converter
# Description: Create a program that converts an amount of money from one currency to another based on current exchange rates.
# Example Input: Amount = $100, Currency = USD to EUR
# Example Output: "The converted amount is €85.62."

# Requirements:
#     * Accept input from the user for the amount of money and the currency conversion (e.g., USD to EUR).
#     * Implement logic to convert the amount from the source currency to the target currency.
#     * Display the converted amount.

# exchange_rates = {'USD to EUR': 0.8562, 'USD to GBP': 0.7325, 'USD to INR': 74.85, 'EUR to USD': 1.1684 }
#
# amount = float(input('Enter the amount :'))
# conversion = input("Enter the currency conversion (e.g., USD to EUR): ").upper()
# exchange_rates_uppercase = {key.upper(): value for key, value in exchange_rates.items()}

# if conversion not in exchange_rates_uppercase:
#     print("Invalid currency conversion. Please enter a valid conversion.")
# else:
#     target_currency, source_currency = conversion.split(' TO ')
#     converted_amount = amount * exchange_rates_uppercase[conversion]
#
#     print('converted amount is',converted_amount, target_currency)

# Task 23: Password Strength Checker
# Description: Develop a program that evaluates the strength of a user's password based on certain criteria
#               (e.g., length, complexity).
# Example Input: "Pa$$w0rd"
# Example Output: "The password is strong."

# Requirements:
#     * Accept input from the user for their password.
#     * Implement logic to evaluate the strength of the password based on criteria such as length, complexity, etc.
#     * Display the result indicating whether the password is strong or weak.

# user_password = input("Enter your password: ")
# special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>\/?"""
#
# if len(user_password) < 8:
#     print('password is weak, It should have at least 8 characters.')
# else:
#     if not any(char in special_characters for char in user_password):
#         print('The password is weak. It should include special characters.')
#     else:
#         print('password is strong!!')


# Task 24: Error Handling
# Description: Write a program that handles different types of errors and displays appropriate error messages to the user.
# Example Input: "5" (when expecting an integer)
# Example Output: "Invalid input. Please enter a valid integer."

# Requirements:
#     * Implement a part of the program where errors might occur
#     * Use try-except blocks to catch and handle different types of errors.
#     * Display informative error messages to the user based on the type of error encountered.
#     * Ensure that the program gracefully handles errors without crashing.

try:
    user_input = input("Enter an integer: ")
    user_integer = int(user_input)

    print('You entered :', user_integer)

except ValueError:
    # Handle ValueError (e.g., when the user enters a non-integer)
    print("Invalid input. Please enter a valid integer.")

except KeyboardInterrupt:
    # Handle KeyboardInterrupt (e.g., when the user presses Ctrl+C)
    print("Operation interrupted by the user.")

except Exception as e:
    # Handle other unexpected errors
    print("An unexpected error occured", e)

# Task 25: Game Character Decision-Making
# Description: Create a program that simulates decision-making for a game character based on different scenarios (e.g., fight or flee, choose a weapon).
# Example Input: Scenario = "Encounter enemy"
# Example Output: "You decide to fight the enemy."

# Requirements:
#     * Define multiple scenarios that the game character might encounter
#               (e.g., encounter enemy, find a treasure, etc.).
#     * Implement logic to make decisions for the character based on the given scenarios.
#     * Display the outcome of the character's decision for each scenario.

scenarios = ["Encounter enemy", "Find a treasure"]

for scenario in scenarios:
    if scenario == "Encounter enemy":
        decision = input("You encounter an enemy. Will you fight or flee? ").lower()
        if decision == "fight":
            print("You decide to fight the enemy. Good luck!")
        elif decision == "flee":
            print("You decide to flee. Live to fight another day!")
        else:
            print("Invalid decision. Please choose 'fight' or 'flee'.")

    elif scenario == "Find a treasure":
        decision = input("You find a treasure chest. Will you open it or leave it? ").lower()
        if decision == "open":
            print("You decide to open the treasure chest. What riches await?")
        elif decision == "leave":
            print("You decide to leave the treasure chest untouched. Wise choice!")
        else:
            print("Invalid decision. Please choose 'open' or 'leave'.")

    else:
        print("Unknown scenario. Please define the decision-making logic for this scenario.")


