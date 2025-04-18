class Bird:
    def fly(self):
        return "Flying in the sky."
    
class Airplane:
    def fly(self):
        return "Flying through the clouds."
    
def make_it_fly(flyable_object):
    print(flyable_object.fly())

parrot = Bird()
boeing = Airplane()

make_it_fly(parrot)
make_it_fly(boeing)