class PlayChar:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)


player3 = PlayChar.adding_things(2, 3)
print(player3.age)
