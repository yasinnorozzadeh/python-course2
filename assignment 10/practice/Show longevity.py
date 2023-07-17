from datetime import date
today = date.today()
print("today:", today)
day_birth = int(input("enter your day of birth: "))
month_birth = int(input("enter your month of birth: "))
year_birth = int(input("enter your year of birth: "))
days = (today.year - year_birth) * 365 + (today.month - month_birth) * 30 + today.day - day_birth
weeks = days / 7
seconds = ((days * 24) * 60) * 60
print(round(weeks), f"weeks have passed since{year_birth}.{month_birth}.{day_birth}")
print(days, f"days have passed since{year_birth}.{month_birth}.{day_birth}")
print(seconds, f"seconds have passed since{year_birth}.{month_birth}.{day_birth}")