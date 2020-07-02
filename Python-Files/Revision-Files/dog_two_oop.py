class Dog:

    kind_of_animal = "canine"  # class variable - Dangerous

    def bark(self):
        var = self.kind_of_animal
        return "woof"

    def bark(self, eat):
        self.eat = eat  # This cannot be affected other than inside the class - Good practice (Encapsulation)
        return "nom nom nom ..."


jack_the_dog = Dog()

print(jack_the_dog.kind_of_animal)
print(jack_the_dog.bark())

jack_the_dog.kind_of_animal = "fish"  # The variable in the class can be accessed outside the class which is dangerous
print(jack_the_dog.kind_of_animal)  # Now the animals kind is fish which is incorrect...

