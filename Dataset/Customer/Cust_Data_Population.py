from faker import Faker 
import datetime
import random
import pandas as pd

def create_synthetic_data(n_rows):
    
    fake = Faker('en_TH')
    # seed 92 is initialized to guarantee deterministic record generation, ensuring permanent identifier consistency for entity-relationship diagrams (ERDs) and database joins.
    SEED = 92
    random.seed(SEED)
    fake.seed_instance(SEED)

    Customer_ID = []
    Customer_Name = []
    Email = []
    Phone = []
    Address = []
    District = []
    City = []
    Postal = []
    Region = []
    Date_of_Birth = []
    Gender = []
    Status = []
    Created_At = []

    for i in range(n_rows):
        
        # District entity prefixes are implemented to prevent identifier collision during table joins. 
        prefix_ID = "CUST_"
        Customer_ID.append(prefix_ID + fake.unique.uuid4()[:6])

        # To keep the data looking realistic, `Customer_Names` are decided by gender.
        selected_gender = random.choice(['Male', 'Female', 'Other'])
        Gender.append(selected_gender)
        if selected_gender == 'Male':
            Customer_Name.append(fake.name_male())
        elif selected_gender == 'Female':
            Customer_Name.append(fake.name_female())
        else:
            Customer_Name.append(fake.name())

        Email.append(fake.unique.free_email())

        # force the phone numbers to start with `06`, `08`, or `09` so they look like actual Thai mobile numbers.
        prefix_phone = random.choice(['06', '08', '09'])
        phone = fake.unique.numerify(prefix_phone + '-####-####')
        Phone.append(phone)

        Address.append(fake.street_address())

        District.append(fake.city())

        City.append(fake.city())

        Postal.append(fake.postcode())

        # set custom percentages for customer regions and weigh more for Central and Northern where `Bangkok` and `Chiang Mai` are located.
        Region.append(random.choices(['Northern', 'Northeast', 'Southern', 'Eastern', 'Western', 'Central'], weights=[0.3, 0.15, 0.05, 0.05, 0.05, 0.4])[0])

        # center the ages around 30 years old and std for 7 years to keep the customer base realistic, then calculate the matching date of birth format.
        random_age = int(random.gauss(30, 7))
        random_age = max(18, min(random_age, 70))
        birth_year = datetime.date.today().year - random_age
        random_dob = datetime.date(birth_year, random.randint(1, 12), random.randint(1, 28))
        Date_of_Birth.append(random_dob.strftime('%Y-%m-%d'))

        Status.append(random.choice(['Single', 'Married', 'Divorced', 'Widowed', 'Other']))

        # To simulate customer acquisition momentum, the `Created_At` dates are generated based on Thailand's GDP path from 2021 to 2026. 
        cus_acq = [
        2021,
        2022,
        2023,
        2024,
        2025,
        2026 
        ] 
        cus_acq_weights = [
        0.10, 
        0.12,
        0.23, 
        0.28, 
        0.17, 
        0.10
        ]
        signup_year = random.choices(cus_acq, weights=cus_acq_weights)[0]
        # For 2026, the date range is limited to January 1st to May 28th to reflect the current date and maintain data realism.
        if signup_year == 2026: 
            signup_date = random.randint(1, 5), random.randint(1, 28)
        else:
            signup_date = random.randint(1, 12), random.randint(1, 28)
        random_created_at = datetime.date(signup_year, signup_date[0], signup_date[1])
        Created_At.append(random_created_at.strftime('%Y-%m-%d'))
    
    Customer_Data = pd.DataFrame({
        'Customer_ID': Customer_ID,
        'Customer_Name': Customer_Name,
        'Email': Email,
        'Phone': Phone,
        'Address': Address,
        'District': District,
        'City': City,
        'Postal': Postal,
        'Region': Region,
        'Date_of_Birth': Date_of_Birth,
        'Gender': Gender,
        'Status': Status,
        'Created_At': Created_At
    })
    return Customer_Data

synthetic_customer_data = create_synthetic_data(5000)
synthetic_customer_data.to_csv('Dataset/Customer/Customer_Data.csv', index=False)