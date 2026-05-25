# Synthetic Customer Data Generator

This project generates realistic synthetic customer data for analytics practice, SQL testing, and portfolio projects.

Features:
- Thai-style customer profiles
- Weighted regional distribution
- Realistic age generation 

## Create Synthetic Customer Dataset

This function generates synthetic customer records using Faker and randomized probability distributions.

>I fixed the randomness at **seed 92** like a permanent save point. This keeps long term simulation and realistic timeline. For example, if I later increase the dataset from 1,000 customers to 1,200, the original 1,000 customers will remain unchanged, and the code will simply generate 200 new customers at the end. This makes it realistic in building future analysis projects.
```Python
from faker import Faker 
import datetime
import random
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
```

## Generate Customer Records

I add a prefix like `CUST_` for customers or `ord_` for orders so different IDs never get mixed up when connecting tables.
```Python
    for i in range(n_rows):

        prefix_ID = "CUST_"
        Customer_ID.append(prefix_ID + fake.uuid4()[:4])
```

To keep the data looking realistic, `Customer_Names` are decided by `Gender`. The code looks at the generated gender first: if it’s `Male`, it picks a male name; if it’s `Female`, it picks a female name. This guarantees the names and genders always match up correctly.
```Python
        selected_gender = random.choice(['Male', 'Female', 'Other'])
        Gender.append(selected_gender)
        if selected_gender == 'Male':
            Customer_Name.append(fake.name_male())
        elif selected_gender == 'Female':
            Customer_Name.append(fake.name_female())
        else:
            Customer_Name.append(fake.name())
```

I force the phone numbers to start with `06`, `08`, or `09` so they look like actual Thai mobile numbers.
```Python
        Email.append(fake.unique.free_email())

        prefix_phone = random.choice(['06', '08', '09'])
        phone = fake.unique.numerify(prefix_phone + '-####-####')
        Phone.append(phone)
```

I set custom percentages for customer regions and weigh more for Central and Northern where `Bangkok` and `Chiang Mai` are located.
```Python
        Address.append(fake.street_address())

        Distinct.append(fake.city())

        City.append(fake.city())

        Postal.append(fake.postcode())

        Region.append(random.choices(['Northern', 'Northeast', 'Southern', 'Eastern', 'Western', 'Central'], weights=[0.3, 0.15, 0.05, 0.05, 0.05, 0.4])[0])
```

I center the ages around **30 years old** and **std for 7 years** to keep the customer base realistic, then calculate the matching date of birth format.
```Python
        random_age = int(random.gauss(30, 7))
        random_age = max(18, min(random_age, 70))
        birth_year = datetime.date.today().year - random_age
        random_dob = datetime.date(birth_year, random.randint(1, 12), random.randint(1, 28))
        Date_of_Birth.append(random_dob.strftime('%Y-%m-%d'))

        Status.append(random.choice(['Single', 'Married', 'Divorced', 'Widowed', 'Other']))

        start_date = datetime.date(2025, 1, 1)
        end_date = datetime.date.today()
        Created_At.append(fake.date_between(start_date=start_date, end_date=end_date))
```

## Build Final Pandas DataFrame
```Python
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
```

## Generate Dataset

```Python
synthetic_customer_data = create_synthetic_data(1000)
synthetic_customer_data
```