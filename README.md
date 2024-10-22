# CIS9440_HW

# Data and Scope Description:

This data comes from https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/data_preview , in my ETL script where can be found here: https://github.com/MudassirAli94/CIS9440_HW/blob/main/ETL%20Scripts/homework_extract_script.py , I run an api to extract the data. The data consists of the crimes that has happened from 2020 to 2023 in LA, California. The goal is to create a data warehouse based on this data source and run basic analysis via power BI. Below this description you can find the raw data dictionary, the information architecutre and the dimensional modeling done. The clean data dictionary where it is related to my data warehouse can be found in the files section. The cloud platform that I chose is google cloud platform using google cloud storage as my staging area and BigQuery as my data warehouse. I have created separate functions to store my data in GCS and create my data warehouse here: https://github.com/MudassirAli94/CIS9440_HW/blob/main/ETL%20Scripts/gcp_functions.py , I call these functions in my extract and transform scripts.

## Data Dictionary

This is the raw data dictionary from the source website. In the files section above is the relevant data dictionary for the table columns I used for the data warehousing.

Raw Data dictionary: https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/about_data

## Information Archeticture:

![image](https://github.com/MudassirAli94/CIS9440_HW/assets/38592433/d8de3f0a-0c83-44b8-8ecd-ec611f18c419)


## Dimensional modeling:


![image](https://github.com/MudassirAli94/CIS9440_HW/assets/38592433/1dca0e7b-26c9-4a0e-8aba-c2a1238d01c4)

## Analysis:

![image](https://github.com/MudassirAli94/CIS9440_HW/assets/38592433/f4675d07-157a-410a-a1ef-9b70da14c004)

A screenshot of the powerBI one page dashboard (also availble above): on a first glance we can see the crime rate spiked from 2021 to 2022 and Hispanic race were the victim of most of the crimes. Additionally the Male and Female victim ratio is just about split at 50-50 with Men having a slight edge. Please see the full pbix file in the files section for a deeper drilldown.

