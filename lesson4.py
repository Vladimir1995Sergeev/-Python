my_list = [1, 777, 13, 21, 12, 9, 19, 21, 4, 72, 72, 74, 93, 93, 69, 12]
print(f"Исходные элементы списка: {my_list} ")
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Элементы списка, не имеющие повторений: {new_list}")