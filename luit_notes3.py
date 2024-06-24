# tuples = () list = []

empty_tuple = ()

one_el_tuple_a = (1,)
one_el_tuple_a = 1,
three_el_tuple_a = 1, 2, 3,


# len function tuple operations
user_data = ('John', 'Doe')
print(len(user_data))

# if statement
user_data2 = ('John', 'Perry', 'American')
if 'American' in user_data2:
    print('This person comes from the US!')

# for statement
user_data3 = ('John', 'Perry', 'American')
for element in user_data3:
    print(element)
    

numbers = (5, 2) * 3
print(numbers)

# tuples-list
city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiera','Algiera', 3.9)

capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiera','Algiera', 3.9)]
for capital in capitals:
    print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2] )
    
# A list within a tuple 
user_data4 = ('Pack', 'Asian', 1975, [77.0, 74.3, 78.2])
print(user_data4[3])