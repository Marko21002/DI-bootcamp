class Animal:  # parent
    def __init__(self, name: str) -> None:
        self.name = name

    def breathing(self):
        out = f'{self.name} breaths'
        print(out)


class Mammal(Animal):  # child
    def __init__(self, name: str, lungs: int) -> None:
        super().__init__(name)
        self.lungs = lungs

    def produce_milk(self):
        out = f'{self.name} produce milk'
        print(out)


class SeaMammal(Mammal):
    def hold_breath(self):
        out = f'{self.name} hold breath'
        print(out)


mammal = Mammal('m', 2)
mammal.breathing()
dolphin = SeaMammal('dolphin', 2)
dolphin.hold_breath()
