from faker import Faker 
import datetime
import random
import pandas as pd

def create_synthetic_data():
    fake = Faker('zh_CN')
    # `seed 92` is initialized to guarantee deterministic record generation, ensuring permanent identifier consistency for entity-relationship diagrams (ERDs) and database joins.
    SEED = 92
    random.seed(SEED)
    fake.seed_instance(SEED)

    Manufacturer_ID = []
    # Manufacturing locations are dynamically assigned based on real-world industrial hubs, mapping mattress production to Foshan and bedding lines to Nantong.
    Manufacturer_Name = [
        'Foshan Mattress Co., Ltd.', 
        'Nantong Bedding Co., Ltd.'
    ]
    City = []
    Country = []
    Contact_Email = []
    Contact_Phone = []
    Created_At = []

    for name in Manufacturer_Name:

        # Distinct entity prefixes are implemented to prevent identifier collision during table joins. 
        prefix_ID = 'MFG_'
        # Shortened 4-character UUID format is utilized to ensure optimal readability of relational identifiers.
        Manufacturer_ID.append(prefix_ID + fake.unique.uuid4()[:4])

        # Location and creation dates use fixed dates to simulate realistic rollout timelines.
        if name == 'Foshan Mattress Co., Ltd.':
            City.append('Foshan')
            Created_At.append(datetime.date(2021, 1, 1))
        else:            
            City.append('Nantong')
            Created_At.append(datetime.date(2024, 1, 1))

        Contact_Email.append(fake.unique.free_email())
        Country.append('China')

        prefix_phone = '+86'
        phone = fake.unique.numerify(prefix_phone + '-###-####-####')
        Contact_Phone.append(phone)

    Manufacturer = pd.DataFrame({
        'Manufacturer_ID': Manufacturer_ID,
        'Manufacturer_Name': Manufacturer_Name,
        'City': City,
        'Country': Country,
        'Contact_Email': Contact_Email,
        'Contact_Phone': Contact_Phone,
        'Created_At': Created_At
    })
    return Manufacturer

Synthetic_Manufacturer_Data = create_synthetic_data()
Synthetic_Manufacturer_Data.to_csv('Dataset/Manufacturer/Manufacturer_Data.csv', index=False)