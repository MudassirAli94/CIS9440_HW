import pandas as pd
import numpy as np
from gcp_functions import read_csv_from_gcs, upload_table_to_bq

YOUR_BUCKET_NAME = "mudassir-cis9440-hw"
PROJECT_ID = 'dw-group-project'

crime_df_raw = read_csv_from_gcs(bucket_name=YOUR_BUCKET_NAME, blob_name='2024-04-08/crime_data_20240408163035.csv')
print(crime_df_raw.head())