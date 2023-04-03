class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def __lt__(self, other):
        return self.age < other.age


x = Cat('x', 24)
y = Cat('y', 23)
z = Cat('z', 22)

g = x > y

if g == True:
    i = x > z
    if i == True:
        print('x is the biggest')
    else:
        print('z is the biggest')
else:
    l = y > z
    if l == True:
        print('y is the biggest')
    else:
        print('z is the biggest')


class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f'{self.name} said wooof!!!')

    def jump(self):
        jm = self.height * 2
        print(f'{self.name} jumped on {jm}')


dog1 = Dog('Marko', 190)
dog2 = Dog('Gena', 20)
dog3 = Dog('Tobias', 35)
dog1.bark()
dog2.jump()

davids_dog = Dog('Rex', 50)
davids_dog.bark()
davids_dog.jump()
sarah_dog = Dog('teacup', 20)
sarah_dog.bark()
sarah_dog.jump()
if sarah_dog.height > davids_dog.height:
    print("srah dog bigger")
else:
    print('sarah dog small')


class song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print(line)


stairway = song(["There’s a lady who's sure", "all that glitters is gold",
                "and she’s buying a stairway to heaven"])
stairway.sing()


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the {self.name} zoo.")
        else:
            print(f"{new_animal} is already in the {self.name} zoo.")

    def get_animals(self):
        print(f"Animals in {self.name} zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from the {self.name} zoo.")
        else:
            print(f"{animal_sold} is not in the {self.name} zoo.")

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            if animal[0] in sorted_animals:
                sorted_animals[animal[0]].append(animal)
            else:
                sorted_animals[animal[0]] = [animal]
        sorted_animals = dict(sorted(sorted_animals.items()))
        for i, animals in enumerate(sorted_animals.values(), 1):
            if len(animals) == 1:
                print(f"{i}: {animals[0]}")
            else:
                print(f"{i}: {animals}")

    def get_groups(self):
        self.sort_animals()


# create an object of the Zoo class
ramat_gan_safari = Zoo("Ramat Gan Safari")

# call the methods of the Zoo class
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Gorilla")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.add_animal("Eagle")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Lion")
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()
