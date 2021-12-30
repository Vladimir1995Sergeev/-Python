my_list = [7, 5, 3, 3, 2]
new_number = float( input("Введите число: "))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
    else:
        break
my_list.insert(i, new_number)
print(my_list)