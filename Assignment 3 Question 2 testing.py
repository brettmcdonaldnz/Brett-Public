# nickname = ["Brett"]
# names = {"Brett":"Brett McDonald"}
# address = {"Brett":"13 Ronald Woolf Place"}
# phone_number = {"Brett":"0273533606"}
# addressBook = ["Brett"]
# details =
#
#
# print(addressBook)
#
# for item in addressBook:
#     print(item)

#
#

# phone_no = {"Brett": "0273533606"}
# addressBook = {"Brett":address}
# print(names["Brett"])
# print(addressBook["Brett"]["address"])

# Using a dictionary indexed by nickname (a short favourite name), write a simple address book that lets you save these contact details.
# • nickname (can be anything you like)
# • name
# • address
# • phone-no
# Each dictionary entry contains a dictionary of the details of that person, so
# names["Tom"] # will return the dictionary that contains all Tom's details'
# details = names["Tom"]  # details will be a dictionary containing  nickname, address...
# toms_address = details["address"]
# or simply
# address = contacts['Tom']['address']
# will return Tom's address

# name = {"Brett": "Brett McDonald"}
# address = {"Brett": "13 Ronald Woolf Place"}
# phone_no = {"Brett": "0273533606"}
# addressBook = {"Brett":[name,address,phone_no]}
# print(addressBook["Brett"][addressBook["Brett"].index(phone_no)]["Brett"])

# name = {"Brett": "Brett McDonald"}
# address = {"Brett": "13 Ronald Woolf Place"}
# phone_no = {"Brett": "0273533606"}
# addressBook = {"Brett":[name["Brett"],address["Brett"],phone_no["Brett"]]}     # address book with nicknames as keys, and
# print(addressBook["Brett"][addressBook["Brett"].index(name["Brett"])])

# contacts = {"Brett":"cat","BRett":"dog"}
# search = "brett"
# for key in list(contacts.keys()):
#     if search.lower() == key.lower():
#         print(key)
# if search.lower() in list(key.lower() for key in contacts.keys()):
#     print("found")
# # print(list(contacts.keys()))

# method for searching contacts with case insensitivity, then replacing keys while preserving case...
# contacts = {"HK":{"name":"Holder-Something","address":"Trentham","phone":"021"},"Rob":{"name":"Robin","address":"Trentham","phone":"029"}}
# proceed_to_contact_entry = False
# while not proceed_to_contact_entry:
#   nickname = input("Enter nickname: ")  # get the nickname as a search string
#   lower_case_list = [key.lower() for key in list(contacts.keys())] # create a list of lower case keys from contacts
#
#   if nickname == "":
#     break
#
#   if nickname.lower() in lower_case_list: # check if the lower case search string is in the lower case list of keys
#     nickname_index = lower_case_list.index(nickname.lower()) # return the index where the lower case nickname was matched to the lowercase list of keys
#     nickname_key = list(contacts.keys())[lower_case_list.index(nickname.lower())] # return the original key from the dictionary that was matched according to the lower case search string matching a lower case key in contacts
#
#     while True:
#       confirm_replace = input("Found entry for '{}' in your contacts. Do you want to overwrite this entry with '{}'? (Y/N):".format(nickname_key,nickname))
#       if confirm_replace.upper() == "Y":
#         contacts.pop(nickname_key)  # remove the original matched key from the dictionary
#         nickname_key = nickname     # assign the new nickname as the new key to be entered in the dictionary (so that case sensitivity of the new key is preserved)
#         proceed_to_contact_entry = True
#         break
#       elif confirm_replace.upper() == "N":
#         proceed_to_contact_entry = False
#         break
#       else:
#         print("no valid response received")
#
#   elif nickname.lower() not in lower_case_list: # check if the lower case search string is not in the lower case list of keys
#     nickname_key = nickname
#     proceed_to_contact_entry = True
#
# if proceed_to_contact_entry:
#   contacts[nickname_key]={"values..."}
#   print(contacts)
