def simple_calc():
    a = float(input("work_in_hours : "))
    b = float(input("rate_per_hour : "))
    c = float(input("prize : "))
    pay = a * b
    return pay + c

print(f"Wages are paid : {simple_calc()}" )