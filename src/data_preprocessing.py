
import pandas as pd
import numpy as np

def preprocess_offer_data(transcript_df, portfolio_df):

    offers_delivered_df = transcript_df[
        transcript_df.event != 'transaction'
    ].copy()

    offers_delivered_df['offer_id'] = offers_delivered_df['value'].apply(
        lambda x: x.get('offer id') if x.get('offer id') is not None \
            else x.get('offer_id')
    )

    offers_delivered_df['event'] = offers_delivered_df['event']\
        .replace(' ', '_', regex=True)

    offers_delivered_df = offers_delivered_df.merge(
        portfolio_df, 
        left_on='offer_id', 
        right_on='id', 
        how='left'
    )

    offers_delivered_df['offer_type_event'] = \
        offers_delivered_df['offer_type'] + '_' + offers_delivered_df['event']

    offers_delivered_df['expiration_time'] = \
        offers_delivered_df['time'] + offers_delivered_df['duration']

    return offers_delivered_df

def get_customer_transactions_per_offer_type(transcript_df, offers_delivered_df):

    transactions_df = transcript_df[
        transcript_df.event == 'transaction'
    ].copy()
    
    transactions_df['amount'] = transactions_df['value'].apply(
        lambda x: x.get('amount')
    )

    transactions_df = transactions_df.rename(columns={'time':'transaction_time'})

    transactions_df = transactions_df.groupby(['person', 'transaction_time'])\
        .amount.sum().reset_index()

    offer_viewed_df = offers_delivered_df[
        offers_delivered_df.event == 'offer_viewed'
    ]
    
    amount_per_offer_df = offer_viewed_df.merge(transactions_df, on='person')

    amount_per_offer_df = amount_per_offer_df[
        (amount_per_offer_df.transaction_time >= amount_per_offer_df.time) &
        (amount_per_offer_df.transaction_time <= amount_per_offer_df.expiration_time)
    ]

    amount_per_offer_df = amount_per_offer_df\
        .groupby(['person', 'offer_type', 'transaction_time']).amount.sum()\
            .reset_index()

    transactions_df['offer_type'] = 'no_offer'
    all_transactions_df = pd.concat([amount_per_offer_df, transactions_df])
    all_transactions_df = all_transactions_df.drop_duplicates(
        subset = ['person', 'transaction_time', 'amount'],
        keep = 'first'
    ).reset_index(drop = True)
    
    all_transactions_df['is_offer'] = (all_transactions_df.offer_type != 'no_offer')*1

    return all_transactions_df