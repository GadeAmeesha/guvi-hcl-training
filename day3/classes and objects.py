class Dog:
    # This is a class attribute, shared by all Dog objects
    species = "Canis lupus familiaris"

    # This is the constructor method
    def __init__(self, name, age):
        self.name = name  # This is an instance attribute, unique to each object
        self.age = age    # This is also an instance attribute
    
    # This is a method (a function defined within the class)
    def bark(self):
        print(f"{self.name} says Woof!")
        # Creating two objects (instances) of the Dog class
my_dog = Dog("Buddy", 3)
your_dog = Dog("Lucy", 5)

# Accessing attributes
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
# Output: My dog's name is Buddy and he is 3 years old.

# Calling a method
your_dog.bark()
# Output: Lucy says Woof!