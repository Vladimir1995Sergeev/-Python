def count_info():
    try:
        with open('file_2.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            for el in range(len(my_list)):
                new_l = my_list[el].split()
                print(f'Количество строк в файле {len(my_list)}. В {el + 1} строке {len(new_l)} слов')
    except FileNotFoundError:
        return 'Файл_отсутствует'

count_info()