import random

from data.data import Person
from faker import Faker

faker_ru = Faker("ru_RU")

def generated_person():
    first_name = faker_ru.first_name()
    last_name = faker_ru.last_name()
    yield Person(
        first_name=first_name,
        last_name=last_name,
        full_name=first_name + " " + last_name,
        email=faker_ru.email(),
        age=random.randint(18, 80),
        salary=random.randint(1000, 10000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )