# Get the number of students
no_of_std = int(input("Enter number of students in your class: "))
sum_marks = 0  # Changed variable name to avoid conflict with built-in sum()


# Loop to get marks for each student
for i in range(no_of_std) :
    
    # Input marks secured by students in CSE1001
    std_marks = int(input(f"Enter marks for student {i + 1}: "))
    sum_marks += std_marks  # Accumulate the sum of marks


# Calculate the average after collecting all marks
if no_of_std > 0 :  # Check to avoid division by zero

    avg = sum_marks / no_of_std
    print(f"Class Average is: {avg : .2f}")

else: 

    print("No students in the class.")
