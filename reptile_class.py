from animal_class import *

class Reptile(Animal):

    def __init__(self, name, age, colour, heart, brain, scales, blood_temp):
        super().__init__(name, age, colour, heart, brain)
        self.scales = scales
        self.blood_temp = blood_temp

    def make_sound(self):
        return 'meow'


animal1 = Animal('Nacho', 20, 'Yellowish', 'Big', 'Small')

reptile1 = Reptile('Ringo', 30, 'Yellow', 'Small', 'Big', 'Super toxic and spiky', 'Frozen')

print(animal1)
print(reptile1)


# Reptile has all the attributes and method of Animal
print(reptile1.name) # This is an attribute of reptile not a method

print(reptile1.eat())
print(reptile1.toilet())
print(reptile1.sleep())
print(reptile1.reproduce())
print(reptile1.make_sound())
