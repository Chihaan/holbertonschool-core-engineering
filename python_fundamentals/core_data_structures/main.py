#!/usr/bin/env python3
element_at = __import__('element_at').element_at
replace_in_list = __import__('replace_in_list').replace_in_list
print_matrix_integer = __import__('print_matrix_integer').print_matrix_integer

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
