import os
import pickle


class AddressBook:

    def __init__(self):
        self.addressBook = {}
        self.addressBookFilename = "addressBook.data"
        self.read()

    def add(self, name, address):
        self.addressBook[name] = address
        self.write()
        print("Added " + name + " to address book.")

    def search(self, name):
        if name in self.addressBook:
            print(f"{name}: {self.addressBook[name]}")
        else:
            print("Name not found.")

    def update(self, name, address):
        self.addressBook[name] = address
        self.write()
        print(name + " updated in address book.")

    def delete(self, name):
        self.addressBook.pop(name)
        self.write()
        print('Deleted ' + name)

    def show(self):
        for name, address in self.addressBook.items():
            print(f"{name}: {address}")

    def write(self):
        with open(self.addressBookFilename, "wb") as f:
            pickle.dump(self.addressBook, f)

    def read(self):
        if os.path.exists(self.addressBookFilename):
            with open(self.addressBookFilename, "rb") as f:
                self.addressBook = pickle.load(f)
        else:
            with open(self.addressBookFilename, "wb") as f:
                pickle.dump(self.addressBook, f)
