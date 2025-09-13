cost_comp = int(input("Enter the cost of one computer: "))
num_comp = int(input("Enter the number of computers: "))

total_cost = cost_comp*num_comp

cost_table = int(input("Enter the cost of one table: "))
num_table = int(input("Enter the number of tables: "))
total_cost += cost_table*num_table

cost_chair = int(input("Enter the cost of one chair: "))
num_chair = int(input("Enter the number of chairs: "))
total_cost += cost_chair*num_chair

print("The total cost of the office furniture is:", total_cost)


num_hours = int(input("Enter the number of working hours: "))
hourly_rate = int(input("Enter the hourly rate: "))
total_earnings = num_hours * hourly_rate

total_budget = budget + total_earnings + total_cost
print("The total budget for setting up the office is:", total_budget)

