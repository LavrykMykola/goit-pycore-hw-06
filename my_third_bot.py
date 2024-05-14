from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        print("Phone number successfully added")

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]
        print("Phone number successfully removed")

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)
        print("Phone number successfully edited")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        print("Phone number not found")


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record
        print("Record successfully added")

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print("Record not found")

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
            print("Record deleted")
        else:
            print("Record not found")


def main():
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    john.remove_phone("1112223333")

    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    book.delete("Jane")


if __name__ == "__main__":
    main()
