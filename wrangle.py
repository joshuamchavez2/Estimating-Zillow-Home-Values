from acquire import acquire_zillow_first, acquire_zillow_second
from prepare import prepare_zillow_first_modeling, prepare_zillow_first_exploration, prepare_zillow_second_modeling

def wrangle_zillow_modeling():
    # For modeling
    train, validate, test = prepare_zillow_first_modeling(acquire_zillow_first())
    
    return train, validate, test

def wrangle_zillow_exploration():
    # For modeling
    train, validate, test = prepare_zillow_first_exploration(acquire_zillow_first())
    
    return train, validate, test

def wrangle_zillow_second_modeling():
    # For modeling
    train, validate, test = prepare_zillow_second_modeling(acquire_zillow_second())
    
    return train, validate, test