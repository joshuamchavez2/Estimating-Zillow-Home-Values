import pandas as pd
import numpy as np
import os

from env import host, user, password

###################### Acquire Zillow Data ######################

def get_db_url(url):
    url = f'mysql+pymysql://{user}:{password}@{host}/{url}'
    return url


# First zillow data will only have these 4 features
def first_zillow_data():
    '''
    This function reads the titanic data from the Codeup db into a df,
    write it to a csv file, and returns the df.
    '''
    # Create SQL query.
    sql_query = """
            
    SELECT calculatedfinishedsquarefeet, bedroomcnt, bathroomcnt, taxvaluedollarcnt
    FROM properties_2017
    LEFT JOIN predictions_2017
	    on properties_2017.parcelid = predictions_2017.parcelid
    WHERE (properties_2017.propertylandusetypeid = 261) and (transactiondate between "2017-05-01" and "2017-08-31");"""

    
    df = pd.read_sql(sql_query, get_db_url('zillow'))


    # renaming column names to one's I like better
    df = df.rename(columns = {'bedroomcnt':'bedrooms', 
                              'bathroomcnt':'bathrooms', 
                              'calculatedfinishedsquarefeet':'area',
                              'taxvaluedollarcnt':'tax_value',})
    return df

# If I have time I would like to grab all the features
def second_zillow_data():
    '''
    This function reads the titanic data from the Codeup db into a df,
    write it to a csv file, and returns the df.
    '''
    # Create SQL query.
    sql_query = """
            
    SELECT calculatedfinishedsquarefeet, bedroomcnt, bathroomcnt, taxvaluedollarcnt, poolcnt, yearbuilt
    FROM properties_2017
    LEFT JOIN predictions_2017
	    on properties_2017.parcelid = predictions_2017.parcelid
    WHERE (properties_2017.propertylandusetypeid = 261) and (transactiondate between "2017-05-01" and "2017-08-31");"""

    
    df = pd.read_sql(sql_query, get_db_url('zillow'))


    # renaming column names to one's I like better
    df = df.rename(columns = {'bedroomcnt':'bedrooms', 
                              'bathroomcnt':'bathrooms', 
                              'calculatedfinishedsquarefeet':'area',
                              'taxvaluedollarcnt':'tax_value',
                              'poolcnt': 'has_pool',
                              'yearbuilt': 'year'})
    return df

def acquire_zillow_first():
    '''
    This function reads in titanic data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('zillow_df_first.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('zillow_df_first.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = first_zillow_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('zillow_df_first.csv')
        
    return df


# this will have all the features, I will do this if I have time.  
def acquire_zillow_second():
    '''
    This function reads in titanic data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('zillow_df_second.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('zillow_df_second.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = second_zillow_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('zillow_df_second.csv')
        
    return df