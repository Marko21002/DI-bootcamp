# Ex1
class Pets():
    def __init__(self, animals):
        self.animals = animals
        self.animals = []

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat(Pets):
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}"

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class sarah_pets(Pets):
    def __init__(self, animals):
        super().__init__(animals)
        self.animals = animals

    def get_cats(self):

        for animal in self.animals:
            print(animal)


x = Siamese('Marko', 12)
y = Chartreux('Marko', 12)
z = Bengal('Marko', 12)
all_cats = [x, y, z]

catos = sarah_pets(all_cats)

catos.walk()
