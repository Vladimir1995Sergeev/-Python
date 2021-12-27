time_in_seconds = int(input("Enter the time in seconds: "))
hours = time_in_seconds // 3600
residue = time_in_seconds % 3600
minutes = residue // 60
seconds = residue % 60
print(f"Result: {hours}:{minutes}:{seconds} ")
