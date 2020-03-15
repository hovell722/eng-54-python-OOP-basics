# OOP Basics

This repo will contain our OOP basics.

We will look at:
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism


## Class
Is like a cookie cutter, that creates instances of cookies.

They wrappers to define how an object looks and behaves.

Classes will wrap characteristics as attributes, and behaviours and methods.

## Methods Vs. Functions
Methods are functions that belong to a specific data type.

Where functions are anonymous and anything can call and run them.

Where as **methods NEED the instance to be called.**

## Characteristics / how an object looks like
These are attributes that are assigned to each instance.
They are variables assigned to an object / instance.

## Instance
Occurrence of something.

## Self
Refers to the instance of on which a method is being called.

self.name = 'ringo'

this means that specific object attributes name will have the string 'ringo'

## Abstraction
The **ability to hide complexity.**

We do this by using:
- separation of concerns
- documentation
    - specify which methods and how to use them
- inheritance --> causes some abstraction

Real life examples are everywhere:
- changing
- heating up food with one button
- using our cards to pass security

## Inheritance
Is the ability to pass to child class all the methods and characteristics.
This is one of the big reasons of OOP - it means you can re-use code!

**promise of reusable code**


## Encapsulation
Making methods or attributes private.

To make something private is to restrict access from external function/methods.

When methods or attributes are private, they can only be called by it own function or within a class.

**This leads to getters and setters**

Syntax:
```python

```


## Polymorphism
Literally means:
    - many forms

It is the ability to **COMPLETELY override methods**, and if need be, recall method from parent class using .super()

## .super()

It represents the parent class, allows you to call methods from parent class.

Usage and case in point:
- Situation where you want to overwrite a method
- You want to add new functionality to the new method
- But still have everything from first method

--->> then you call super()

Most of the times this happened with the __init__ method.
- You want to add new characteristics to child object
- And you want to keep all the original characteristics
- So you overwrite the init method and still call the original init method, with all the necessary arguments.

```python
class Animal():

    # original init method with age and colour_fur
    def __init__(self, age, colour_fur):
        self.age = age
        self.colour_fur = colour_fur


class Reptile(Animal):

    # this overwrites the original init method
    # however, what we want is to keep all the original code and add more code
    def __init__(self, name, age, colour_fur):
        # use super to call original init method
        # we need to pass the arguments for the original init to work
        super().__init__(age, colour_fur)
        self.name = name

rt = Reptile('ringo', 10, 'shiny gold')
```


