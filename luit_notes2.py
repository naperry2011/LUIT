# list change positions
# Version doesn't work second print shows your second number twice
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping: ', first, second)
first = second
second = first
print('After swapping: ', first, second)

# complex developed process on swapping numbers
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping: ', first, second)
temporary = first
first = second
second = temporary
print('After swapping: ', first, second)


# simplified version of swapping numbers
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping: ', first, second)
first , second = second, first
print('After swapping: ', first, second)

# sorting with list
random_numbers = [2, 5, 3, -5, 4]
random_numbers.sort()
print(random_numbers)


# sorting reverse with a word trigger
random_numbers = [2, 5, 3, -5, 4]
random_numbers.sort(reverse=True)
print(random_numbers)


# list.name.sort(): sorts the original list
# sorted(list_name): gives back a new, sorted list, keeps the original unchanged


# List checking presence

invited_guest = ['Kate', 'Adam', 'Scott', 'Bruce', 'William']
name = input('What is your name? ')
if name in invited_guest:  # if {input}_in_{variable}:
    print('Welcome Family!')

else: 
    print('Get the fuck out of here!!!')
    

# List comprehensions

# What I've been learning
numbers =[] 
for i in range(1, 20):
    numbers.append(i)
print(numbers)

# Now simplify it
numbers = [i for i in range(1,35)]
print(numbers)

# Nested Lists
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0] [2])

table = [[i for i in range(1, 6)] for j in range(4)]
print(table)

