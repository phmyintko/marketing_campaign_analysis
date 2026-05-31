from faker import Faker
import pandas as pd
import random
import datetime

def create_synthetic_data():
    fake = Faker('en_TH')
    # seed 92 is initialized to guarantee deterministic record generation, ensuring permanent identifier consistency for entity-relationship diagrams (ERDs) and database joins.
    SEED = 92
    random.seed(SEED)
    fake.seed_instance(SEED)

    Channel_ID = []
    Channel_Name = [
        'Physical_Store',
        'Facebook',
        'Line',
        'Shopee',
        'Lazada',
        'Company_Site',
        'Tiktok'
    ]
    Created_At = []

    for channel in Channel_Name:
        # Distinct entity prefixes are implemented to prevent identifier collision during table joins. 
        prefix_id = 'CH_'
        Channel_ID.append(prefix_id + fake.unique.uuid4()[:4])

        if channel in ['Physical_Store', 'Facebook', 'Line', 'Shopee', 'Lazada']:
            Created_At.append(datetime.date(2021, 1, 1))
        # Tiktok marketplace was launched in Thailand in June 2022
        else:
            Created_At.append(datetime.date(2022, 1, 1))

    Channel_Data = pd.DataFrame({
        'Channel_ID': Channel_ID,
        'Channel_Name': Channel_Name,
        'Created_At': Created_At
    })
    return Channel_Data

Synthetic_Channel_Data = create_synthetic_data()
Synthetic_Channel_Data.to_csv('Dataset/Channel/Channel_Data.csv', index=False)