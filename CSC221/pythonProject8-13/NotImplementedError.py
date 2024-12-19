class Animal:
    def make_sound(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
try:
    generic_animal = Animal()
    generic_animal.make_sound()  # This will raise NotImplementedError
except NotImplementedError as e:
    print(f"Error: {e}")

dog = Dog()
print(dog.make_sound())  # Output: Woof!

cat = Cat()
print(cat.make_sound())  # Output: Meow!
