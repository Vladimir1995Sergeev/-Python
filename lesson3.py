def workers_statistics():
    workers = [['Бобров ', '19252,50 \n'], ['Савин ', '13380 \n'], ['Фролов ', '22488,90 \n'], ['Шорохов ', '85390 \n']]
    try:
        with open('new_file.txt', 'r+', encoding="utf-8") as file:
            for el in range(len(workers)):
                file.writelines(workers[el])
            l = file.readlines()
            poor = []
            sum = 0
            for el in range(len(l)):
                salary = int((l[el].split())[1])
                if salary < 20000:
                    poor.append((l[el].split())[0])
                sum += salary
            print(f'Средняя величина дохода сотрудников равна {sum / len(workers) / 12:.2f}')
            print(f'Меньше 20 тыс. рублей получает сотрудник: {", ".join(poor)}')
    except FileNotFoundError:
        return 'Файл не найден.'


workers_statistics()