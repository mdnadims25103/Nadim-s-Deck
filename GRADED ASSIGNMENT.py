#NAME:- MD NADIM SARBAR
#ENROLLMENT NO.:- 2502140103

# Contact Directory (Phase 1: In-Memory)
# Login Function
def login():
    password = "198254MNS"
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted!\n")
        return True
    else:
        print("Access denied.")
        return False


# Create (Add Contact)
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    date_added = input("Enter date added (YYYY-MM-DD): ")

    contact = {
        'name': name,
        'phones': {phone},
        'email': email,
        'date_added': tuple(date_added.split('-'))
    }

    contacts.append(contact)
    print("✅ Contact added successfully!")


# Read (View Contacts)
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, start=1):
            print(f"\nContact {i}:")
            print(f"Name       : {contact['name']}")
            print(f"Phones     : {', '.join(contact['phones'])}")
            print(f"Email      : {contact['email']}")
            print(f"Date Added : {'-'.join(contact['date_added'])}")
        print("---------------------")


# Update (Modify Contact)
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Current details:", contact)
            new_name = input("Enter new name (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_phone = input("Enter new phone (leave blank to keep current): ")

            if new_name:
                contact['name'] = new_name
            if new_email:
                contact['email'] = new_email
            if new_phone:
                contact['phones'].add(new_phone)

            print("✅ Contact updated successfully!")
            return
    print("Contact not found.")


# Delete Contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            confirm = input(f"Are you sure you want to delete {name}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.remove(contact)
                print("🗑️ Contact deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
    print("Contact not found.")


# Search Contact
def search_contact(contacts):
    keyword = input("Enter name or phone to search: ")
    found = False
    for contact in contacts:
        if (keyword.lower() in contact['name'].lower()) or (keyword in ','.join(contact['phones'])):
            print(f"\nName: {contact['name']}")
            print(f"Phones: {', '.join(contact['phones'])}")
            print(f"Email: {contact['email']}")
            print(f"Date Added: {'-'.join(contact['date_added'])}")
            found = True
    if not found:
        print("No matching contacts found.")


# Reports (Count & Unique Phones)
def report(contacts):
    print("\n--- Reports ---")
    print(f"Total Contacts: {len(contacts)}")

    all_numbers = set()
    for c in contacts:
        all_numbers.update(c['phones'])
    print(f"Unique Phone Numbers: {len(all_numbers)}")
    print("----------------")


# Main Menu Loop
def main():
    contacts = []
    if not login():
        return

    while True:
        print("\n====== Contact Directory ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Reports")
        print("7. Exit")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            search_contact(contacts)
        elif choice == '6':
            report(contacts)
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the Program
if __name__ == "__main__":
    main()
