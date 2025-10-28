#print capital and cities
capitals = {

        "USA"    : "Washington, D.C.",
        "France" : "Paris",
        "Japan"  : "Tokyo",
        "India"  : "New Delhi",
        "Brazil" : "Brasília"

}

print("Enter the name of a country to get its capital:")

for i in capitals.keys() :

    print(i, end=", ")

print("\n")
    
country_name = input("Country: ").strip()
    
if country_name in capitals :

    capital = capitals.get(country_name)
    print(f"The capital of {country_name} is: {capital}")
    
else :

    print("please enter capital in given list.")

