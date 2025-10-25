# Student CGPA Evaluation
cgpa = input("Enter your CGPA: ")

# Evaluate CGPA and print corresponding message
if float(cgpa) >= 9 and float(cgpa) <= 10:
    print("Outstanding!")

elif float(cgpa) >= 8 and float(cgpa) < 9:
    print("Excellent!")

elif float(cgpa) >= 7 and float(cgpa) < 8:
    print("Good!")

elif float(cgpa) >= 6 and float(cgpa) < 7:
    print("Average")

elif float(cgpa) >= 5 and float(cgpa) < 6:
    print("Better")

elif float(cgpa) >= 4 and float(cgpa) < 5:
    print("Poor!")
