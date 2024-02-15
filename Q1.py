employee_salaries = {}

while True:
    name = input("Enter the employee's name: ")
    if name.lower() == 'no':
        break
    salary = float(input(f"Enter the salary for {name}: "))
    employee_salaries[name] = salary

print("Employee salaries:")
print(employee_salaries)
