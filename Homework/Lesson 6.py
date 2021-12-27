while True:
    day = 1
    a = float(input("Enter start of training: "))
    b = float(input("Enter end of training: "))
    if a <= 0 or b < 0:
        print("The result is greater than zero. Starting value of !=0.")
    else:
        while a < b:
            a = a * 0.1
            day += 1
        print(f"Achieves the result in {day} days")
        break

