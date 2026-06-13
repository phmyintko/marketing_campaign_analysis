import random
import pandas as pd

# use row oriented cos of extra field eg. Discount_Value
def product_promotion_generator():
    SEED = 92
    random.seed(SEED)

    product_df = pd.read_csv('Dataset/Product/Product_Data.csv')
    promotion_df = pd.read_csv('Dataset/Promotion/Promotion_Data.csv')

    ### create bridge records
    bridge_records = []

    ### loop every single row in promotion table to make relationship and populate data
    for promo in promotion_df.itertuples(index=False):
        promo_id = promo.Promotion_ID
        promo_name = promo.Promotion_Name
        promo_type = promo.Promotion_Type

        ### Match promotions to relevant products using keywords

        ## set keywords: if related keyword contain in promotion name, set desired keyword aka product category
        # nfr: New Year Mattress Discount, Summer Mattress Savings
        if 'Mattress' in promo_name: 
            keyword = 'Mattress'
        # nfr: Couple Bedding Bundle
        elif 'Bedding' in promo_name or 'Bedsheet' in promo_name:
            keyword = 'Bedsheet'
        #for future proof
        elif 'Pillow' in promo_name:
            keyword = 'Pillow'
        elif 'Bolster' in promo_name:
            keyword = 'Bolster'
        elif 'Blanket' in promo_name:
            keyword = 'Blanket'
        # nfr: Songkran Free Shipping, Mid_Year Mega Discount, Nationwide Free Shipping, Rainy Season Voucher, Sleep Better Bundle, 10.10, 11.11, Holiday Bundle Offer
        else:
            keyword = 'All'
        
        ## set relationship: link the recorded keywords with product names
        # if All -> all products
        if keyword == 'All':
            promo_products = product_df
        #otherwise -> filter by keyword
        else:
            promo_products = product_df[product_df['Product_Name'].str.contains(keyword, case=False)]
        #if found nothing -> all products
        if promo_products.empty:
            promo_products = product_df

        # create discount rules for every single row
        for prod in promo_products.itertuples(index=False):
            prod_id = prod.Product_ID
            prod_price = float(prod.Price) 
            # bool: only mega promotions will get max discount
            promo_campaign = promo_name in ['Mid-Year Mega Discount', '11.11 Mega Sale']
            # percentage discount: min 8%, max 20%
            if promo_type == 'Percentage Discount':
                discount = 20.0 if promo_campaign else 8.0
            # fixed discount: based on product price; min 6%, max 15%
            elif promo_type == 'Fixed Discount':
                discount_rate = 0.15 if promo_campaign else 0.06
                discount = round(prod_price * discount_rate, 0) # set 0 to localize
            # voucher code: 10%
            elif promo_type == 'Voucher Code':
                discount = 10.0
            # flash sale: 15%
            elif promo_type == 'Flash Sale':
                discount = 15.0
            # these promotions have no direct price discount
            elif promo_type in ['Bundle Offer', 'Free Shipping']:
                discount = 0.00
            # employee / emergency discount
            else:
                discount = 5.00

            # append data
            bridge_records.append({
                'Product_ID': prod_id,
                'Promotion_ID': promo_id,
                'Discount_Value': discount
            })
    # build table
    product_promotion_df = pd.DataFrame(bridge_records)
    # drop rows if the pair of product id and promotion id are duplicate
    product_promotion_df = product_promotion_df.drop_duplicates(subset=['Product_ID', 'Promotion_ID'])
    return product_promotion_df

product_promotion = product_promotion_generator()
product_promotion.to_csv('Dataset/Product_Promotion/Product_Promotion_Data.csv', index=False)