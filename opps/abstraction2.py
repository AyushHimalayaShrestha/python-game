from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        return "Meow!"
class Dog(Animal):
    def sound(self):
        return "Woof!"

animal =[Cat(),Dog()]
for a in animal :
    print(a.sound())