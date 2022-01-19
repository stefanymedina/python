#A user class with both instance attribute and instance method
class User:
    active_user = 0
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_user += 1
    
    @classmethod # this is a class method that opera away of the object and don't have direct relation
    def display_active_user(cls):
        return f"there are currently {cls.active_user} active users"
    @classmethod
    def from_string_to_name(cls, fullNameage):
        first,last,age = fullNameage.split(',')
        return cls(first,last,age)

    def logout(self):
        User.active_user -= 1
        return f"{self.first} has logout"
    def fullName(self):
            return f"{self.first} {self.last}"
    def initial(self):
        return f"{self.first[0]}.{self.last[0]}"
    def like(self, word):
        return f"{self.first} like {word}"
    
    
        
# u1 = User(first='Stefany', last='Medina', age=24)
# print(u1.logout())
# print(u1.like('draw'))
u2 = User.from_string_to_name("Stefany,Medina,25")
print(u2.like("smile"))






