class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone}"

class ContactBook:
    def __init__(self, filename='contacts.txt'):
        self.contacts = []
        self.filename = filename
        self.load_from_file()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_to_file()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. {contact}")

    def update_contact(self, index, name=None, email=None, phone=None):
        if 0 <= index < len(self.contacts):
            if name:
                self.contacts[index].name = name
            if email:
                self.contacts[index].email = email
            if phone:
                self.contacts[index].phone = phone
            self.save_to_file()
        else:
            print("Invalid contact index!")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)
            self.save_to_file()
        else:
            print("Invalid contact index!")

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.email},{contact.phone}\n")

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, email, phone = line.strip().split(',')
                    self.contacts.append(Contact(name, email, phone))
        except FileNotFoundError:
            print("No previous contacts found. Starting with a fresh contact book.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Application")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Update an existing contact")
        print("4. Delete a contact")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            email = input("Enter contact email: ")
            phone = input("Enter contact phone number: ")
            new_contact = Contact(name, email, phone)
            contact_book.add_contact(new_contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.view_contacts()
            try:
                index = int(input("Enter contact number to update: ")) - 1
                name = input("Enter new name (leave blank to keep current): ")
                email = input("Enter new email (leave blank to keep current): ")
                phone = input("Enter new phone number (leave blank to keep current): ")
                contact_book.update_contact(index, name, email, phone)
            except ValueError:
                print("Invalid input!")
        elif choice == '4':
            contact_book.view_contacts()
            try:
                index = int(input("Enter contact number to delete: ")) - 1
                contact_book.delete_contact(index)
            except ValueError:
                print("Invalid input!")
        elif choice == '5':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice! Please enter a valid number.")

if __name__ == "__main__":
    main()
