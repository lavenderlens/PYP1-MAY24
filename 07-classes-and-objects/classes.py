'''
a class is a template/blueprint for creating objects
you might choose to code a class as an alternative to using dictionaries to represent your data 
'''

class Client:
    # NB every method in a class is automatically and explicitly passed a ref to the current object
    # the ref to the current object is conventionally named "self"

    # every class hould have an __init__ method which is a dunder method (double underscore or magic method)
    # which is called whenever the class is called
    # it is used to set the props and optionally the values on a new object
    def __init__(self):
        self.name = "name"
        self.email = "email"
        self.dependents = []
        self.options = {"contact_preferences": {"mail": False, "email":False, "SMS": False, "telephone": True}}
    
    def to_csv(self):
        return self.name + "," + self.email  + "," + str(self.dependents) + "," + str(self.options)
        pass

client = Client()
# NB the dot notation now used to reference object props
# NOT square brackets as in dictionaries
print(client.name)
print(client.email)
print(client.dependents)
print(client.options)
print(client.to_csv())

# comparisons with dict datatype;
# OBJECTS:
# dot notation for drilling down into props
# DICTIONARIES:
# square bracket notation for drilling down into props

# what if we wished to provide values for our object props at instantiation?
# we pass them in as args to the __init__ function:
class ClientWithParams:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.dependents = []
        self.options = {"contact_preferences": {"mail": False, "email":False, "SMS": False, "telephone": True}}
    
    def to_csv(self):#our own method, arbitrary named, no underscores
        return self.name + "," + self.email  + "," + str(self.dependents) + "," + str(self.options)
    
    # dunder methods __str__ and __repr__ control a meaningful string representation of the object
    # there are subtle differences between the two
    def __str__(self):
        return f"{self.name}, {self.email}, {self.dependents}, {self.options}"
        
# client2 = ClientWithParams()#missing 2 required positional arguments: 'name' and 'email'
client2 = ClientWithParams("Alan", "me@me.com")

# when the object reference is called from print(), the default implementation of __str__ runs 
print(client2)#<__main__.ClientWithParams object at 0x1047cee10> again: <__main__.ClientWithParams object at 0x102ee2e10>
print("explicitly calling the str() function")
print(str(client2))
import datetime
today = datetime.datetime.now()
print(today)#print calls builtin __str__ function #2024-05-16 13:53:29.617877
# __str__ HAS BEEN OVERRIDDEN in datetime
print(str(today))#the builtin str() function ALSO calls the __str__ "under the hood"
print(today.__str__())#explicitly calling __str__ results in the same
print(today.__repr__())#datetime.datetime(2024, 5, 16, 13, 56, 5, 663566)
'''
__str__ and __repr__ dunder/magic methods differ slightly
__str__ prints a meaningful, user-friendly string representation of the object
__repr__ prints a comprehensive, structural string representation of the object
sse ref: https://www.geeksforgeeks.org/str-vs-repr-in-python/
'''