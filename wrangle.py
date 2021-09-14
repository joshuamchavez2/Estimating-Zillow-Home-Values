from acquire import acquire_zillow_first
from prepare import prepare_zillow_first_modeling, prepare_zillow_first_exploration

def wrangle_zillow_modeling():
    # For modeling
    train, validate, test = prepare_zillow_first_modeling(acquire_zillow_first())
    
    return train, validate, test

def wrangle_zillow_exploration():
    # For modeling
    train, validate, test = prepare_zillow_first_exploration(acquire_zillow_first())
    
    return train, validate, test