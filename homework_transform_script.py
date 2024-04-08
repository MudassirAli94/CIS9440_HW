import pandas as pd
import numpy as np
import json
from gcp_functions import read_csv_from_gcs, upload_table_to_bq

## get GCP configurations
with open('config.json') as config_file:
    config = json.load(config_file)

YOUR_BUCKET_NAME = config["bucket_name"]
PROJECT_ID = config["project_id"]

## begin data cleaning and transformation
crime_df_raw = read_csv_from_gcs(bucket_name=YOUR_BUCKET_NAME, file_name='2024-04-08/crime_data_20240408172539.csv')
crime_df_raw.drop_duplicates(subset=['dr_no'], inplace=True)

## removing columns with more than 25% missing values
missing_percentages = crime_df_raw.isnull().mean() * 100
columns_to_drop = missing_percentages[missing_percentages > 25].index

crime_df = crime_df_raw.drop(columns=columns_to_drop).copy()
#formatting time columns
crime_df["time_occ"] = crime_df.time_occ.apply(lambda i:str(i).split(".")[-1])

#formatting date columns
crime_df["date_rptd"] = crime_df.date_rptd.apply(lambda i:str(i).split("T")[0])
crime_df["date_rptd"] = crime_df.date_rptd.apply(lambda i:str(i).replace("-",""))
crime_df["date_rptd"] = crime_df["date_rptd"].astype(int)

crime_df["date_occ"] = crime_df.date_occ.apply(lambda i:str(i).split("T")[0])
crime_df["date_occ"] = crime_df.date_occ.apply(lambda i:str(i).replace("-",""))
crime_df["date_occ"] = crime_df["date_occ"].astype(int)

print(crime_df.time_occ.value_counts(10))

print(crime_df.tail(30))
