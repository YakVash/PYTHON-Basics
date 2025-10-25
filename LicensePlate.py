#Program to validate license plate numbers
def validate_license_plate(plate):
    #Check for older style license Plate: 3 letters followed by 3 digits
    if len(plate) == 6 and plate[:3].isalpha() and plate[:3].isalpha() and plate[3:].isdigit():
        return "Valid for Old Style License Plate."
    #Check for newer style license Plate: 4 digits followed by 3 letters
    elif len(plate) == 7 and plate[:4].isdigit() and plate[4:].isalpha() and plate[4:].isupper():
        return "Valid for New Style License Plate."
    else:
        return "Invalid License Plate."
#USER INPUT
license_plate = input("Enter the license plate number: ")

#VALIDATE AND DISPLAY RESULT
result = validate_license_plate(license_plate)
print(result)