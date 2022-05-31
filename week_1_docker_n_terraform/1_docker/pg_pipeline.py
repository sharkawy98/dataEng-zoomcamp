import pandas as pd
from sqlalchemy import create_engine
from time import time

# connect to postgres database attached to docker network
engine = create_engine('postgresql://root:root@pg-database:5432/ny_taxi')

# read data
df = pd.read_parquet('yellow_tripdata.parquet')
ddl = pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine)
print('Generated DDL for the taxi data DataFrame')
print(ddl)

# load data
t1 = time()
df.to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')
t2 = time()

print('Successfuly loaded taxi data to postgres...')
print('Load job time: ', t2 - t1, 'secs')
