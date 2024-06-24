# Creating Functions. Every function starts off with the 'def' indicator 
def greet():
    print('Hello new function!!!')
    
greet() 


def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)
    
get_average([5, 3, 25, 15, 485, 68])


def print_letter_count(text, letter):
    counter = 0.0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
    
    
print_letter_count('apple', 'p')