class Character:
    def __init__(self, name, hp=20, attack=10,) -> None:
        self.name = name
        self.hp = hp
        self.attack = attack

    def basic_attack(self, other):
        x = other.hp - self.attack
        other.hp = x
        print(other.name, 'hp is now =', other.hp)


class Druid(Character):
    def __init__(self, name, hp=20, attack=10) -> None:
        super().__init__(name, hp, attack)

    def meditate(self):
        self.attack -= 2
        self.hp += 10

    def animal_help(self):
        self.attack += 2

    def fight(self, other):
        other.hp -= 0.75*self.life + 0.75*self.attack


class Warrior(Character):
    def __init__(self, name, hp=20, attack=10) -> None:
        super().__init__(name, hp, attack)

    def brawl(self, other):
        other.hp -= 2*self.attack
        self.hp += 0.5*self.attack

    def train(self):
        self.hp += 2
        self.attack += 2

    def roar(self, other):
        other.attack -= 3
