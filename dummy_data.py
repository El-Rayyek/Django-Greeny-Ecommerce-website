import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from faker import Faker
import random
from products.models import Product , Brand , Category


def seed_brand(n):  #20
    fake = Faker()

    images = [
        '1.jpg','2.jpg','3.jpg','4.jpg','5.jpg',
        '6.jpg','7.jpg','8.jpg','9.jpg','10.jpg',
        '11.jpg','12.jpg','13.jpg','14.jpg','15.jpg'
    ]

    for _ in range(n):    
        name = fake.name()
        image = f"Brand/{images[random.randint(0,14)]}"

        Brand.objects.create(
            name = name,
            image = image,
            )
    print(f"Seed {n} Brands")

def seed_category(n): #20
    fake = Faker()

    images = [
        '1.jpg','2.jpg','3.jpg','4.jpg','5.jpg',
        '6.jpg','7.jpg','8.jpg','9.jpg','10.jpg',
        '11.jpg','12.jpg','13.jpg','14.jpg','15.jpg',
    ]

    for _ in range(n):    
        name = fake.name()
        image = f"Category/{images[random.randint(0,14)]}"

        Category.objects.create(
            name = name,
            image = image,
            )    
    
    print(f"Seed {n} Category")


def seed_products(n):
    fake = Faker()
    
    flag_type = ['New','Feature']
    images = ['1.jpg','2.jpg','3.jpg','4.jpg',
              '5.jpg','6.jpg','7.jpg','8.jpg',
              '9.jpg','10.jpg','11.jpg','12.jpg','13.jpg']

    for _ in range(n):
        name = fake.name()
        SKU = random.randint(1,100000)
        brand = Brand.objects.get(id = random.randint(1,20))
        price = round( random.uniform(20.99,99.00),2)
        desc = fake.text()
        flag = flag_type[random.randint(0,1)]
        category = Category.objects.get(id = random.randint(1,20))
        image = f"products/{images[random.randint(0,12)]}"

        Product.objects.create(
            name = name,
            SKU = SKU,
            brand = brand,
            price = price,
            desc = desc ,
            flag = flag,
            category = category,
            image = image
        )
    print(f"Seed {n} Products")


# seed_brand(20)
# seed_category(20)
seed_products(1000)