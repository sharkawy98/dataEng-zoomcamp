# base image
FROM python:3.9

# download and install dependencies
RUN pip install pandas pyarrow sqlalchemy psycopg2

# tell the image what to do when it starts as a container
WORKDIR /app
COPY pg_pipeline.py .
COPY yellow_tripdata.parquet .

# cmd
ENTRYPOINT [ "python", "pg_pipeline.py" ] 
