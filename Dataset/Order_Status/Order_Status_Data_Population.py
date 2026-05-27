from faker import Faker
import pandas as pd
import random
import datetime

def create_synthetic_data():
    fake = Faker('en_TH')
    # `seed 92` is initialized to guarantee deterministic record generation, ensuring permanent identifier consistency for entity-relationship diagrams (ERDs) and database joins.
    random.seed(92)
    fake.seed_instance(92)

    Status_ID = []
    Status = [
        'In Progress', 
        'Completed', 
        'Cancelled', 
        'Returned'
    ]

    for status in Status:
        # Distinct entity prefixes, such as `STAT_` for Status and `ORD_` for orders, are implemented to prevent identifier collision during table joins. 
        prefix_id = 'STAT_'
        # Shortened 4-character UUID format is utilized to ensure optimal readability of relational identifiers.
        Status_ID.append(prefix_id + fake.uuid4()[:4])

    Order_Status = pd.DataFrame({
        'Status_ID': Status_ID,
        'Status': Status
    })
    return Order_Status

Order_Status_Data_Population = create_synthetic_data()
Order_Status_Data_Population.to_csv('Synthetic_Order_Status_Data.csv', index=False)