my_list = []
while True:
    line = input("Введите любые данные: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("File_1.txt", "w") as file_obj:
        file_obj.writelines(my_list)