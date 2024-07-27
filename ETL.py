import pandas as pd

csv_file_path = 'sample_datatest.csv'
data = pd.read_csv(csv_file_path)

data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]

data.fillna(method='ffill', inplace=True)  

if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])

import sqlite3

conn = sqlite3.connect('data_lake.db')
cursor = conn.cursor()

data.to_sql('data_table', conn, if_exists='replace', index=False)

conn.commit()
conn.close()