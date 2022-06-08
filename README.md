# Starbucks Customer Offer Targeting

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Methodology](#methodology)
5. [Main results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

Most of the libraries used on the project, such as pandas, numpy, matplotlib and scikit-learn can be installed using the Anaconda distribution of Python.

The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

The goal is to analyze a dataset with simulated data that mimics customer behavior on the Starbucks rewards mobile app and give a proposal based on the findings and insights while exploring the data.

After doing the analysis that can be seen at the *starbucks_offers_eda.ipynb* Jupyter Notebook in the *src* directory, I decided to develop Machine Learning models that predict customers who will complete an offer if the person is target by it.

Understanding how your customers will interact with your offers is relevant because:

1. Helps to estimate how much in discounts you will offer to your customers in a new offer campaign.
2. Avoid losing revenue from customers that are already willing to pay full price, but they received an offer.

## File Descriptions <a name="files"></a>

This project has 3 main directories: *data*, *images*, and *src*.

* *data*: contains 3 JSON files with the data of customer demographic information, offer information (duration, type, reward, etc), and records of transactions and offers interactions by the customers.
* *images*: contains the main visualizations of the exploratory data analysis and the model evaluation metrics.
* *src*: contains the Jupyter Notebooks and Python script used to do the analysis and develop the Machine Learning models.

## CRISP-DM Methodology <a name="methodology"></a>

### Business Understanding

Customers have different behaviors regarding how they interact with offers campaigns. For example, there may be customers who only make purchases when they are incentivized by offers. But, on the opposite side, there may be customers who make purchases regardless of receiving nothing at all.

Understanding how customers interact with these offers is key to keeping customers engaged with offers but also not losing revenue opportunities by targeting the wrong customers.

### Data Understanding

The data used is a dataset with simulated data that mimics customer behavior on the Starbucks rewards mobile app. There are 3 JSON files with different pieces of information that can be used for analyzing the data.

Below is a brief explanation of the JSON files and the main columns for each file:
* *potfolio.json*: contains information about the offers.
    * offer_type: type of the offer, i.e. BOGO (buy one get one free), discount of informational.
    * duration: time for the offer to be open, in days.
* *profile.json*: contains demographic data for each customer.
    * age: age of the customer.
    * gender: gender of the customer.
    * income: customer's income.
* *transcript.json*: contains records of transactions and offers interactions by the customers.
    * event:  record description (ie transaction, offer received, offer viewed, etc.)
    * value: either an offer id or transaction amount depending on the record.

Also, by doing some exploratory analysis, it was possible to answer the following questions:

1. How do the customers interact with each type of offer?
2. What type of offer has the higher average ticket value? Is it higher than the purchases without offering discounts?
3. How many customers have an average purchase without offers higher than their purchases with offers? 
4. Which age group interacts best with each type of offer?

### Data Preparation

Since the project have three main datasets, one of the steps necessary to me made is to combine information between datasets. The *transcript.json* file is the most important because combines information about the customers, which offers each customers interacted with and information about customer's purchases. In order to use this dataset properly, it was split in two datasets: the first containing only purchase details and the second containing only offer interactions. This preprocessing helps to determine if a customer made purchases during the offer period or not.

Also, it was required to make feature engineering, creating features with information of the offers that each customer interacted with, fill missing data and handle categorical data before train the models. 

### Modelling

The Machine Learning models used on the project were:
* Decision Tree;
* Random Forest;
* Support Vector Machine for Classification.

### Evaluation

The data was split into training, validation, and test sets. The precision and balanced accuracy for each model on validation set were:

Model  | Precison | Balanced Accuracy
------------- | ------------- | -------------
Decision Tree  | 83.8% | 66.3%
Random Forest  | 84.6% | 70.3%
SVC            | 84.5% | 69.8%

Since the Random Forest model got the best precison on the validation set, I used this model to predict the results on the test set and it got the same 84.2% of precision and 69.3% of balanced accuracy scores.

### Deployment

The model was not deployed in any application but the code is available on the *starbucks_offer_prediction.ipynb* file in the *src* directory.

Also, the main insights of the project can be found in the blog post at the [Main results](#results) section.


## Main Results<a name="results"></a>

The main insights found in the exploratory analysis and the discussion comparing Machine Learning models used in this project are available this [blog post](https://medium.com/@andredesouzag/which-customers-should-starbucks-offer-discounts-to-797015b6d2aa).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

All the credits and acknowledgements are for Udacity and Starbucks, the dataset owners. 

