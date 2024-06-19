import random 

# We are going to create a python script that generates unique names for the follow departments. If the user isn't apart of these departments they will not be allowed to move forward.

# List of allowed departments
department_names = ['Marketing', 'Accounting', 'FinOps']

# List of random adjectives and nouns for name generation
adjectives = ['Quick', 'Mighty', 'Smart', 'Stupid', 'Blue', 'Green']
nouns = ['Lions', 'Monkey', 'Tiger', 'Snail', 'Bear']

# Function to generate a random name
def generate_random_name():
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adj}{noun}"
# User Prompts 
username = input("What is your name? ")
department = input("What department do you work for? ")

if department in department_names:
    answer = input(f"Welcome {username} your {department} department is allowed to use this function. Are you requesting a unique name? Y/N:\n")
    if answer.upper() == "Y":
        unique_name = generate_random_name()
        print(f"{username} your unique name is: {unique_name}")
    else:
        print(f"Okay {username}, no unique name generated. Have a great day!")
else:
    print(f"Sorry {username} your {department} department is not allowed to use this function, have a great day.")
    

# updating the code 
