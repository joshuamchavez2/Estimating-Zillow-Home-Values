- # Project Planning

    - Understand the project goals
        - What is my Target?
        - What will I use my target for?
        - What are my deliverables?
        - What platform am I going to use for slide deck?


- # Acquire

    - Acquire the data from codeup database
        - Grab first iteration of features
            - use only square feet of the home
            - number of bedrooms
            - number of bathrooms
            - taxvaluedollarcnt
        - Grab second iteration of features
            - all of them

- # Preperation

    - Clean 
        - Drop or Impute nulls
        - Change datatypes
        - remove duplicate or unuseful features
        - scale
        - split

    - First iteration for exploration
        - Clean() WITH OUT scaling

    - First iteration for modeling
        - Clean() WITH scaling

    - Second iteration for exploration
        - Clean() WITH OUT scaling

    - Second iteration for modeling
        - Clean() with scaling


    - prep functions # By having different prep functions I can easily have different data to work with.
        - prepare_first_exploration()
        - prepare_first_modeling()
        - prepare_second_exploration()
        - prepare_second_modeling()

# Data Exploration
- # Find good graphs to keep for slide deck
    - orginal hyposesis
    - lay out some questions to answer
    - Feature engineer 
    - univerate, bivariate, multivariate
    - t test / chi2 test
    - heat maps
    
# Modeling
- # document well for slide deck
    - Run one of each regression models 
    - change a few hyperparameters
    - find best model with lowest RMSE
    - best model on test

# Conclusion and Pre
    - Take aways, recommendation and if I had more time
    - Work on excuetive summary
    - Create slides
        - 