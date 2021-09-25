class User:
    def __init__(self, name, surname, login, email,phone):
        self.name = name
        self.surname = surname
        self.login = login
        self.email = email
        self.phone = phone
        
    def get_info(self):
        return f"Login: {self.login}, name: {self.name} {self.surname}, email: {self.email}"
              
    
user1 = User("Bob", "Johnson", "J25", "JB789@gmail.com", 123456789)
user2 = User("Manu", "Gupta", "motor", "rutter@mail.ru", 987654321)
user3 = User("Abror", "Maripov", "lagoon", "speed345@mail.uz", 456123789)

print(user1.get_info())
print(user3.get_info())
print(user2.get_info())

print(user1.login)
print(user3.phone)
print(user2.surname)
