class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def add_member(self, name, age, gender, is_child):
        member = {'name': name, 'age': age,
                  'gender': gender, 'is_child': is_child}
        self.members.append(member)

    def born(self, **kwargs):
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} was born.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"{self.last_name} family:")
        for member in self.members:
            print(f"- {member['name']}")


class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name}'s power is: {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old.")

    def incredible_presentation(self):
        super().family_presentation()
        for member in self.members:
            print(f"- {member['incredible_name']}: {member['power']}")


# Initial members data
initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False,
        'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False,
        'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

# Create TheIncredibles object
my_family = TheIncredibles('Incredibles', initial_members)

# Call incredible_presentation method
my_family.incredible_presentation()

# Add Baby Jack with unknown power
my_family.born(name='Baby Jack', age=0, gender='Male',
               is_child=True, power='Unknown Power', incredible_name='Jack')

# Call incredible_presentation method again
my_family.incredible_presentation()
