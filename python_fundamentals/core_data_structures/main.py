#!/usr/bin/env python3


element_at = __import__('element_at').element_at
replace_in_list = __import__('replace_in_list').replace_in_list
print_matrix_integer = __import__('print_matrix_integer').print_matrix_integer
add_tuple = __import__('add_tuple').add_tuple
common_elements = __import__('common_elements').common_elements
update_dictionary = __import__('update_dictionary').update_dictionary

my_list = ["a", "b", "c", "d", "e"]

print()
print("Ex:1")
print()

print(element_at(my_list, 3))
print(element_at(my_list, -1))
print(element_at(my_list, 15))
print(element_at(my_list, 0))
print(element_at(my_list, 1))
print(element_at(my_list, -100))
print(element_at(my_list, 13))
print(element_at(my_list, 4))

print()
print("Ex:2")
print()

my_list = [1, 2, 3, 4, 5]
print(replace_in_list(my_list, 3, 99))
print(replace_in_list(my_list, 15, 99))

print()
print("Ex:3")
print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)

print()
print("Ex:4")
print()

print(add_tuple((1, 89), (88, 11)))
print(add_tuple((1, 89), (1, )))
print(add_tuple((1, 89), ()))
print(add_tuple((), ()))


print()
print("Ex:5")
print()



set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
print(sorted(list(common_elements(set_1, set_2))))

print()
print("Ex:6")
print()


d = {'language': 'C', 'number': 89, 'track': 'Low level'}
print(update_dictionary(d, 'language', 'Python'))
print(update_dictionary(d, 'city', 'San Francisco'))
