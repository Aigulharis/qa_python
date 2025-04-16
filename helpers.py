import random
from faker import Faker

def generate_random_book():
    titles: ['Гордость и предубеждение', 'Что делать, если ваш кот хочет вас убить', 'Дом']
    return random.choice(titles)

fake = Faker('ru_RU')

def generate_random_book_title():
    return fake.catch_phrase()

if __name__ == "__main__":
    print(generate_random_book_title())
