class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name,hp,level)

    def speak(self):
        return  "{0} says: 'I heard monsters running around last night!'".format(self.name)

p1 = NPC("bob", 100, 12)
print(p1.name)
print(p1.hp)
print(p1.level)
print(p1.speak())