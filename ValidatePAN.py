#display a validation pan number
def is_valid_pan(pan_number) :
    
    # Check the length of the PAN number
    if len(pan_number) != 10 :

        return False


    # Check the format
    if (pan_number[:5].isalpha() and pan_number[:5].isupper() and  
    # First 5 should be uppercase letters

        pan_number[5:9].isdigit() and                            
        # Next 4 should be digits

        pan_number[9].isalpha() and pan_number[9].isupper()) :  
        # Last should be an uppercase letter

        return True

    return False

# Example usage
pan_number = input("Enter the PAN number: ")

if is_valid_pan(pan_number) :

    print("The PAN number is valid.")

else :

    print("The PAN number is invalid.")
