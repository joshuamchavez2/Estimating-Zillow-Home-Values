## Predicting-Zillow-Home-Values


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Project Summary
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
> - Create modules (wrangle.py, acquire.py, prepare.py, explore.py, evaluate.py) that make your process repeateable.
> - A report in the form of a presentation, verbal supported by slides. The report/presentation slides should summarize your findings about the drivers of the single unit property values.
> - Deliver a 5 minute [Slide deck](https://www.canva.com/design/DAEqCehG2NM/wyyWkWzU8JlmRbPyFecviw/view?utm_content=DAEqCehG2NM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) with presentation summarizing findings presentation; your presentation should be appropriate for your target audience.
> - Answer panel questions about your code, process, findings and key takeaways, and model.

#### Business Goals
> - The project and goal is to predict the values of single unit properties that the tax district assesses using the property data from those with a transaction during the "hot months" (in terms of real estate demand) of May-August, 2017.
> - Find the distribution of tax rates for each county.
> - Document the process.

#### Audience
> - Zillow Data Science Team

#### Project Deliverables
> - A final report notebook 
> - A 5 min slide deck presentation
> - All necessary modules to make my project reproducible

#### Project Context
> - The Zillow dataset I'm using came from the Codeup database.


#### Data Dictionary
| Column Name                  | Renamed   | Info                                            |
|------------------------------|-----------|-------------------------------------------------|
| bathroomcnt                  | bathrooms | number of bathrooms                             |
| bedroomcnt                   | bedrooms  | number of bedrooms                              |
| calculatedfinishedsquarefeet | area      | number of square feet                           |
| fips                         | N/A       | FIPS code (for county)                          |
| yearbuilt                    | N/A       | The year the property was built                 |
| taxvaluedollarcnt            | tax_value | Property's tax value in dollars                 |
| taxamount                    | tax_amount| amount of tax on property                       |
| tax_rate                     | N/A       | tax_rate on property                            |
| poolsizesum                  | has_pool  | 1 for pool, 0 for no                            |

#### Initial Hypotheses

> - **Hypothesis 1 -**
    > - $H_o$: area and bedrooms are not linearly correlated
    > - $H_a$: area and bedrooms are linearly correlated
    > - Outcome: I rejected the Null Hypothesis; Area and bedrooms are linearly correlated.

> - **Hypothesis 2 -** 
    > - $H_o$: area and restrooms are not linearly correlated
    > - $H_a$: area and restrooms are linearly correlated
    > - Outcome: I rejected the Null Hypothesis; Area and bathrooms are linearly correlated.
    

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - Conclusion, my best model was a Tweedie Regressor beating my baseline RMSE by roughly $30k.  My best features to predict tax value were area, bedrooms, and bathrooms.  LA had the highest tax rate and sold the most houses during hot months.

> - Take Aways, my models residuals implied that there is another driving feature for higher tax value properties.
    

> - I had more time, I would have liked to explore and model the many different features of the Zillow database.  I would have also liked to learn more about the domain knowledge of real estate.


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### Plan
> - Understand the project goals
    - What is my Target?
    - What will I use my target for?
    - What are my deliverables?
    - What platform am I going to use for slide deck?

> - Acquire the data from codeup database
    - Grab first iteration of features
        - use only square feet of the home
        - number of bedrooms
        - number of bathrooms
        - taxvaluedollarcnt
    - Grab second iteration of features
        - select all features

> - Prepare the data
    - Clean
        - Drop or Impute nulls
        - Change datatypes
        - remove duplicate or unuseful features
        - scale
        - split
    - Create functions that can making modeling/exploration easy.  
        - prepare_first_exploration(), 
        - prepare_first_modeling()
        - prepare_second_exploration()
        - prepare_second_modeling()

> - Data Exploration
    - state original hyposesis
    - lay out some questions to answer
    - Feature engineer 
    - univerate, bivariate, multivariate
    - t test / chi2 test
    - heat maps
    
> - Modeling
    - Run one of each regression models
    - change a few hyperparameters
    - Store type of test and hyerparameters used in a DB
    - find best model with lowest RMSE
    - best model on test

> - Conclusion and Recommendations
    - Take aways, recommendation and if I had more time
    - Work on excuetive summary
    - Create slides
___

##### Plan -> Acquire
> - Store functions that are needed to acquire data from the Zillow database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the acquire.py module
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> Prepare
> - Store functions needed to prepare the zillow data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Create any new features, if made for this project.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
___

##### Plan -> Acquire -> Prepare -> Explore
> - Answer key questions, my hypotheses, and figure out the features that can be used in a regression model to best predict the target variable, tax_value. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are correlated to tax_value (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver
> - Introduce myself and my project goals at the very beginning of my slide deck walkthrough.
> - Summarize my findings at the beginning like I would for an Executive Summary.
> - Walk "Zillow Data Science Team" through the analysis I did to answer my questions and that lead to my findings.
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [x] Download the wrangle.py, aquire.py, prepare.py, explore.py, evaluate.py, and final.ipynb files into your working directory
- [x] Add your own env file to your directory. (user, password, host)
- [x] Run the final_report.ipynb notebook