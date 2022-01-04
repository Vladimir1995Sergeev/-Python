def my_func(x, y):
    counter = 1
    result = 1 / x
    while counter < abs(y):
        result = result * (1/x)
        counter += 1
    return result
print(f'Возведения степени : '
      f'{my_func(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')