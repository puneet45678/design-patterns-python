"""
Pattern name - SingleTon
Pattern type - Creational Design Pattern
"""


# Solution - 4
class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        print(cls.__instances)
        return cls.__instances[cls]

# SingletonMeta overrides the __call__ method (which gets called when a class is instantiated). This method checks if the class has already been instantiated before (i.e., if an instance exists in the __instances dictionary). If not, it creates a new instance; otherwise, it returns the existing one.

# DBConnector is then defined with SingletonMeta as its metaclass. This means that when DBConnector is instantiated, it's the __call__ method of SingletonMeta that gets executed. 
class DBConnector(metaclass=SingletonMeta):
    def __init__(self):
        self.status = "Not Connected"

    def disconnect(self):
        self.status = "Disconnected"

    def connect(self):
        self.status = "Connected"


client1 = DBConnector()
print("Client 1 ", client1)
print(client1.status)

client2 = DBConnector()
print("Client 2 ", client2)
client2.connect()
print(client1.status)

client1.disconnect()
print(client2.status)
