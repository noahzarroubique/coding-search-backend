import sqlite3
import pandas as pd

conn = sqlite3.connect('localdata.sqlite')

data = pd.read_sql_query("SELECT * FROM data", conn)