import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler



def add_scaled_columns(train, validate, test, scaler, columns_to_scale):
    
    # new column names
    new_column_names = [c + '_scaled' for c in columns_to_scale]
    
    # Fit the scaler on the train
    scaler.fit(train[columns_to_scale])
    
    # transform train validate and test
    train = pd.concat([
        train,
        pd.DataFrame(scaler.transform(train[columns_to_scale]), columns=new_column_names, index=train.index),
    ], axis=1)
    
    validate = pd.concat([
        validate,
        pd.DataFrame(scaler.transform(validate[columns_to_scale]), columns=new_column_names, index=validate.index),
    ], axis=1)
    
    
    test = pd.concat([
        test,
        pd.DataFrame(scaler.transform(test[columns_to_scale]), columns=new_column_names, index=test.index),
    ], axis=1)
    
    return train, validate, test

def remove_outliers(df, k, col_list):
    ''' remove outliers from a list of columns in a dataframe 
        and return that dataframe
    '''
    
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df

def prepare_zillow_first_exploration(df):
    ''' Prepare zillow data for exploration'''

    # drop Nulls and Empty spaces
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.dropna() # Decided to remove all nulls instead of imputing because of lack of domain knowledge

    # removing outliers
    df = remove_outliers(df, 1.5, ['bedrooms', 'bathrooms', 'area', 'tax_value'])
    
    # train/validate/test split
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)
    
    return train, validate, test

def prepare_zillow_first_modeling(df):
    ''' Prepare zillow data for modeling'''

    # drop Nulls and Empty spaces
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.dropna() # Decided to remove all nulls instead of imputing because of lack of domain knowledge

    # removing outliers
    df = remove_outliers(df, 1.5, ['bedrooms', 'bathrooms', 'area', 'tax_value'])
    
    # train/validate/test split
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)
    
    columns_to_scale = ['bedrooms', 'bathrooms', 'area',]
    train, validate, test = add_scaled_columns(train, validate, test, MinMaxScaler(), columns_to_scale)
    
    return train, validate, test

def prepare_zillow_second_modeling(df):
    
    df.has_pool = df.has_pool.fillna(0)
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.dropna()

    df = remove_outliers(df, 1.5, ['bedrooms', 'bathrooms', 'area', 'tax_value', 'year'])
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)
    columns_to_scale = ['bedrooms', 'bathrooms', 'area', 'has_pool', 'year']
    train, validate, test = add_scaled_columns(train, validate, test, MinMaxScaler(), columns_to_scale)
    return train, validate, test