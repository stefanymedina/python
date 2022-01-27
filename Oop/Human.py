#In this example we'll put in practice all about the propierties 
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age > 0:
            self._age = age
        else:
            raise ValueError("The age can't be negative")

    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            raise ValueError("The age can't be negative")
    
    # work with properties
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError("The age can't be negative")

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        self.first , self.last = name.split(" ")      




h1 = Human("Carlos", "Medina", 10)
# If I want to call the h1.age I can't because this is not a property of the
# object, We need to call te method get_age to catch the value of the age
# print(h1.get_age())
#h1.set_age(34)
# print(h1.get_age())

# work with properties, you don't need call method with parentesis 
print(h1.age)
h1.age = 20 # thanks to the @age.setter I don't need call the method with parentesis and pass the value this form
print(h1.age)
print(h1.fullname)
h1.fullname = "Stefany Medina"
print(h1.fullname)