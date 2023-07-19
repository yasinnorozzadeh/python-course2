def salary_calc(contract, hour_time):
    if contract == "A":
        if hour_time < 150:
            sal = 4000000
        elif hour_time == 150:
            sal = 5000000
        else:
            sal = 6000000

    elif contract == "B":
        sal = hour_time * 45000

    else:
        sal = "-1"
    return sal

def decrease_tax(salary, tax=9):
    percent = 1 - (tax / 100)
    final_salary = salary * percent
    return final_salary

name = input("name: ")
contract = "A" #"A: قرار دادی" "B : ساعتی"
hour_time = float(input("hour time: "))
salary = salary_calc(contract, hour_time)
final_salary = decrease_tax(salary)
print(final_salary)

