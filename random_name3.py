import random 

# We are going to create a python script that generates unique names for the follow departments. If the user isn't apart of these departments they will not be allowed to move forward.
department_names = ['Marketing', 'Accounting', 'FinOps']
username = input("What is your name? ")
department = input("What department do you work for? ")

if department in department_names:
    answer = input(f"Welcome {username} your {department} department is allowed to use this function. How can we be of assistance? ")
else:
    print(f"Sorry {username} your {department} department is not allowed to use this function, have a great day.")