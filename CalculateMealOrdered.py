#Program to calculate the total cost of a meal in restuarant
#Function to calculate meal total including tax and tip
def calculate_meal_total(meal_cost) :
    # Define tax and tip rates
    tax_rate = 0.05 #5% tax
    tip_rate = 0.18 #18% tip

    # Calculate tax, tip and grand total amounts
    tax_amount = meal_cost * tax_rate
    tip_amount = meal_cost * tip_rate
    grand_cost = meal_cost + tax_amount + tip_amount

    # Display the breakdown of charges
    print(f"Meal Cost: ${meal_cost:.2f}")
    print(f"Tax Amount (7%): ${tax_amount:.2f}")
    print(f"Tip Amount (18%): ${tip_amount:.2f}")
    print(f"Total Meal Cost: ${grand_cost:.2f}")

#Get meal cost from the user
meal_cost = float(input("Enter the cost of the meal: $"))

#Calculate and display the meal total
calculate_meal_total(meal_cost)