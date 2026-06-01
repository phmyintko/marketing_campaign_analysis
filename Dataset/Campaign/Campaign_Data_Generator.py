from faker import Faker
import pandas as pd
import random
import datetime

def create_campaign_data():
    fake = Faker('en_TH')
    # seed 92 is initialized to guarantee deterministic record generation, ensuring permanent identifier consistency for entity-relationship diagrams (ERDs) and database joins.
    SEED = 92
    random.seed(SEED)
    fake.seed_instance(SEED)

    Campaign_ID = []
    # created to avoid name length crash
    Campaign_Name_List = [
        'New Year Bedroom Refresh',
        'Valentine Bedding Bundle',
        'Summer Mattress Sale',
        'Happy Songkran',
        'Mid-Year Mega Discount',
        'Free Shipping Month',
        'Rainy Season Bedding Deals',
        'Sleep Better Campaign',
        'Back to School Home Essentials',
        '10.10 Flash Sale',
        '11.11 Mega Sale',
        'Holiday Bundle Promotion'
    ]
    Campaign_Names = []
    Campaign_Type = []
    Start_Date = []
    End_Date = []
    Budget = []
    Target_Audience = []
    Region = []
    Status = []
    Created_At = []

    year_list = [2020, 2021, 2022, 2023, 2024, 2025]

    # LOOP 1 for year
    for year in year_list:
        
        # LOOP 2 for assigned list
        for name in Campaign_Name_List:
            
            # campaign timeline are set strategically to cover festivals and national events.
            # campaign budgets are designed based on Thailand Consumer Spending pattern. Q2 > Q4 > Q3 > Q1. source: tradingeconomics.com
            if name == 'Valentine Bedding Bundle':
                start = datetime.date(year + 1, 1, 24)
                end = datetime.date(year + 1, 2, 17)
                budg = 33000
                created = datetime.date(year + 1, 1, 1)
            elif name == 'Summer Mattress Sale':
                start = datetime.date(year + 1, 2, 24)
                end = datetime.date(year + 1, 3, 17)
                budg = 33000
                created = datetime.date(year + 1, 2, 1)
            elif name == 'Happy Songkran':
                start = datetime.date(year + 1, 3, 24)
                end = datetime.date(year + 1, 4, 17)
                budg = 33000
                created = datetime.date(year + 1, 3, 1)
            elif name == 'Mid-Year Mega Discount':
                start = datetime.date(year + 1, 4, 24)
                end = datetime.date(year + 1, 5, 17)
                budg = 33000
                created = datetime.date(year + 1, 4, 1)
            elif name == 'Free Shipping Month':
                start = datetime.date(year + 1, 5, 24)
                end = datetime.date(year + 1, 6, 17)
                budg = 66000
                created = datetime.date(year + 1, 5, 1)
            elif name == 'Rainy Season Bedding Deals':
                start = datetime.date(year + 1, 6, 24)
                end = datetime.date(year + 1, 7, 17)
                budg = 66000
                created = datetime.date(year + 1, 6, 1)
            elif name == 'Sleep Better Campaign':
                start = datetime.date(year + 1, 7, 24)
                end = datetime.date(year + 1, 8, 17)
                budg = 66000
                created = datetime.date(year + 1, 7, 1)
            elif name == 'Back to School Home Essentials':
                start = datetime.date(year + 1, 8, 24)
                end = datetime.date(year + 1, 9, 17)
                budg = 66000
                created = datetime.date(year + 1, 8, 1)
            elif name == '10.10 Flash Sale':
                start = datetime.date(year + 1, 9, 24)
                end = datetime.date(year + 1, 10, 17)
                budg = 49000
                created = datetime.date(year + 1, 9, 1)
            elif name == '11.11 Mega Sale':
                start = datetime.date(year + 1, 10, 24)
                end = datetime.date(year + 1, 11, 17)
                budg = 49000
                created = datetime.date(year + 1, 10, 1)
            elif name == 'Holiday Bundle Promotion':
                start = datetime.date(year + 1, 11, 24)
                end = datetime.date(year + 1, 12, 17)
                budg = 49000
                created = datetime.date(year + 1, 11, 1)
            elif name == 'New Year Bedroom Refresh':
                start = datetime.date(year + 1, 12, 24)
                end = datetime.date(year + 2, 1, 17)
                budg = 49000
                created = datetime.date(year + 1, 12, 1)

            # Stop generating after May 2026
            if start > datetime.date(2026, 5, 31):
                continue

            Start_Date.append(start)
            End_Date.append(end)
            Budget.append(budg)
            Created_At.append(created)
            Campaign_Names.append(name)

            prefix = "CMP_"
            Campaign_ID.append(prefix + fake.unique.uuid4())

            # Assign Campaign Types
            if name in ['New Year Bedroom Refresh', 'Summer Mattress Sale', '11.11 Mega Sale']:
                Campaign_Type.append('Percentage Discount')
            elif name in ['Back to School Home Essentials']:
                Campaign_Type.append('Fixed Discount')
            elif name in ['Valentine Bedding Bundle', 'Holiday Bundle Promotion']:
                Campaign_Type.append('Buy One Get One')
            elif name in ['Happy Songkran', 'Free Shipping Month']:
                Campaign_Type.append('Free Shipping')
            elif name == '10.10 Flash Sale':
                Campaign_Type.append('Limited Time Offer')
            else:
                Campaign_Type.append('Voucher Code')

            # Assign Target Audiences
            if name in ['New Year Bedroom Refresh', 'Happy Songkran', '11.11 Mega Sale', 'Sleep Better Campaign']:
                Target_Audience.append('All Customers')
            elif name == 'Valentine Bedding Bundle':
                Target_Audience.append('Couples')
            elif name == 'Summer Mattress Sale':
                Target_Audience.append('Families')
            elif name in ['Mid-Year Mega Discount', '10.10 Flash Sale']:
                Target_Audience.append('Budget Shoppers')
            elif name in ['Free Shipping Month', 'Rainy Season Bedding Deals']:
                Target_Audience.append('Existing Customers')
            elif name in ['Back to School Home Essentials']:
                Target_Audience.append('Students')
            else:
                Target_Audience.append('New Homeowners')

            # Assign Region
            Region.append(random.choices([
                'Nation Wide', 'Northern', 'Northeast', 'Southern', 'Eastern', 'Western', 'Central'
            ], weights=[1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])[0])
            
            # Assign Status based timeline 
            if end < datetime.date.today():
                Status.append('Completed')
            elif start > datetime.date.today():
                Status.append('Upcoming')
            else: 
                Status.append('Active')  
        
    data = pd.DataFrame({
        'Campaign_ID': Campaign_ID,
        'Campaign_Name': Campaign_Names,
        'Campaign_Type': Campaign_Type,
        'Start_Date': Start_Date,
        'End_Date': End_Date,
        'Budget': Budget,
        'Target_Audience': Target_Audience,
        'Region': Region,
        'Status': Status,
        'Created_At': Created_At
    })
    return data

Campaign_Data_Population = create_campaign_data()
Campaign_Data_Population.to_csv('Dataset/Campaign/Campaign_Data.csv', index=False)