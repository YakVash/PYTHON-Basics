#program for a telephone directory
class TelephoneDirectory :

    def __init__(self) :

        self.directory = {}  # Initialize an empty directory

    def add_employee(self, name, numbers) :

        self.directory[name] = numbers  # Add employee and their numbers

    def search_numbers(self, query) :

        results = {}  # Store search results
        for name, numbers in self.directory.items() :

            if query.lower() in name.lower() :  # Case insensitive search

                results[name] = numbers

        return results

def main() :

    directory = TelephoneDirectory()  # Create a directory instance

    # Add some employees
    directory.add_employee("John Paul", ["123-456-7890", "987-654-3210"])
    directory.add_employee("Michel John", ["555-123-4567"])
    directory.add_employee("Alice Smith", ["555-987-6543"])
    directory.add_employee("John Doe", ["444-333-2222"])

    query = input("Enter part of the employee's name to search: ")  # User input

    results = directory.search_numbers(query)  # Search for numbers

    # Print the results
    if results :

        print("Phone numbers found:")

        for name, numbers in results.items() :

            print(f"{name}: {', '.join(numbers)}")

    else :

        print("No employee found with that name.")

if __name__ == "__main__" :

    main()
