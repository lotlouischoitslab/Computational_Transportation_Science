# Class and Object:
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}'s engine started")

# Creating objects
car1 = Car("Tesla", "Model 3")
car2 = Car("Hyundai", "Kona")

# Accessing attributes and methods
print(car1.make)  # Output: Toyota
car2.start_engine()  # Output: Honda Civic's engine started

# Constructor:
class Dog:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is born")


dog1 = Dog("Buddy")


# Inheritance:
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog("Canine")
cat = Cat("Feline")

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!


# Polymorphism
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()} m^2")


class Parent:
    def show(self):
        print("Parent's show method")

class Child(Parent):
    def show(self):
        print("Child's show method")

child = Child()
child.show()  # Output: Child's show method
