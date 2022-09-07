# Initializing Dictionaries
phonebook1 = {}
phonebook1["John"] = 938477566
phonebook1["Jack"] = 938377264
phonebook1["Jill"] = 947662781
print(phonebook1)

phonebook2 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook2)

# Deleting Queries
del phonebook1["John"]

phonebook2.pop("John")

for name, number in phonebook1.items():
    print("Phone number of %s is %d" % (name, number))