#check whether the factor forms a group of N
# Read a group of five numbers
g = []
result = []
print("Enter five numbers:")

for i in range(5) :

    number = int(input("Number: "))
    g.append(number)


# Read another number 'n'
n = int(input("Enter a number 'n': "))

# Check each number in g to see if it's a factor of n
for i in range(5):

    if n % g[i] == 0 : 

        result.append(g[i]) 


if result :

    print(f"Factors of {n} from the group are: {result}")

else :

    print("No factors found in the group.")
