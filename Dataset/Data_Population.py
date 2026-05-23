from faker import Faker
import random

faker = Faker('en_TH')
faker.seed_instance(92)

NUM = 100
Customer_ID = [i + 1 for i in range(NUM)]
Customer_Names = [faker.name() for _ in range(NUM)]
Email = [faker.email() for _ in range(NUM)]
Phone = [faker.phone_number() for _ in range(NUM)]
City = [faker.city() for _ in range(NUM)]

for i in range(NUM):
    print(f"{Customer_ID[i]},{Customer_Names[i]},{Email[i]},{Phone[i]},{City[i]}")