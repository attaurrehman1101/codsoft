# Contact Book Application

# Define a dictionary to store contacts.
contacts = {}

# Function to add a new contact.
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")

# Function to view the contact list.
def view_contacts():
    if contacts:
        for name, contact_info in contacts.items():
            print(f"Name: {name}, Phone: {contact_info['phone']}")
    else:
        print("Contact list is empty.")

# Function to search for a contact.
def search_contact():
    search_term = input("Enter the name or phone number to search for: ")
    found = False
    for name, contact_info in contacts.items():
        if search_term in name or search_term in contact_info['phone']:
            print(f"Name: {name}, Phone: {contact_info['phone']}")
            found = True
    if not found:
        print("No matching contacts found.")

# Function to update a contact.
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Contact found. Update the information:")
        phone = input("New phone number: ")
        email = input("New email address: ")
        address = input("New address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact.
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# User Interface
while True:
    print("\nContact Book Application")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
