#Program to classify triangle based on side lengths
#Function to classify triangle based on side lengths
def classify_triangle(side1, side2, side3):
    
    #Check for equilateral triangle
    if side1 == side2 == side3:
        return "Equilateral"

    #Check for isosceles triangle
    elif side1 == side2 or side2 == side3 or side1 == 3:

        return "Isosceles Triangle"

    #if all sides are different, it is a scalene triangle
    else:

        return "Scalene Triangle"

#Read the length of the three sides of the triangle from user
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

#display the result
print("The triangle is:", classify_triangle(side1, side2, side3))