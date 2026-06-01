from faker import Faker
import pandas as pd
import random
import datetime

def create_product_category_data():

    fake = Faker('en_TH')
    # `seed 92` is initialized to guarantee deterministic record generation, ensuring permanent identifier consistency for entity-relationship diagrams (ERDs) and database joins.
    SEED = 92
    random.seed(SEED)
    fake.seed_instance(SEED)

    Category_ID = []
    Category_Name = [
        'Mattress',
        'Bedsheet',
        'Pillow',
        'Bolster',
        'Blanket'
    ]
    Created_At = []

    for name in Category_Name:
        # Distinct entity prefixes are implemented to prevent identifier collision during table joins. 
        prefix_ID = "PROCAT_"
        Category_ID.append(prefix_ID + fake.unique.uuid4()[:4])

        # Simulated product-line expansion where Mattress and Bedsheet launch first, followed by Pillow, Bolster, and Blanket in later years.
        if name in ['Mattress', 'Bedsheet']:
            Created_At.append(datetime.date(2021, 1, 1))
        else:
            Created_At.append(datetime.date(2024, 1, 1))

    Product_Category = pd.DataFrame({
        'Category_ID': Category_ID,
        'Category_Name': Category_Name,
        'Created_At': Created_At
    })
    return Product_Category

synthetic_product_category_data = create_product_category_data()
synthetic_product_category_data.to_csv('Dataset/Product_Category/Product_Category_Data.csv', index=False)