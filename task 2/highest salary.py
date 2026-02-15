employees = {}
# input
n = int(input("Enter the number of employees: "))
# loop to get employee details
for i in range(n):
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    employees[name] = salary
# find the employee with the highest salary
highest_employee = max(employees, key=employees.get)
# print highest employy with salary
print("Highest salary:", highest_employee,"-", employees[highest_employee])
