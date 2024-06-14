# Given income
income = 250000

# Tax rates for Lowtaxland and Ripoffland
lowtaxland_rate = 0.05
ripoffland_rate = 0.43
# Calculating the tax amounts
tax_lowtaxland = income * lowtaxland_rate
tax_ripoffland = income * ripoffland_rate
# Calculating the difference in tax amounts
tax_difference = tax_ripoffland - tax_lowtaxland

# # Printing the required output
print(f"Your income is {income} and you would pay {tax_lowtaxland} income tax in Lowtaxland or {tax_ripoffland} income tax in Ripoffland. You would save {tax_difference} by paying taxes in Lowtaxland!")

# input practice
login = input("Enter your login: ")
language = input("Enter your native language: ")

print(f"Your username is {login} and your native language is {language}")


# Typecasting
height_cm = float(input("Height converter: enter your height in cm: "))
print("Your height in feet is :", height_cm / 30.48)

# Salary calculator code
hours = float(input("How many hours did you work last month? "))
hourly_rate= float(input("What is your hourly rate? "))
salary = hours * hourly_rate
print(f"Last month, you earned ${salary} dollars")

# If conditions
# if condition_a_met:
#     do_scenario_a()
# elif condition_b_met:
#     do scenario_b()
# else:
#     do_scenario_c

user_age = int(input("How old are you? "))
if user_age > 30:
    print("Welcome to the elite Level of adulthood!!")
elif user_age == 30:
    print("You're exactly 30 years old")
else:
    print("Leave you man/woman! You are not of age yet")
    
    
    
# Operators order 1. not 2. and 3. or

# Nested if statements
answer_a = input("Do you like traveling? y/n:\n")
if answer_a == 'y':
    answer_b = input("And where do you like to travel? ")
    print(f"{answer_b.title()} is a beautiful place to visit")
else:
    print("Well I hope you get to travel one day! ")
    

# exercise.py
purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')
 
if(is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
  print('You can get a refund.')
else:
  print('You cannot get a refund.')