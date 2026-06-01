from faker import Faker
import pandas as pd

def create_sub_category_data():

    fake = Faker('en_TH')

    # seed 92 is initialized to guarantee deterministic record generation
    SEED = 92
    fake.seed_instance(SEED)

    # Load Product Category data
    product_category_df = pd.read_csv('Dataset/Product_Category/Product_Category_Data.csv')

    # Convert date
    product_category_df['Created_At'] = pd.to_datetime(product_category_df['Created_At']).dt.date

    # Create dictionaries for quick lookups
    category_id_map = dict(
        zip(
            product_category_df['Category_Name'],
            product_category_df['Category_ID']
        )
    )

    category_created_at_map = dict(
        zip(
            product_category_df['Category_Name'],
            product_category_df['Created_At']
        )
    )

    # Product Category -> Sub Category Mapping
    sub_category_mapping = {
        "Mattress": [
            "Foam",
            "Spring",
            "Pocket Spring"
        ],
        "Bedsheet": [
            "Cotton",
            "Polyester",
            "Linen"
        ],
        "Pillow": [
            "Cotton",
            "Feather",
            "Polyester"
        ],
        "Bolster": [
            "Cotton",
            "Feather",
            "Polyester"
        ],
        "Blanket": [
            "Cotton",
            "Flannel",
            "Fleece"
        ]
    }

    # Lists
    Sub_Category_ID = []
    Sub_Category_Name = []
    Category_ID = []
    Created_At = []

    # Generate Sub Categories
    for category, sub_categories in sub_category_mapping.items():

        for sub_category in sub_categories:

            prefix_id = 'SUBCAT_'
            Sub_Category_ID.append(prefix_id + fake.unique.uuid4()[:4])

            Sub_Category_Name.append(sub_category)

            Category_ID.append(category_id_map[category])

            # Sub category cannot exist before parent category
            Created_At.append(category_created_at_map[category])

    # Create DataFrame
    Product_Sub_Category = pd.DataFrame({
        'Sub_Category_ID': Sub_Category_ID,
        'Sub_Category_Name': Sub_Category_Name,
        'Category_ID': Category_ID,
        'Created_At': Created_At
    })

    return Product_Sub_Category


# Generate dataset
Product_Sub_Category = create_sub_category_data()
Product_Sub_Category.to_csv('Dataset/Product_Sub_Category/Product_Sub_Category_Data.csv', index=False)