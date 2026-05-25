from faker import Faker
import datetime
import random
import numpy as np
import pandas as pd


def create_synthetic_data(n_rows):
    
    fake = Faker('en_TH')
    random.seed(92)
    fake.seed_instance(92)

    Customer_ID = []
    Customer_Name = []
    Email = []
    Phone = []
    Address = []
    Distinct = []
    City = []
    Postal = []
    Region = []
    Date_of_Birth = []
    Gender = []
    Status = []
    Created_At = []

    for i in range(n_rows):

        prefix_ID = "CUST_"
        Customer_ID.append(prefix_ID + fake.uuid4()[:4])

        selected_gender = random.choice(['Male', 'Female', 'Other'])
        Gender.append(selected_gender)
        if selected_gender == 'Male':
            Customer_Name.append(fake.name_male())
        elif selected_gender == 'Female':
            Customer_Name.append(fake.name_female())
        else:
            Customer_Name.append(fake.name())

        Email.append(fake.unique.free_email())

        prefix_phone = random.choice(['06', '08', '09'])
        phone = fake.unique.numerify(prefix_phone + '-####-####')
        Phone.append(phone)

        Address.append(fake.street_address())

        Distinct.append(fake.city())

        City.append(fake.city())

        Postal.append(fake.postcode())

        Region.append(random.choices(['Northern', 'Northeast', 'Southern', 'Eastern', 'Western', 'Central'], weights=[0.3, 0.15, 0.05, 0.05, 0.05, 0.4])[0])

        random_age = int(random.gauss(30, 7))
        random_age = max(18, min(random_age, 70))
        birth_year = datetime.date.today().year - random_age
        random_dob = datetime.date(birth_year, random.randint(1, 12), random.randint(1, 28))
        Date_of_Birth.append(random_dob.strftime('%Y-%m-%d'))

        Status.append(random.choice(['Single', 'Married', 'Divorced', 'Widowed', 'Other']))

        start_date = datetime.date(2025, 1, 1)
        end_date = datetime.date.today()
        Created_At.append(fake.date_between(start_date=start_date, end_date=end_date))

    Customer_Data = pd.DataFrame({
        'Customer_ID': Customer_ID,
        'Customer_Name': Customer_Name,
        'Email': Email,
        'Phone': Phone,
        'Address': Address,
        'Distinct': Distinct,
        'City': City,
        'Postal': Postal,
        'Region': Region,
        'Date_of_Birth': Date_of_Birth,
        'Gender': Gender,
        'Status': Status,
        'Created_At': Created_At
    })
    return Customer_Data

synthetic_customer_data = create_synthetic_data(1000)
synthetic_customer_data.to_csv('synthetic_customer_data.csv', index=False)