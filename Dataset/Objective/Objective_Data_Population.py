from faker import Faker
import pandas as pd
import random
import datetime

def create_synthetic_data():
    fake = Faker('en_TH')
    # `seed 92` is initialized to guarantee deterministic record generation, ensuring permanent identifier consistency for entity-relationship diagrams (ERDs) and database joins.
    random.seed(92)
    fake.seed_instance(92)

    Objective_ID = []
    Objective_Name = [
    'Increase Revenue',
    'Grow Customer Base',
    'Increase Repeat Purchases',
    'Improve Customer Retention',
    'Improve Cross-Category Adoption',
    'Expand Product Category Penetration',
    ]
    Created_At = []

    for objective in Objective_Name:
        # Distinct entity prefixes, such as `OBJ_` for Objective and `ORD_` for orders, are implemented to prevent identifier collision during table joins. 
        prefix_id = 'OBJ_'
        # Shortened 4-character UUID format is utilized to ensure optimal readability of relational identifiers.
        Objective_ID.append(prefix_id + fake.uuid4()[:4])
        # Simulates evolving real-world business objectives over time.
        if objective == 'Grow Customer Base':
            Created_At.append(datetime.date(2021, 1, 1))
        elif objective == 'Increase Revenue':
            Created_At.append(datetime.date(2022, 1, 1))
        elif objective == 'Improve Customer Retention':
            Created_At.append(datetime.date(2023, 1, 1))
        elif objective in ['Improve Cross-Category Adoption', 'Expand Product Category Penetration']:
            Created_At.append(datetime.date(2024, 1, 1))
        else: 
            Created_At.append(datetime.date(2025, 1, 1))

    Objective = pd.DataFrame({
        'Objective_ID': Objective_ID,
        'Objective_Name': Objective_Name,
        'Created_At': Created_At
    })
    return Objective

Objective_Data_Population = create_synthetic_data()
Objective_Data_Population.to_csv('Objective_Data_Population.csv', index=False)