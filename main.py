import sys
from address_book import AddressBook


def check_input_parameters(param_count, command_name):
    if len(sys.argv) < param_count:
        print(f"Usage: python order2.py {command_name}" + " <param>" * (param_count - 2))
        return False
    else:
        return True


addressBook = AddressBook()

if len(sys.argv) > 1:
    if sys.argv[1] == 'add':
        if check_input_parameters(4, "add"):
            addressBook.add(sys.argv[2], sys.argv[3])
    if sys.argv[1] == 'update':
        if check_input_parameters(4, "update"):
            addressBook.update(sys.argv[2], sys.argv[3])
    if sys.argv[1] == 'delete':
        if check_input_parameters(3, "delete"):
            addressBook.delete(sys.argv[2])
    if sys.argv[1] == 'show':
        addressBook.show()
    if sys.argv[1] == 'search':
        if check_input_parameters(3, "search"):
            addressBook.search(sys.argv[2])
