from faker import Faker
import pandas as pd
import random
import datetime

def create_synthetic_data():
    fake = Faker('zh_CN')
    random.seed(92)
    fake.seed_instance(92)

    Manufacturer_ID = []
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

        if name == 'Foshan Mattress Co., Ltd.':
            City.append('Foshan')
            Created_At.append(datetime.date(2025,1,1))
        else:            
            City.append('Nantong')
            Created_At.append(datetime.date(2025,4,1))

        Country.append('China')

        Contact_Email.append(fake.unique.free_email())

        prefix_phone = '+86'
        phone = fake.unique.numerify(prefix_phone + '-###-####-####')
        Contact_Phone.append(phone)

        prefix = 'MFG_'
        Manufacturer_ID.append(prefix + fake.uuid4()[:4])

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
Synthetic_Manufacturer_Data.to_csv('Synthetic_Manufacturer_Data.csv', index=False)