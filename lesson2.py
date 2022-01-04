def user_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Номер телефон: {phone}')


user_data(name=input('Имя: '), lastname=input('Фамилия: '), year_of_birth=input('Год Рождения: '),
          city=input('Город проживания: '), email=input('email: '), phone=input("phone: "))