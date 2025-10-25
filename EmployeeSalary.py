#Program to calculate gross and net salary of an employee
print("Company name: Tech Solutions Inc.")

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

#Calculate allowances and deductions
hra = 0.20 * basic_salary  
da = 0.50 * basic_salary
ta = 0.30 * basic_salary
pf = 0.12 * basic_salary  
gross_salary = basic_salary + hra + da + ta - pf

#Calculate net salary
net_salary = gross_salary - pf
#Display the salary details
print("DA amount:", da)
print("HRA amount:", hra)
print("TA amount:", ta)
print("PF amount:", pf)
print("Gross Salary:", gross_salary)
print("Net Salary of", employee_name, "is:", net_salary)