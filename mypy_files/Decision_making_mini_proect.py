####### Bank loan approvel

# def loan_approval_system(credit_score, income, loan_amount):
#     credit_score_threshold = 700
#     income_threshold = 50000
#     loan_amount_threshold = 10000
#
#     if credit_score >= credit_score_threshold:
#         if income >= income_threshold:
#             if loan_amount <= loan_amount_threshold:
#                 return "Loan Approved"
#             else:
#                 return "Further evaluation required for loan amount"
#         else:
#             return "Income too low for loan approval"
#     else:
#         return "Credit score too low for loan approval"
#
# credit_score = int(input("Enter your credit score :"))
# income = float(input("Enter your income :"))
# loan_amount = float(input("Enter the loan amount :"))
#
# result = loan_approval_system(credit_score, income, loan_amount)
# print(result)
#

##########  Flight Booking System:
### Develop a program for a flight booking system. Consider factors such as seat availability,
### passenger age, and class preference. Use nested if statements to determine if a booking is successful
### and calculate the ticket price.

# def flight_booking_system(seat_availability, passenger_age, class_preference):
#     ECONOMY_PRICE = 500
#     BUSINESS_PRICE = 1000
#     AGE_CHILD = 12
#     AGE_SENIOR = 60
#
#     if seat_availability > 0:
#         if class_preference.lower() == "economy":
#             ticket_price = ECONOMY_PRICE
#         elif class_preference.lower() == "business":
#             ticket_price = BUSINESS_PRICE
#         else:
#             return "Invalid class preference. Please choose Economy or Business."
#
#         if passenger_age < AGE_CHILD:
#             ticket_price *= 0.5
#         elif passenger_age >= AGE_SENIOR:
#             ticket_price *= 0.8
#
#         return f"Booking successful! Ticket price per person: {ticket_price :}"
#     else:
#         return "Sorry, no seats available for booking."
#
# seat_availability = int(input("Enter the seats available :"))
# passenger_age = int(input("Enter the passenger age :"))
# class_preference =input("Enter the class (economy or business) :")
#
# result  = flight_booking_system(seat_availability, passenger_age, class_preference)
# print(result)


####### Medical Diagnosis:
#######Create a program that simulates a medical diagnosis system. Consider symptoms input by the user
#### and use nested if statements to suggest possible illnesses or conditions.

# The program defines sets of symptoms associated with common illnesses (common cold, flu, allergies).
# It takes symptoms as input from the user, converts them to lowercase, and creates a set.
# Using nested if statements, the program checks if the provided symptoms match those associated with common illnesses.
# If a match is found, the program suggests a possible illness and provides advice.
# The result is displayed to the user.


# def medical_diagnosis(symptoms):
#     common_cold_symptoms = {'runny nose', 'sneezing', 'cough', 'sore throat'}
#     flu_symptoms = {'fever', 'body aches', 'fatigue', 'headache'}
#     allergies_symptoms = {'itchy eyes', 'sneezing', 'runny nose', 'skin rash'}
#
#     if symptoms.issubset(common_cold_symptoms):
#         return "You may have a common cold."
#     elif symptoms.issubset(flu_symptoms):
#         return "You may have the flu."
#     elif symptoms.issubset(allergies_symptoms):
#         return "You may be experiencing allergies."
#     else:
#         return "couldn't determine the specific illness based on the provided symptoms."
#
# user_input = input("Enter your symptoms (comma-separated): ")
# symptoms = set(user_input.lower().split(','))
#
# result = medical_diagnosis(symptoms)
# print(result)

#########  Automated Teller Machine (ATM):
## Implement an ATM system where users can withdraw money, check balances, and deposit funds.
## Use nested if statements to validate transactions and handle various scenarios such as insufficient funds.

## The program initializes a global variable account_balance to represent the initial balance.
## The atm_system function performs ATM transactions based on the provided action and amount.
## Nested if statements are used to validate and execute different transaction types (withdraw, check balance, deposit).
## The program takes input from the user for the ATM action and amount.
## The result of the transaction is displayed to the user.

# account_balance = 1000
# def atm_system(action, amount):
#     global account_balance
#     if action.lower() == 'withdraw':
#         if amount > 0 and amount <= account_balance:
#             account_balance -= amount
#             return f"Withdrawal successful! Remaining balance: {account_balance}"
#         elif amount <= 0:
#             return "Invalid withdrawal amount. Please enter a positive value."
#         else:
#             return "Insufficient funds. Withdrawal unsuccessful."
#     elif action.lower() == 'check balance':
#         return f"Your current balance is: {account_balance}"
#     elif action.lower() == 'deposit':
#         if amount > 0:
#             account_balance += amount
#             return f"Deposit successful! Updated balance: {account_balance}"
#         else:
#             return "Invalid deposit amount. Please enter a positive value."
#     else:
#         return "Invalid action. Please choose 'withdraw', 'check balance', or 'deposit'."
#
# action = input("Enter your desired action (withdraw/check balance/deposit): ")
# amount = float(input("Enter the amount: "))
#
# result = atm_system(action, amount)
# print(result)



### The game starts by welcoming the player to a mysterious forest.
## The player makes decisions at different points in the game using input.
## Nested if statements are used to handle different choices and outcomes.
## The game includes multiple branches and possible paths based on the player's decisions.
## The time.sleep function is used to create a more immersive experience with delayed text output.

import time

def text_based_game():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)

    print("\nYou find yourself in a mysterious forest.")
    time.sleep(1)

    print("\nYou come across a fork in the path. Do you want to go left or right?")
    choice1 = input("Enter your choice (left/right): ")

    if choice1.lower() == 'left':
        print("\nYou discover a hidden treasure chest!")
        time.sleep(1)
        print("Do you want to open the chest or leave it?")
        choice2 = input("Enter your choice (open/leave): ")

        if choice2.lower() == 'open':
            print("\nCongratulations! You found a magical amulet.")
            time.sleep(1)
            print("You continue your journey with the amulet.")
        elif choice2.lower() == 'leave':
            print("\nYou decide to leave the chest and continue exploring.")
            time.sleep(1)
            print("As you walk away, you hear a mysterious sound in the distance.")
        else:
            print("\nInvalid choice. The game ends.")
    elif choice1.lower() == 'right':
        print("\nYou encounter a friendly creature offering guidance.")
        time.sleep(1)
        print("Do you want to follow the creature or ignore its advice?")
        choice3 = input("Enter your choice (follow/ignore): ")

        if choice3.lower() == 'follow':
            print("\nThe creature leads you to a magical portal.")
            time.sleep(1)
            print("You step through the portal and find yourself in a new realm.")
        elif choice3.lower() == 'ignore':
            print("\nYou decide to ignore the creature and explore on your own.")
            time.sleep(1)
            print("You discover a hidden passage that leads to an ancient temple.")
        else:
            print("\nInvalid choice. The game ends.")
    else:
        print("\nInvalid choice. The game ends.")

text_based_game()

######### Smart Home Automation:
#########Develop a program for a smart home system. Use nested if statements to simulate the automation of lights,
######### temperature, and security based on user preferences and environmental conditions.
