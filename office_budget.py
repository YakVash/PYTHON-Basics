#Program to calculate the budget for setting up a new office
cost_comp = int(input("Enter the cost of one computer: "))
num_comp = int(input("Enter the number of computers: "))

#Calculate total cost of computers
total_cost = cost_comp*num_comp

#Get budget for office setup
cost_table = int(input("Enter the cost of one table: "))
num_table = int(input("Enter the number of tables: "))
total_cost += cost_table*num_table

#Get cost for chairs
cost_chair = int(input("Enter the cost of one chair: "))
num_chair = int(input("Enter the number of chairs: "))
total_cost += cost_chair*num_chair

#Get budget for office supplies
print("The total cost of the office furniture is:", total_cost)

#Get budget from user
num_hours = int(input("Enter the number of working hours: "))
hourly_rate = int(input("Enter the hourly rate: "))
total_earnings = num_hours * hourly_rate

#Get initial budget
total_budget = budget + total_earnings + total_cost
print("The total budget for setting up the office is:", total_budget)

