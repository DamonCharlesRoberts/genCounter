"""
    Title: purge dictionary table
    Notes:
        - Description: Scheduled script to daily purge contents of core_documents table
        - Updated: 2022-12-23
        - Updated by: dcr
"""

from sqlalchemy import create_engine # to connect to database
import os # for path management
from dotenv import load_dotenv # for env file for secretkeys

# Load secret keys
load_dotenv("/home/damoncroberts/gencounter/.env")

# Load
USER = os.getenv("USER") # define USER var
PASSWORD = os.getenv("PASS") # define PASSWORD var
engine = create_engine( # create the engine to connect to the database
        f'mysql+mysqlconnector://{USER}:{PASSWORD}@{USER}.mysql.pythonanywhere-services.com/{USER}$genCounter'
        ) # access the mysql database for this webapp
engine.connect() # connect to the database with the engine
engine.execute("TRUNCATE TABLE core_document;", con = engine) # delete the contents of the table but but recreate the columns.