my_list = [52, 48, 55, 77, 1, 22, 5, 33, 6, 4, 77, 5, 999, 54, 11, 22, 40, 18, 15, 64, 69, ]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(f"Исходный список : {my_list}")
print(f"Результат : {new_list}")