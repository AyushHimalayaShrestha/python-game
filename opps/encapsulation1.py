# Encapsulation is the bundle of data (attributes) and methods (functions) that operates on single data into a single unit (class). It restricts direct access to some of the objects components.
class Dog:
    def __init__(self,name,age):
        self.__name = name,
        self.__age = age,
    def bark(self):
        return f"{self.__name} says woof!"
    def get_age(self):
        return self.__age
    
my_dog =Dog("Buddy",3)
print(my_dog.bark())
print(f"My dog's age is:{my_dog.get_age()}")