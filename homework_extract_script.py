import pandas as pd
import requests
from gcp_functions import upload_dataframe_to_gcs

YOUR_BUCKET_NAME =  "mudassir-cis9440-hw"
PROJECT_ID = 'dw-group-project'

url = "https://data.lacity.org/resource/2nrs-mtv8.csv"

response = requests.get(url)

if response.status_code == 200:
    df = pd.read_csv(url)
    print(df.head())
else:
    print("Failed to fetch data. Status code:", response.status_code)


for n in df.columns:
    print(df[n].head())
    print()

upload_dataframe_to_gcs(bucket_name=YOUR_BUCKET_NAME,
                        df=df, file_name='crime_data_raw',
                        project_id=PROJECT_ID)


