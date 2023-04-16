import random
from ex2 import Dog  # assuming the previous exercise was saved in a file named dog.py


class PetDog(Dog):
    def __init__(self, name, age, weight, power, trained=False):
        super().__init__(name, age, weight, power)  # call the parent class constructor
        self.trained = trained

    def train(self):
        self.trained = True
        bark_output = self.bark()
        print(bark_output)
        return self.trained

    def play(self, *dog_names):
        dog_names = list(dog_names)
        dog_names.append(self.name)
        print(" ".join(dog_names), "all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet")


dog1 = PetDog("Max", 2, 10, 2)
dog2 = PetDog("Buddy", 3, 15, 2)
dog3 = PetDog("Charlie", 4, 20, 2)

dog1.train()
dog1.play(dog2.name, dog3.name)
dog1.do_a_trick()

dog2.train()
dog2.play(dog1.name, dog3.name)
dog2.do_a_trick()

dog3.train()
dog3.play(dog1.name, dog2.name)
dog3.do_a_trick()
