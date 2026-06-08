from faker import Faker
import pandas as pd
import datetime

def create_product_data():

    fake = Faker('en_TH')
    SEED = 92
    fake.seed_instance(SEED)

    #import csv and covert string to date
    category_df = pd.read_csv('Dataset/Product_Category/Product_Category_Data.csv', 
    parse_dates=[
        'Created_At'
    ]
    )
    sub_category_df = pd.read_csv('Dataset/Product_Sub_Category/Product_Sub_Category_Data.csv',
    parse_dates=[
        'Created_At'
    ]
    )

    ###mapping
    #manufacturer_id map
    manufacturer_map = {
        'Mattress': 'MFG_8cd2',
        'Bedsheet': 'MFG_ba3a',
        'Pillow': 'MFG_ba3a',
        'Bolster': 'MFG_ba3a',
        'Blanket': 'MFG_ba3a'
    }
    #size and color map based on product category
    size_map = {
        'Mattress': ['Single', 'Queen', 'King'],
        'Bedsheet': ['Single', 'Queen', 'King'],
        'Pillow': ['One Size'],
        'Bolster': ['One Size'],
        'Blanket': ['Single', 'Queen', 'King']
    }
    color_map = {
        'Mattress': ['Color', 'Pattern'],
        'Bedsheet': ['Color', 'Pattern', 'Graphic'],
        'Pillow': ['Color', 'Pattern', 'Graphic'],
        'Bolster': ['Color', 'Pattern', 'Graphic'],
        'Blanket': ['Color', 'Pattern', 'Graphic']
    }
    #price map based on category and size
    price_map = {
    'Mattress': {
        'Foam': {'Single': 3500, 'Queen': 5500, 'King': 7500},
        'Spring': {'Single': 4000, 'Queen': 6000, 'King': 8000},
        'Pocket Spring': {'Single': 8500, 'Queen': 13000, 'King': 17500}
    },
    'Bedsheet': {
        'Cotton': {'Single': 800, 'Queen': 1200, 'King': 1500},
        'Polyester': {'Single': 400, 'Queen': 500, 'King': 600},
        'Linen': {'Single': 2000, 'Queen': 3800, 'King': 4200}
    },
    'Pillow': {
        'Cotton': {'One Size': 250},
        'Feather': {'One Size': 650},
        'Polyester': {'One Size': 180}
    },
    'Bolster': {
        'Cotton': {'One Size': 300},
        'Feather': {'One Size': 700},
        'Polyester': {'One Size': 220}
    },
    'Blanket': {
        'Cotton': {'Single': 1200, 'Queen': 2000, 'King': 2200},
        'Flannel': {'Single': 600, 'Queen': 1000, 'King': 1200.00},
        'Fleece': {'Single': 300, 'Queen': 600, 'King': 700}
        }
    }
    #weight map based on category and size
    weight_map = {
    'Mattress': {
        'Foam': {'Single': 40, 'Queen': 60, 'King': 70},
        'Spring': {'Single': 50, 'Queen': 80, 'King': 90},
        'Pocket Spring': {'Single': 80, 'Queen': 100, 'King': 110}
    },
    'Bedsheet': {
        'Cotton': {'Single': 2, 'Queen': 3, 'King': 4},
        'Polyester': {'Single': 1.5, 'Queen': 2.2, 'King': 3.0},
        'Linen': {'Single': 2.5, 'Queen': 3.5, 'King': 4.5}
    },
    'Blanket': {
        'Cotton': {'Single': 2.5, 'Queen': 3.5, 'King': 4.5},
        'Flannel': {'Single': 3, 'Queen': 4, 'King': 5},
        'Fleece': {'Single': 2, 'Queen': 2.8, 'King': 3.5}
    },
    'Pillow': {
        'Cotton': {'One Size': 0.3}, 'Feather': {'One Size': 0.4}, 'Polyester': {'One Size': 0.2}
    },
    'Bolster': {
        'Cotton': {'One Size': 0.4}, 'Feather': {'One Size': 0.5}, 'Polyester': {'One Size': 0.3}
    }
    }

    ###create join table
    #merge two tables based on category id in order to generate product name
    product_join_df = sub_category_df.merge(
        category_df[[
            'Category_ID',
            'Category_Name',
            'Created_At'
        ]],
        on=['Category_ID'],
        how='left'
        )
    #add manufacturer id to the table
    product_join_df['Manufacturer_ID']=(
        product_join_df['Category_Name']
        .map(manufacturer_map)
    )
    #add size and color to the table
    product_join_df['Size'] = product_join_df['Category_Name'].map(size_map)
    product_join_df['Color'] = product_join_df['Category_Name'].map(color_map)
    #explode lists into individual row
    product_join_df = product_join_df.explode('Size')
    product_join_df = product_join_df.explode('Color')

    ##add columns to the table
    #generate naem
    product_join_df['Product_Name'] = (
        product_join_df['Sub_Category_Name']
        + ' '
        + product_join_df['Category_Name']
        + ' '
        + product_join_df['Color']
        + ' '
        + product_join_df['Size']
    )
    #generate product id 
    product_join_df['Product_ID'] = [
        item_category[:3] + item_sub_category[:3] + '_' + fake.unique.uuid4()[:4]
        for item_category, item_sub_category in zip(
            product_join_df['Category_Name'], 
            product_join_df['Sub_Category_Name']
        )
    ]
    #add price look up
    product_join_df['Price'] = [
        price_map.get(item_category, {}).get(item_sub_category, {}).get(item_size, None)
        for item_category, item_sub_category, item_size in zip( 
            product_join_df['Category_Name'], 
            product_join_df['Sub_Category_Name'], 
            product_join_df['Size']
        )
    ]
    #add weight look up
    product_join_df['Weight_lbs'] = [
        weight_map.get(item_category, {}).get(item_sub_category, {}).get(item_size, None)
        for item_category, item_sub_category, item_size in zip(
            product_join_df['Category_Name'], 
            product_join_df['Sub_Category_Name'], 
            product_join_df['Size']
        )
    ]

    ###arrange columns
    columns = [
        'Product_ID',
        'Product_Name',
        'Sub_Category_ID',
        'Size',
        'Weight_lbs',
        'Color',
        'Price',
        'Manufacturer_ID',
        'Created_At'
    ]
    
    #column format
    #get Created_At from right table: sub category
    product_join_df['Created_At']=product_join_df['Created_At_x']
    product_join_df = product_join_df[columns]
    
    ###reset index and delete old index
    product_join_df = product_join_df.reset_index(drop=True)
    
    ###handover
    return product_join_df

product_join_df = create_product_data()
product_join_df.to_csv('Dataset/Product/Product_Data.csv', index=False)