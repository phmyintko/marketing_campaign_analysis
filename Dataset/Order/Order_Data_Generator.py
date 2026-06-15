from faker import Faker
import pandas as pd
import random
import datetime

def order_data_generator():
    
    fake = Faker('en_TH')
    SEED = 92
    random.seed(SEED)
    fake.seed_instance(SEED)

    ### import related entities to get fk
    customer_df = pd.read_csv('Dataset/Customer/Customer_Data.csv', 
    parse_dates=['Created_At']
    ).rename(columns={'Created_At': 'Cust_Created_At'})
    payment_df = pd.read_csv('Dataset/Payment/Payment_Data.csv',
    parse_dates=['Created_At']
    ).rename(columns={'Created_At': 'Pay_Created_At'})
    status_df = pd.read_csv('Dataset/Order_Status/Order_Status_Data.csv')

    ### create order records
    order_records = []
    # set order distribution rule: calculated by Thailand's Consumer Spending Data; source: tradingeconomics.com
    order_years = [
        2021,
        2022,
        2023,
        2024,
        2025,
        2026
    ]
    order_weights = [
        0.161,
        0.170,
        0.182,
        0.191,
        0.196,
        0.098
    ]

    ### loop each customer for their customer type and how many orders they should have.
    for customers in customer_df.itertuples(index=False):
        customer_id = customers.Customer_ID

        customer_created_at = customers.Cust_Created_At.date()

        # rule: customer type 
        customer_type = random.choices(
            ['One_Time', 'Repeat', 'Commercial'],
            weights=[0.75, 0.20, 0.05]
        )[0]

        # rule: number of orders per customer
        if customer_type == 'One_Time':
            order_count = 1
        elif customer_type == 'Repeat':
            order_count = random.randint(2, 6)
        else:
            order_count = random.randint(8, 20)

        ## loop to create each order for the customer
        for _ in range(order_count):

            # generate order year based on consumer spending
            order_year = random.choices(
                order_years,
                weights=order_weights
            )[0]

            # generate order date
            if order_year == 2026:
                order_date = datetime.date(
                    2026,
                    random.randint(1, 5),
                    random.randint(1, 28)
                )
            else:
                order_date = datetime.date(
                    order_year,
                    random.randint(1, 12),
                    random.randint(1, 28)
                )
            # if the generated date is before customer's signup date, use the signup date
            if order_date < customer_created_at:
                order_date = customer_created_at

            # extract eligible list first in order to prevent generate payment before created
            eligible_payments = payment_df[
                payment_df['Pay_Created_At'].dt.date <= order_date
            ]
            payment_id = random.choice(
                eligible_payments['Payment_ID'].tolist()
            )

            # generate status
            status_id = random.choice(
                status_df['Status_ID'].tolist()
            )

            ### append results
            order_records.append({
                'Order_ID': 'ORD_' + fake.unique.uuid4()[:6],
                'Customer_ID': customer_id,
                'Order_Date': order_date,
                'Payment_ID': payment_id,
                'Status_ID': status_id,
                'Created_At': order_date
            })

    order_df = pd.DataFrame(order_records)
    return order_df
    
order_df = order_data_generator()
order_df.to_csv('Dataset/Order/Order_Data.csv')