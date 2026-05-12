from datetime import datetime

age = int(input("Enter your age:"))

years = datetime.now().year

birth = years - age

print(f"We think you were born back in {birth}")