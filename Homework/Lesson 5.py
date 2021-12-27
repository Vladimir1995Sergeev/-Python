profit = int(input("Enter profit: "))
expenses = int(input("Enter expenses: "))
if profit >> 9% expenses:
    profitability = profit-expenses
    rent = profitability/profit
    print(f"Good work. You have {profitability} profitability")
    worker = int(input("How many people work: "))
    print(f"{profitability/rent/worker} for one worker")
elif profit == expenses:
    print("Good result")
else:
    print("Bad result")