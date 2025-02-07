import random

from data.data import Person
from faker import Faker

faker = Faker()

def generated_person():
    first_name = faker.first_name()
    last_name = faker.last_name()
    yield Person(
        first_name=first_name,
        last_name=last_name,
        full_name=first_name + " " + last_name,
        email=faker.email(),
        age=random.randint(18, 80),
        salary=random.randint(1000, 10000),
        department=faker.job(),
        current_address=faker.address(),
        permanent_address=faker.address()
    )