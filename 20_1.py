def client_info(name, surname, ybirth, pbirth, email='',tel=None):
    """A function that returns information about the client in the form of a dictionary."""
    client = {'name':name,
             'surname':surname,
             'ybirth':ybirth,
             'age':2020-ybirth,
             'pbirth':pbirth,
             'email':email,
             'phone':tel}
    return client

print("Please enter customer details.")
clients =[]
while True:
    name = input("name: ")
    surname = input("Surname: ")
    ybirth = int(input("Year of birth: "))
    pbirth = input("Place of birth: ")
    email = input("Email: ")
    phone = input("phone number: ")
    clients.append(client_info(name, surname, ybirth, pbirth, email, phone))
    javob = input("Will you continue? (yes/no): ")
    if javob!='yes':
        break

print("Clients:")
for client in clients:
    print(f"{client['name'].title()} {client['surname'].title()}," 
          f"{client['age']} years old, phone: {client['phone']}")