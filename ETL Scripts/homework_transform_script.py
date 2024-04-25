import pandas as pd
import json
from gcp_functions import read_csv_from_gcs, insert_dataframe_to_bigquery, create_bigquery_schema
from google.oauth2 import service_account
from google.cloud import bigquery

## get GCP configurations
with open('config.json') as config_file:
    config = json.load(config_file)

YOUR_BUCKET_NAME = config["bucket_name"]
PROJECT_ID = config["project_id"]

## begin data cleaning and transformation
crime_df_raw = read_csv_from_gcs(bucket_name=YOUR_BUCKET_NAME, file_name='2024-04-08/crime_data_20240408172539.csv')
crime_df_raw.drop_duplicates(subset=['dr_no'], inplace=True)
crime_df = crime_df_raw.copy()
#formatting time columns
crime_df['time_occ'] = crime_df['time_occ'].astype(str).str.zfill(4)

#formatting date columns
crime_df["date_rptd"] = crime_df.date_rptd.apply(lambda i:str(i).split("T")[0])
crime_df["date_rptd"] = crime_df.date_rptd.apply(lambda i:str(i).replace("-",""))
crime_df["date_rptd"] = crime_df["date_rptd"].astype(int)

crime_df["date_occ"] = crime_df.date_occ.apply(lambda i:str(i).split("T")[0])
crime_df["date_occ"] = crime_df.date_occ.apply(lambda i:str(i).replace("-",""))
crime_df["date_occ"] = crime_df["date_occ"].astype(int)

## reformat race

descent_mapping = {
    'A': 'Other Asian',
    'B': 'Black',
    'C': 'Chinese',
    'D': 'Cambodian',
    'F': 'Filipino',
    'G': 'Guamanian',
    'H': 'Hispanic/Latin/Mexican',
    'I': 'American Indian/Alaskan Native',
    'J': 'Japanese',
    'K': 'Korean',
    'L': 'Laotian',
    'O': 'Other',
    'P': 'Pacific Islander',
    'S': 'Samoan',
    'U': 'Hawaiian',
    'V': 'Vietnamese',
    'W': 'White',
    'X': 'Unknown',
    'Z': 'Asian Indian'
}
crime_df['vict_descent'] = crime_df['vict_descent'].replace(descent_mapping)

## rename columns
crime_df = crime_df.rename(columns = {"area":"area_cd","crm_cd_desc":"crm_desc","weapon_used_cd":"weapon_cd"})

## Dimensional modeling

## area dimension

area_df = crime_df[['area_cd', 'area_name']].drop_duplicates().copy()

## crime type dimension

crime_type_df = crime_df[['crm_cd', 'crm_desc']].drop_duplicates().copy()
crime_type_df = crime_type_df.rename(columns = {"crm_cd":"crime_cd", "crm_desc":"crime_desc"})

## premise dimension

premise_df = crime_df[['premis_cd', 'premis_desc']].drop_duplicates().copy()

## weapon dimension

weapon_df = crime_df[['weapon_cd', 'weapon_desc']].drop_duplicates().copy()

## date time dimension

date_time_df = crime_df[["date_rptd",'date_occ', 'time_occ']].drop_duplicates().copy()
date_time_df["month"] = date_time_df.date_occ.apply(lambda i:int(str(i)[4:6]))
date_time_df["year"] = date_time_df.date_occ.apply(lambda i:int(str(i)[:4]))
date_time_df["day"] = date_time_df.date_occ.apply(lambda i:int(str(i)[6:]))
date_time_df["month_name"] = pd.to_datetime(date_time_df["date_occ"], format='%Y%m%d').dt.month_name()
date_time_df["calendar_year_quarter"] = pd.to_datetime(date_time_df["date_occ"], format='%Y%m%d').dt.quarter
date_time_df["hour"] = date_time_df.time_occ.apply(lambda i:int(str(i)[:2]))
date_time_df["minute"] = date_time_df.time_occ.apply(lambda i:int(str(i)[2:]))
date_time_df["time_occ"] = date_time_df.time_occ.apply(lambda i:str(i).zfill(4))
date_time_df["day_of_week"] = pd.to_datetime(date_time_df["date_occ"], format='%Y%m%d').dt.day_name()

date_time_df = date_time_df[["date_occ", "date_rptd", "year", "month", "month_name","day", "day_of_week",
                             "time_occ" ,"hour","minute","calendar_year_quarter"]]

## fact table

fact_df = crime_df[['dr_no', 'date_occ','area_cd', 'crm_cd', 'premis_cd', 'weapon_cd',
                    "status_desc" ,"vict_age","vict_sex","vict_descent"]].copy()
fact_df = fact_df.rename(columns = {"crm_cd":"crime_cd", "crm_desc":"crime_desc"})



# CREATING SCHEMA FOR DATA WAREHOUSE

key_path = config['key_path']

# Construct a BigQuery client object.
credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Path to your SQL file
sql_file_path = 'schema_creation.sql'

create_bigquery_schema(sql_file_path=sql_file_path)

insert_dataframe_to_bigquery(area_df, 'la_crime.dim_area', credentials.project_id)

print("Finished inserting area dimension")
print()

insert_dataframe_to_bigquery(crime_type_df, 'la_crime.dim_crime', credentials.project_id)

print("Finished inserting crime type dimension")
print()

insert_dataframe_to_bigquery(premise_df, 'la_crime.dim_premise', credentials.project_id)

print("Finished inserting premise dimension")
print()

insert_dataframe_to_bigquery(weapon_df, 'la_crime.dim_weapon', credentials.project_id)

print("Finished inserting weapon dimension")
print()

insert_dataframe_to_bigquery(date_time_df, 'la_crime.dim_date_time', credentials.project_id)

print("Finished inserting date time dimension")
print()

insert_dataframe_to_bigquery(fact_df, 'la_crime.la_crime_facts', credentials.project_id, if_exists='append')

print("Finished inserting fact table")
print()

print("ETL process is complete.")
