#MARK SCORED IN CIA 1
# Function to get student details and calculate average marks
def main() :

    # Get the number of students
    num_students = int(input("Enter the number of students: "))

    # Loop through each student to get their details
    for i in range(num_students) :

        print(f"\nEnter details for student {i + 1}:")
        name = input("Name: ")
        reg_no = input("Register Number: ")
        mark1 = float(input("Mark 1: "))
        mark2 = float(input("Mark 2: "))
        mark3 = float(input("Mark 3: "))

        # Calculate average
        average = (mark1 + mark2 + mark3) / 3

        # Display the result
        print(f"\nName: {name}, Register Number: {reg_no}")
        print(f"Marks: {mark1}, {mark2}, {mark3}")
        print(f"Average Marks: {average:.2f}")
        print("-" * 30)

# Call the main function to run the program
main()
