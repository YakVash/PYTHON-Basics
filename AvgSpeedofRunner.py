# This program calculates the average speed of a runner in miles per hour.
# It takes the distance in kilometers and time in minutes and seconds as input.
distance_kilometers = float(input("Enter the distance covered (in kilometers): "))

time_minutes = float(input("Enter the minutes taken (in minutes): "))
time_seconds = float(input("Enter the seconds taken (in seconds): "))

# Convert distance to miles and time to hours
distance_mile = distance_kilometers / 1.6
# Convert time to hours
time_hours = (time_minutes / 60) + (time_seconds / 3600)
# Calculate average speed in miles per hour
average_speed_mph = distance_mile / time_hours

# Display the average speed
print(f"The average speed of the runner is {average_speed_mph:.2f} miles per hour.")
