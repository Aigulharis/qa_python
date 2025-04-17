import random
from faker import Faker

def generate_random_collector():
    name: ['Гордость и предубеждение', 'Каспер', 'Дом']
    return random.choice(name)

fake = Faker('ru_RU')

def generate_random_collector_name():
    return fake.catch_phrase()

if __name__ == "__main__":
    print(generate_random_collector_name())

