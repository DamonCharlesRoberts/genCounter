"""
Title: Dictionary to MySQL database

Notes:
    - Description: Add gendered language dictionary file to MySQL database for genCounter project.
    - Updated: 2022-12-21
    - Updated by: dcr
"""

import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv("/home/damoncroberts/gencounter/.env")
df = pd.read_csv("/home/damoncroberts/dict.csv")
dfClean=df[["Word", "mean-a"]].rename(columns={"mean-a":"Score"})
dfClean["Word"] = dfClean["Word"].astype('string')
dfClean["id"] = range(1, len(dfClean) + 1)

USER = os.getenv("USER")
PASSWORD = os.getenv("PASS")
engine = create_engine(
        f'mysql+mysqlconnector://{USER}:{PASSWORD}@{USER}.mysql.pythonanywhere-services.com/{USER}$genCounter'
        )
engine.connect()
dfClean.to_sql(con=engine, name="dictionary", if_exists="replace")