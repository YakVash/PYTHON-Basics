# Function to find common items between two shopping lists
def find_common_items(customer1_items, customer2_items) :

    # Find common items using set intersection
    common_items = customer1_items & customer2_items
    return tuple(common_items)  # Return the common items as a tuple (immutable)

def main() :
    
    # Define shopping lists for two customers
    customer1_items = {"Milk", "Bread", "Eggs", "Butter", "Cheese"}
    customer2_items = {"Milk", "Eggs", "Fruit", "Butter", "Rice"}
    
    # Find common items
    common_items = find_common_items(customer1_items, customer2_items)
    
    # Output the common items
    print("Common items between the two customers:", common_items)

# Call the main function to run the program
main()
