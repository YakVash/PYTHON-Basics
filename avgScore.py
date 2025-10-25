scores = [ ]

for i in range(1, 4+1):
    num = int(input(f"Enter the score for match {i}: "))
    scores.append(num)
 # Calculate average
average_score = sum(scores)/len(scores)

# Output the result
print(f"The average score over 4 matches is: {average_score}")