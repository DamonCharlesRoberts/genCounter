"""
Title: Dictionary to MySQL database

Notes:
    - Description: Add gendered language dictionary file to MySQL database for genCounter project.
    - Updated: 2022-12-23
    - Updated by: dcr
"""

import pandas as pd # for dataframe management
from sqlalchemy import create_engine # to connect to database
import os # for path management
from dotenv import load_dotenv # for env file for secretkeys

# Load secret keys
load_dotenv("/home/damoncroberts/gencounter/.env")

# Extract and transform
df = pd.read_csv("/home/damoncroberts/dict.csv") # extract the dictionary from a csv
dfClean=df[["Word", "mean-a"]].rename(columns={"mean-a":"Score"}) # grab the mean-a and Word columns. Rename the mean-a column to score
dfClean["Word"] = dfClean["Word"].astype('string') # force the Word column to string type
dfClean["id"] = range(1, len(dfClean) + 1) # create an id column
