from faker import Faker
import pandas as pd
import random
import datetime

def create_synthetic_data():
    fake = Faker('en_TH')
    # seed 92 is initialized to guarantee deterministic record generation, ensuring permanent identifier consistency for entity-relationship diagrams (ERDs) and database joins.
    random.seed(92)
    fake.seed_instance(92)

    Payment_ID = []
    Payment_Method = [
        'COD', 
        'Card', 
        'PromptPay', 
        'TrueMoney'
    ]
    Created_At = []

    for method in Payment_Method:
        # Distinct entity prefixes, such as `Pay_` for Payment and `ORD_` for orders, are implemented to prevent identifier collision during table joins. 
        prefix_ID = 'PAY_'
        # Shortened 4-character UUID format is utilized to ensure optimal readability of relational identifiers.
        Payment_ID.append(prefix_ID + fake.uuid4()[:4])
        # Payment methods use fixed dates to simulate realistic rollout timelines.
        if method in ['COD', 'Card', 'PromptPay']:
            Created_At.append(datetime.date(2025,1,1))
        else:
            Created_At.append(datetime.date(2025,4,1))
        
    Payment = pd.DataFrame({
            'Payment_ID': Payment_ID,
            'Payment_Method': Payment_Method,
            'Created_At': Created_At
    })
    return Payment

Payment_Population = create_synthetic_data()
Payment_Population.to_csv('Payment_Population.csv', index=False)