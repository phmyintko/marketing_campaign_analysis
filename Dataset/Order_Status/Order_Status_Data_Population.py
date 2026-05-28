from faker import Faker
import pandas as pd
import random
import datetime

def create_synthetic_data():
    fake = Faker('en_TH')
    # `seed 92` is initialized to guarantee deterministic record generation, ensuring permanent identifier consistency for entity-relationship diagrams (ERDs) and database joins.
    SEED = 92
    random.seed(SEED)
    fake.seed_instance(SEED)

    Status_ID = []
    Status = [
        'In Progress', 
        'Completed', 
        'Cancelled', 
        'Returned'
    ]

    for status in Status:
        # Distinct entity prefixes are implemented to prevent identifier collision during table joins. 
        prefix_id = 'STAT_'
        # Shortened 4-character UUID format is utilized to ensure optimal readability of relational identifiers.
        Status_ID.append(prefix_id + fake.unique.uuid4()[:4])

    Order_Status = pd.DataFrame({
        'Status_ID': Status_ID,
        'Status': Status
    })
    return Order_Status

Order_Status_Data_Population = create_synthetic_data()
Order_Status_Data_Population.to_csv('Dataset/Order_Status/Order_Status_Data.csv', index=False)