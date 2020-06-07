import pathlib

import regression_model

import pandas as pd


pd.options.display.max_rows = 10
pd.options.display.max_columns = 10


PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
TESTING_DATA_FILE = "test.csv"
TRAINING_DATA_FILE = "train.csv"
TARGET = "convert"


# variables
FEATURES = ["landing_page_id","origin"]

# this variable is to calculate the temporal variable,
# can be dropped afterwards
DROP_FEATURES = []

# numerical variables with NA in train set
NUMERICAL_VARS_WITH_NA = []

# categorical variables with NA in train set
CATEGORICAL_VARS_WITH_NA = ["landing_page_id","origin"]


TEMPORAL_VARS = []

# variables to log transform
NUMERICALS_LOG_VARS = []

# categorical variables to encode
CATEGORICAL_VARS = [ "landing_page_id","origin"]

NUMERICAL_NA_NOT_ALLOWED = [
    feature
    for feature in FEATURES
    if feature not in CATEGORICAL_VARS + NUMERICAL_VARS_WITH_NA
]

CATEGORICAL_NA_NOT_ALLOWED = [
    feature for feature in CATEGORICAL_VARS if feature not in CATEGORICAL_VARS_WITH_NA
]


PIPELINE_NAME = "logistic_regression"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
