import sys

result = 0
while True:
    line = input("Enter the code character g to exit: ")
    symbols = line.split(" ")
    for symbol in symbols:
        try:
            number = float(symbol)
            result += number
        except:
            if symbol == 'g':
                print(f"You sum is {result}. Program is terminated")
                exit(0)
            else:
                print(f"You sum is {result}. Input error", file=sys.stderr)
                exit(1)