def calculate_cell_phone_bill(minutes_used, texts_used):
    # Base charges and rates
    base_charge = 15.00
    base_minute = 50
    base_texts = 50
    additional_minute_rate = 0.25
    additional_text_rate = 0.15
    tax_rate = 0.05
    emergency_fee = 0.44

    #Calculate additional charges
    additional_minutes_charge = max(0, minutes_used - base_minute) * additional_minute_rate
    additional_texts_charge = max(0, texts_used - base_texts) * additional_text_rate

    #Calculate subtotal, tax, and total bill
    subtotal = base_charge + additional_minutes_charge + additional_texts_charge + emergency_fee
    tax = subtotal * tax_rate
    total_bill = subtotal + tax

    #Display charges
    print(f"Base Charge: ${base_charge:.2f}")
    if additional_minutes_charge > 0:
        print(f"Additional Minutes Charge: ${additional_minutes_charge:.2f}")
    if additional_texts_charge > 0:
        print(f"Additional Texts Charge: ${additional_texts_charge:.2f}")
    print(f"Emergency Fee: ${emergency_fee:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total Cell Phone Bill: ${total_bill:.2f}")

#User input
minutes_used = int(input("Enter the number of minutes used: "))
texts_used = int(input("Enter the number of texts sent: "))

#Calculate and display the cell phone bill
calculate_cell_phone_bill(minutes_used, texts_used)
