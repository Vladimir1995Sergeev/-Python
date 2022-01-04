def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Division by zero is impossible"
    except ValueError:
        return "Enter the number"
print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))