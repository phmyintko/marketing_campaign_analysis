from faker import Faker
import pandas as pd
import datetime

def create_synthetic_data():

    fake = Faker('en_TH')
    random.seed(92)
    fake.seed_instance(92)

    Category_ID = []
    Category_Name = [
        'Mattress',
        'Bedsheet',
        'Pillow',
        'Bolster',
        'Blanket'
    ]
    Created_At = []


    for _ in Category_Name:
        prefix_ID = "ProCat_"
        Category_ID.append(prefix_ID + fake.uuid4()[:4])

        if Category_Name == 'Mattress' or Category_Name == 'Bedsheet':
            Created_At.append(datetime.date(2025, 1, 1))
        else:
            Created_At.append(datetime.date(2025, 4, 1))

    Product_Category = pd.DataFrame({
        'Category_ID': Category_ID,
        'Category_Name': Category_Name,
        'Created_At': Created_At
    })
    return Product_Category

synthetic_product_category_data = create_synthetic_data()
synthetic_product_category_data.to_csv('Synthetic_Product_Category_Data.csv', index=False)