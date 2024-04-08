import pandas as pd
import numpy as np
from gcp_functions import read_csv_from_gcs, upload_table_to_bq

YOUR_BUCKET_NAME = "mudassir-cis9440-hw"
PROJECT_ID = 'dw-group-project'

crime_df_raw = read_csv_from_gcs(bucket_name=YOUR_BUCKET_NAME, file_name='2024-04-08/crime_data_20240408172539.csv')
crime_df_raw.drop_duplicates(subset=['dr_no'], inplace=True)

## removing columns with more than 25% missing values
missing_percentages = crime_df_raw.isnull().mean() * 100
columns_to_drop = missing_percentages[missing_percentages > 25].index

crime_df = crime_df_raw.drop(columns=columns_to_drop).copy()
#formatting time columns
crime_df["time_rptd"] = crime_df.date_rptd.apply(lambda i:str(i).split("T")[-1])
crime_df["time_rptd"] = crime_df["time_rptd"].apply(lambda i: str(i).split(".")[0])
crime_df["time_rptd"] = crime_df["time_rptd"].apply(lambda i: str(i).replace(":",""))
crime_df["time_rptd"] = crime_df["time_rptd"].astype(str)

crime_df["time_occ"] = crime_df.time_occ.apply(lambda i:str(i).split(".")[0])


print("Is the time occurred all 000000?", len(crime_df[crime_df["time_occ"] == "000000"]) == len(crime_df))
print()
print("Is the time reported all 000000?", len(crime_df[crime_df["time_rptd"] == "000000"]) == len(crime_df))
print()

#crime_df.drop(columns=["time_occ", "time_rptd"], inplace=True)

#formatting date columns
crime_df["date_rptd"] = crime_df.date_rptd.apply(lambda i:str(i).split("T")[0])
crime_df["date_rptd"] = crime_df.date_rptd.apply(lambda i:str(i).replace("-",""))
crime_df["date_rptd"] = crime_df["date_rptd"].astype(int)

crime_df["date_occ"] = crime_df.date_occ.apply(lambda i:str(i).split("T")[0])
crime_df["date_occ"] = crime_df.date_occ.apply(lambda i:str(i).replace("-",""))
crime_df["date_occ"] = crime_df["date_occ"].astype(int)

print(crime_df.time_occ.value_counts(10))

print(crime_df.tail(30))
