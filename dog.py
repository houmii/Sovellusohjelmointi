
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age, kennel): #1) Modify the Dog class by adding one new attribute and one new method. Use your imagination. (0,5 point) ok
        self.name = name
        self.age = age
        self.kennel = kennel

    def sit(self):
        """Simulate a dog sittin in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate dog rolling over response to a command."""
        print(f"{self.name} rolled over!.")

    def escape(self): #1) Modify the Dog class by adding one new attribute and one new method. Use your imagination. (0,5 point) ok
        """Simulate dog escape over response to a command."""
        print(f"{self.name} escaped!")

my_dog = Dog('Sylvi', 8, 'Helsingin pentutehdas') #2)Create a new instance from the Dog class. (0,5 point) ok
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
