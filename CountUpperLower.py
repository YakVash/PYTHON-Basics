#Program to count uppercase and lowercase and uppercase letters in a string
str = input("Enter a string: ")
upper_count = 0
lower_count = 0

for char in str:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
        
#Display the counts
print("Number of uppercase letters: ", upper_count)
print("Number of lowercase letters: ", lower_count)
