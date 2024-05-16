class Client:
    def __init__(self, name, email, *dependents):
        self.name = name
        self.email = email
        self.dependents = dependents    
    def to_csv(self):
        return self.name + "," + self.email  + "," + str(self.dependents)
    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, dependents: {self.dependents}"
    
class RegisteredClient(Client):
    def __init__(self, id, name, email, *dependents):
        super().__init__(name, email, *dependents)
        self.id = id
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, email: {self.email}, dependents: {self.dependents}"

reg_client1 = RegisteredClient(1, "Fred", "fred@gmail.com", "Alfredo", "Frida")
print(reg_client1)