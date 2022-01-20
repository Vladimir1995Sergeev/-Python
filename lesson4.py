def File_work():
    num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = []
    try:
        with open('File_work.txt', 'r+', encoding="utf-8") as file:
            with open('new_file.txt', 'r+', encoding="utf-8") as new_file:
                l = file.readlines()
                for el in l:
                    el = el.split(' ', 1)
                    new_text.append(num[el[0]] + ' ' + el[1])
                new_file.writelines(new_text)
    except FileNotFoundError:
        return 'Файл не найден.'


File_work()