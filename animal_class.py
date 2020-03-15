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
        self.__age = age
        self.colour = colour
        self.heart = heart
        self.brain = brain



    # Age
    # We should be able to retrieve the age
    # We SHOULD NOT be able to change/alter the age without being an admin

    # first let's make the age private
    # create a method that get's the age and returns it

    def get_age(self):     # A getter method - allows access to encapsulated resources
        return self.__age  # inside the class we have access to the private methods.

    # change the sleep method to increment age

    def set_age(self, age = 500):
        # We SHOULD NOT be able to change/alter the age without being an admin

        # fake verification
        password = input("what is the password? ")

        if password == 'password':
            self.__age = age
            return True
        else:
            return False


    def __increment_age(self):
        self.__age += 1


    # defining the method .eat(), .sleep(), .reproduce()

    def eat(self):
        # when it eats it should increment the age
        self.__increment_age()
        # we will do this by calling the __increment_age() method
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
# print(ringo.age)
print(ringo.colour)

# Second Animal
minnie = Animal('Stacey', 234, 'Blue', 'Almost Big', 'Big')

print(minnie.name)

print(ringo.get_age())
print(ringo.set_age(500))
print(ringo.get_age())