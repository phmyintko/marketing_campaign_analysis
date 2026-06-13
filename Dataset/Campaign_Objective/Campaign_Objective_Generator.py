import pandas as pd

#column oriented
def create_campaign_objective_bridge():

    # Load datasets
    campaign_df = pd.read_csv('Dataset/Campaign/Campaign_Data.csv')
    objective_df = pd.read_csv('Dataset/Objective/Objective_Data.csv')

    # Convert dates bec python see them as string
    campaign_df['Created_At'] = pd.to_datetime(campaign_df['Created_At']).dt.date

    objective_df['Created_At'] = pd.to_datetime(objective_df['Created_At']).dt.date

    # Create dictionaries for quick lookups
    obj_id_map = dict(
        zip(
            objective_df['Objective_Name'],
            objective_df['Objective_ID'],
        )
    )
    obj_date_map = dict(
        zip(
            objective_df['Objective_Name'],
            objective_df['Created_At']
        )
    )

    # Bridge lists
    campaign_ids = []
    objective_ids = []

    # create temp table
    def add_link(campaign_id, campaign_created_at, objective_name):

        obj_id = obj_id_map.get(objective_name)
        obj_date = obj_date_map.get(objective_name)

        if (
            obj_id is not None
            and obj_date is not None
            and obj_date <= campaign_created_at
        ):
            campaign_ids.append(campaign_id)
            objective_ids.append(obj_id)

    # Campaign → Objective Mapping
    for row in campaign_df.itertuples(index=False):

        campaign_id = row.Campaign_ID
        campaign_name = row.Campaign_Name
        campaign_created_at = row.Created_At

        # Every campaign seeks revenue growth
        add_link(
            campaign_id,
            campaign_created_at,
            'Increase Revenue'
        )

        # Customer acquisition campaigns
        if campaign_name in [
            'Summer Mattress Upgrade',
            'Mid-Year Home Refresh',
            '11.11',
            'New Year Bedroom Refresh'
        ]:

            add_link(
                campaign_id,
                campaign_created_at,
                'Grow Customer Base'
            )

        # Bundle / cross-sell campaigns
        elif campaign_name in [
            'Valentine Sleep & Comfort',
            'Holiday Home Comfort',
            'Back to School Home Essentials'
        ]:

            add_link(
                campaign_id,
                campaign_created_at,
                'Improve Cross-Category Adoption'
            )

        # Retention-focused campaigns
        elif campaign_name in [
            'Free Shipping Festival',
            'Rainy Season Comfort'
        ]:

            add_link(
                campaign_id,
                campaign_created_at,
                'Improve Customer Retention'
            )

        # Awareness / category expansion campaigns
        elif campaign_name in [
            'Happy Songkran',
            'Sleep Better'
        ]:

            add_link(
                campaign_id,
                campaign_created_at,
                'Expand Product Category Penetration'
            )

        # Flash sale campaigns
        elif campaign_name == '10.10':

            add_link(
                campaign_id,
                campaign_created_at,
                'Grow Customer Base'
            )

            add_link(
                campaign_id,
                campaign_created_at,
                'Increase Repeat Purchases'
            )

    # Create bridge table
    bridge_df = pd.DataFrame({
        'Campaign_ID': campaign_ids,
        'Objective_ID': objective_ids
    })

    bridge_df = bridge_df.drop_duplicates()

    return bridge_df

campaign_objective_bridge_df = create_campaign_objective_bridge()
campaign_objective_bridge_df.to_csv('Dataset/Campaign_Objective/Campaign_Objective_Data.csv', index=False)