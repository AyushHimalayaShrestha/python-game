class Animal:
    def speak(self):
        return "some sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())