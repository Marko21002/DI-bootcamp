from copy import copy, deepcopy

class Car:

    def __init__(self, speed): 
        self.speed = speed
        self.owners = []

    # > - greater than
    def __gt__(self, other_car): 
        return self.speed > other_car.speed
    
    # < - less than
    def __lt__(self, other_car):
        return self.speed < other_car.speed
    
    def __eq__(self, other_car):
        return self.speed == other_car.speed
    
    # +
    def __add__(self, other_car):
        return self.speed + other_car.speed

    # - 

    # += 
    def __iadd__(self, other_car): 
        self.speed += other_car.speed
        return self

    def copy(self):
        return deepcopy(self)
    
    # def __setattr__(self, __name: str, __value: Any) -> None:
    #     pass


car1 = Car(200)
car1.owners = ['Bill', 'Am']
car2 = Car(300)
car2.owners = ['Adam', 'Eve']

car1 += car2
car1 = car2.copy()

car2.owners = ['HDFDSF']

print(id(car1))
print(id(car2))

print(car1.owners)
print(car2.owners)

