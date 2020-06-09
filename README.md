# Deploying Machine Learning Models : Lead Conversion


## What is ML Ops ? 

Machine Learning has the potential to help solve business problems and deliver real business value. However, implementing ML at scale can be challenging in enterpise environments. Just like how software developers have DevOps to bring together Software Engineers and Operations, Data Scientists can leverage ML Ops the same way.

Many companies still have Machine Learning Engineers and Data Scientists develop models in silos. The complexity of the devlopment environment makes it hard to collaborate. This leads to loss of productivity and delay in adding value to the business. 

MLOps is about creating an end to end solution from research to deployment of the ML model into production. This brings in the agility that DevOps brings ro software development. Data Scientists can operate in a shared and collaborative work space and initiate development,training and prediction using standardised procedures. This accelerates time to value. 

## Data Set Used 

The dataset used is from Kaggle's Marketing Funnel by Olist. This is a marketing funnel dataset from sellers that filled-in requests of contact to sell their products on Olist Store. The dataset has information of 8k Marketing Qualified Leads (MQLs) that requested contact between Jun. 1st 2017 and Jun 1st 2018.

The data set can be found here : https://www.kaggle.com/olistbr/marketing-funnel-olist

This repo builds a model to predict the conversion of a lead. 

## Workflow Implemented 

The following workflow has been implemeted in this repository : 

![Alt text](https://github.com/supriyaarun27/lead_prediction/blob/master/Screenshot%202020-06-08%20at%203.50.52%20PM.png "WorkFlow")

## Research Environment

### Data Analytics 
This step of the process is to get insight into the data we are using. This helps in understanding the data and it's characteristics. In this project I have analysed the following in this step : 
1. Loading the Dataset 
2. Understanding the Shape of the data
3. Visualising the characteristics of the different variables 

### Data Preparation 
This step I have drilled down into the variables to make undestand and prepare the data for training and testing. 
This step includes analysing and identifying the following : 
1. Missing Values 
2. Numerical Variables 
3. Temporial Variables 
4. Categorical Variables 
5. Cardinality of Variables 

### Feature Engineering
This step is where the following have been delt with : 
1. Splitting the data for training and testing 
2. HHandling Missing values in Categorical Variables 
3. Encoding Categorical Variables 

### Model Building 
This step is where I have implemeted a logistic regression model to predict lead conversion. 

## ML Pipeline 

### Procedural Programming 

Writing the steps of data preparation, feature engineering and ModelBuilding steps as functions so they can be called one after the other to build a pipeline. 

### Virtual Environments 

We can maintain the compatability and dependency requirements of the project by using virtual environments. I have used the VENV module from Python. 

I have also used [TOX](https://pypi.org/project/tox/) as a task automation tool.

### Testing Frameworks 

I have used the Pytest framework to write tests for this model

## Collaboration and Version Control

I have used Github (a distributed version control system) for hosting and collaborating this project.

## CI / CD Pipeline 

I have used [CircleCi](https://circleci.com/) for automating the development process. 

