contacts= []
def displaymenu():
    #display the menu options
    print("\n Contact list manager")
    print("1. add new contact")
    print("2. view all contacts")
    print("3. search contacts")
    print("4. delete contact")
    print("5. exit")

def add_contact():
    #add new contact
    name= input("enter contact name: ").strip()
    phone_input= input("enter 11 digit phone number: ").strip()
    try:
        if len(phone_input)<11:
            print("Error: phone number incomplete, please check and try again")
        elif len(phone_input)>11:
            print("Error: Phone number more than 11, please check and try again")
            return
        phone= int(phone_input)
    except ValueError:
        print("Error: Please enter numbers only")
        return
    email= input("enter email address: ").strip()
    #add the details to contacts list
    contacts.append([name, phone, email])
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contact found")
        return
    for index in range(len(contacts)):
        contact= contacts[index]
        print(f"{index}: Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

def search_contacts():
    #enter search term
    search_term= input("enter contact name(case sensitive): ").lower().strip()
    found= False
    for contact in contacts: #loop through contacts
        if search_term in contact[0].lower():
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
            found= True
    if not found:
        print("No Contact found")

def delete_contact():
    #Delete a contact by index.
    view_contacts()  # Show contacts first
    if not contacts:
        return
    try:
        index = int(input("Enter index to delete: "))  # Convert to int
        if 0 <= index < len(contacts):  # Validate index
            deleted_contact = contacts.pop(index)  # Remove contact
            print(f"Deleted contact: {deleted_contact[0]}")
        else:
            print("Contact doesn't exist. Check and try again")
    except ValueError:  # Handle non-numeric input
        print("Please enter a valid number.")
    except Exception as e:  # Catch unexpected errors
        print(f"An error occurred: {e}")

# Step 7: Define main function
def main():
    """Main program loop."""
    while True:  # While loop
        displaymenu()
        choice = input("Enter choice (1-5): ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter 1-5.")

# Step 8: Run the program
if __name__ == "__main__":
    main()