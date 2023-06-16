# By Brett McDonald
# SID: 10158931
# Assignment 3
# Question 2: An Address Book

contacts = {}   # initiate the contacts dictionary


def get_menu_option():
    """displays a menu and carries out the appropriate action depending on which letter the user types, and then re-displays the menu"""

    print('*** My Contacts ***')
    print('   f - find')
    print('   a - add new entry')
    print('   d - delete')
    print('   l - list all')
    print('   q - quit')
    command = input('command: ?')
    print()

    return command.lower()


def find():
    """prompt for a nickname, then perform a case insensitive search for the name, address and phone number associated with that nickname key and display the details."""

    print("'find' - press <ENTER> to abort")

    while True:
        find = input("Find entry for nickname: ")
        print()                                                                 # add a line break before displaying the output
        if find == "":                                                          # abort the input command if the user enters an empty string
            break
        elif find.title() not in list(key.title() for key in contacts.keys()):
            print("'{}' was not found in your contacts".format(find))           # return to find input loop if no case insensitive matches were found
        elif find.title() in list(key.title() for key in contacts.keys()):
            for key in list(contacts.keys()):
                if find.title() == key.title():                                 # iterate over every case insensitive match in contacts
                    nickname = False

                    while not nickname:
                        print("nickname: {}".format(key))                       # use the matched key as the nickname for each match
                        nickname = True
                        for field in contacts[key]:
                            print("{}: {}".format(field, contacts[key][field])) # display the details of the contact found in contacts
                        print()                                                 # add a line break after displaying the output
            break                                                               # exit the function after displaying all details for all case insensitive matches in contacts


def add_new_entry():
    """prompt separately for each of name, address, phone-no and nickname, then save all of these fields into a data structure"""

    print("'add new entry' - press <ENTER> to abort")
    confirm_add_new_entry = False

    while not confirm_add_new_entry:
        nickname = input("Enter nickname: ")
        if nickname == "":                                      # abort the input command if the user enters an empty string
            print()                                             # add a line break before returning to the contacts menu
            return
        elif nickname.title() in contacts.keys():                       # check to see if the nickname is already in the contacts

            while True:
                confirm_replace = input("The nickname '{}' is already in your contacts, do you want to replace the existing entry? (Y/N): ".format(nickname.title()))
                if confirm_replace.upper() == "N":              # if the user doesn't want to replace the existing entry, return to the nickname input loop
                    break
                elif confirm_replace.upper() == "Y":            # if the user wants to replace the existing entry, proceed to entering details
                    confirm_add_new_entry = True
                    break
                else:
                    print("Enter 'Y' for yes or 'N' for no")    # print error message if the user did not input Y or N

        elif nickname.title() not in contacts.keys():                   # if a new nickname is entered, proceed to entering details
            confirm_add_new_entry = True

    if confirm_add_new_entry:                                   # proceed to entering details
        name = input("Enter full name: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        contacts[nickname.title()] = {"name":name, "address":address, "phone":phone}
        print("\nNew entry added to your contacts:\n")
        print("nickname: {}".format(nickname.title()))
        for key in contacts[nickname.title()]:
            print("{}: {}".format(key, contacts[nickname.title()][key]))
        print()                                                 # add a line break after displaying the output


def delete():
    """prompt for a nickname, then find and display the related entry. Ask the user if this is the correct one to be deleted. If they reply "yes" delete it"""
    
    print("'delete' - press <ENTER> to abort")
    delete_from_contacts = False

    while not delete_from_contacts:
        delete = input("Delete entry for nickname: ")
        if delete == "":                                            # abort the input command if the user enters an empty string
            print()                                                 # add a line break before returning to the contacts menu
            return
        elif delete.title() not in contacts.keys():
            print("\n'{}' was not found in your contacts\n".format(delete.title()))
        elif delete.title() in contacts.keys():
            print("\nFound the following entry in your contacts:\n")
            print("nickname: {}".format(delete.title()))
            for key in contacts[delete.title()]:
                print("{}: {}".format(key, contacts[delete.title()][key]))  # display the contact to be deleted

            while True:
                confirm_delete = input("\nIs this the entry you want to delete from your contacts? (Y/N): ")
                if confirm_delete.upper() == "N":                   # if the user doesn't want to delete the existing entry, return to the nickname input loop
                    break
                elif confirm_delete.upper() == "Y":                 # if the user wants to delete the existing entry, proceed to deleting the entry
                    delete_from_contacts = True
                    break
                else:
                    print("\nEnter 'Y' for yes or 'N' for no")      # print error message if the user did not input Y or N

    if delete_from_contacts:
        contacts.pop(delete.title())                                        # remove the key and its values from contacts
        print("\nRemoved entry for '{}' from contacts".format(delete.title()))
        print()                                                     # add a line break after displaying the output


def list_all():
    """display a sequentially numbered list of all fields for all entries in the address book"""

    for contact in contacts.keys():
        print("Contact Entry: {}".format(list(contacts.keys()).index(contact)+1))   # display the number of each entry in contacts
        print("nickname: {}".format(contact))
        for key in contacts[contact]:
            print("{}: {}".format(key, contacts[contact][key]))                     # display the details of each entry in contacts
        print()                                                                     # add a line break after displaying each entry


def quit():
    """quit the program"""
    
    print("Quitting program...")


while True:
    cmd = get_menu_option() # Display the menu and return a valid option
    if cmd == 'f':          # Find - prompt for a nickname, then perform a case insensitive search for the name, address and phone number of every case-insensitive matched nickname in the address book and display their details.
        find()
    elif cmd == 'a':        # Add new entry - prompt separately for each of name, address, phone-no and nickname, then save all of these fields into a data structure.
        add_new_entry()
    elif cmd == 'd':        # Delete - prompt for a nickname, then find and display the related entry. Ask the user if this is the correct one to be deleted. If they reply "yes" delete it.
        delete()
    elif cmd == 'l':        # List all - display a sequentially numbered list of all fields for all entries in the address book
        list_all()
    elif cmd == 'q':        # Quit - quit the program
        quit()
        break
