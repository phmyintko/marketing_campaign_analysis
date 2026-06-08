from faker import Faker
import pandas as pd

#pandas build
def promotion_data_generator():
    fake = Faker('en_TH')
    SEED = 92
    fake.seed_instance(SEED)

    #load Campaign Data
    campaign_data_df = pd.read_csv('Dataset/Campaign/Campaign_Data.csv')
    #convert string to datetime
    campaign_data_df['Created_At'] = pd.to_datetime(campaign_data_df['Created_At'])
    campaign_data_df['Start_Date'] = pd.to_datetime(campaign_data_df['Start_Date'])
    campaign_data_df['End_Date'] = pd.to_datetime(campaign_data_df['End_Date'])

    promotion_name_map = {
        'New Year Bedroom Refresh': 'New Year Mattress Discount',
        'Valentine Sleep & Comfort': 'Couple Bedding Bundle',
        'Summer Mattress Upgrade': 'Summer Mattress Savings',
        'Happy Songkran': 'Songkran Free Shipping',
        'Mid-Year Home Refresh': 'Mid-Year Mega Discount',
        'Free Shipping Festival': 'Nationwide Free Shipping',
        'Rainy Season Comfort': 'Rainy Season Voucher',
        'Sleep Better': 'Sleep Better Bundle',
        'Back to School Home Essentials': 'Student Savings Offer',
        '10.10': '10.10 Flash Sale',
        '11.11': '11.11 Mega Discount',
        'Holiday Home Comfort': 'Holiday Bundle Offer'
    }

    promotion_type_map = {
        'New Year Bedroom Refresh': 'Percentage Discount',
        'Valentine Sleep & Comfort': 'Bundle Offer',
        'Summer Mattress Upgrade': 'Percentage Discount',
        'Happy Songkran': 'Free Shipping',
        'Mid-Year Home Refresh': 'Percentage Discount',
        'Free Shipping Festival': 'Free Shipping',
        'Rainy Season Comfort': 'Voucher Code',
        'Sleep Better': 'Bundle Offer',
        'Back to School Home Essentials': 'Fixed Discount',
        '10.10': 'Flash Sale',
        '11.11': 'Percentage Discount',
        'Holiday Home Comfort': 'Bundle Offer'
    }

    promo_code_map = {
        'New Year Bedroom Refresh': 'NEWYEAR',
        'Valentine Sleep & Comfort': 'LOVE',
        'Summer Mattress Upgrade': 'SUMMER',
        'Happy Songkran': 'SONGKRAN',
        'Mid-Year Home Refresh': 'MIDYEAR',
        'Free Shipping Festival': 'FREESHIP',
        'Rainy Season Comfort': 'RAINY',
        'Sleep Better': 'SLEEP',
        'Back to School Home Essentials': 'SCHOOL',
        '10.10': '1010',
        '11.11': '1111',
        'Holiday Home Comfort': 'HOLIDAY'
    }

    campaign_data_df['Promotion_ID'] = [
        'PROMO_' + fake.unique.uuid4()[:4]
        for _ in range(len(campaign_data_df))
    ]
    #campaign name -> promotion name, campaign type, promo code
    campaign_data_df['Promotion_Name'] = (
        campaign_data_df['Campaign_Name'].map(promotion_name_map)
    )

    campaign_data_df['Promotion_Type'] = (
        campaign_data_df['Campaign_Name'].map(promotion_type_map)
    )
    campaign_data_df['Promo_Code'] = (
        campaign_data_df['Campaign_Name'].map(promo_code_map)
        + campaign_data_df['Start_Date'].dt.year.astype(str)
    )
    #campaign date -> promotion date
    campaign_data_df['Start_Date'] = (
        campaign_data_df['Start_Date'] + pd.Timedelta(days=3)
    )
    campaign_data_df['End_Date'] = (
        campaign_data_df['End_Date'] - pd.Timedelta(days=2)
    )

    #create dataframe
    promotion = campaign_data_df[
        [
            'Promotion_ID',
            'Campaign_ID',
            'Promotion_Name',
            'Promotion_Type',
            'Promo_Code',
            'Start_Date',
            'End_Date',
            'Created_At'
        ]
    ]

    return promotion

promotion = promotion_data_generator()
promotion.to_csv('Dataset/Promotion/Promotion_Data.csv', index=False)