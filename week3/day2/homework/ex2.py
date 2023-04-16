class Dog:
    def __init__(self, name, age, weight, power):
        self.name = name
        self.age = age
        self.weight = weight
        self.power = power

    def bark(self):
        print(f'{self.name} is barking')

    def run_speed(self):
        speed = self.weight/self.age * 10
        return speed

    def fight(self):
        fight_power = (self.weight/self.age * 10) * self.weight
        self.power = fight_power
        return self.power

    def compare_attribute(self, other1, other2, attribute):
        max_person = self
        if getattr(other1, attribute) > getattr(max_person, attribute):  # getattr - take atribute
            max_person = other1
        if getattr(other2, attribute) > getattr(max_person, attribute):
            max_person = other2
        return max_person.name


x = Dog('Marko', 23, 23, 2)
# x.bark()
x.fight()
y = Dog('Gregori', 10, 90, 3)
y.fight()
z = Dog('Valera', 15, 160, 2)
z.fight()
strongest = x.compare_attribute(y, z, "power")
# print(f"{strongest} is the strongest person.")
