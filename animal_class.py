# define our Animal Class

# Sudocode
# Looks / Characteristics of every animal
    # heart, brain, name, age, colour

# Behaviours / Methods of every animal
    # eat, sleep, reproduce, toilet, make_sound

class Animal():
    pass
    # define behaviour and characteristics

    # define the characteristics of EVERY animal
    def __init__(self, name, age, colour, heart, brain):
        self.name = name
        self.age = age
        self.colour = colour
        self.heart = heart
        self.brain = brain

    # defining the method .eat(), .sleep(), .reproduce()
    def eat(self):
        return 'Nom Nom Nom'

    def sleep(self):
        return 'zzZZzzZZzzZZzz'

    def reproduce(self):
        return "I'm going to need some privacy here... :D"

    def toilet(self):
        return "0_0 HUMMMM!!! o_0 AHHHH!!! SPLOSH! o_o"

    def make_sound(self):
        return 'Woof'

# To call methods we need an object of this class
# Creating an instance of class animal

ringo = Animal('Ringo', 30, 'Green', 'Big', 'Small') # Creates instances of clss animal and assigns to variable ringo

# Checking and print the instance
print(ringo)
print(type(ringo))

# Calling methods on instance of Animal
print(ringo.eat())
print(ringo.toilet())
print(ringo.sleep())

# Check the attribute of an instance
print(ringo.name)
print(ringo.age)
print(ringo.colour)

# Second Animal
minnie = Animal('Stacey', 234, 'Blue', 'Almost Big', 'Big')

print(minnie.name)