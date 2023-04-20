from faker import Faker

fake = Faker()
users = []


def add_user():
    name = fake.name()
    address = fake.address()
    language_code = fake.language_code()
    users.append({'name': name, 'address': address,
                 'language_code': language_code})


# Add three users to the list
add_user()
add_user()
add_user()

# Print the list of users
print(users)
