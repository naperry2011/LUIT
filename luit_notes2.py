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
