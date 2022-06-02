import sqlite3
import pandas as pd


# Insert data into SQLite database
def load(data):
    con = sqlite3.connect('./DBClick.db')
    data.to_sql(name='Adult', con=con, if_exists='append')

# Read data from SQLite database
def read(sql_query):
    con = sqlite3.connect('./DBClick.db')
    df = pd.read_sql(sql_query,con)
    print(df)
