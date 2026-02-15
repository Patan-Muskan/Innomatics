employees = {}
n = int(input("Enter the number of employees: "))
for i in range(n):
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    employees[name] = salary
highest_employee = max(employees, key=employees.get)
print("Highest salary:", highest_employee,"-", employees[highest_employee])
