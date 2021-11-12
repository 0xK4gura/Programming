 # 2 class that are very similar
 # class called Dog and Cat

# The Usual Way
"""
# class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow")
# class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self): # the only differences between both are just speak
        print("Bark")
"""

# Inheritance Way
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet): # notice the bracket inside
    def __init__(self, name, age, color):
        super().__init__(name, age) # super means to reference from the parent class, __init__ is the function from that class we want to refer to
        self.color = color
    
    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34, "Blue") # notice that in Cat function there is no "show" function but still called upon, so it inherited from Pet
c.show()
d = Dog("Jill", 25)
d.speak()

# Refered to TechWithTim as guidelines and deeper understanding; https://www.youtube.com/watch?v=JeznW_7DlB0
