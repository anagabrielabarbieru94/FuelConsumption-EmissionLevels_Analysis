import boto3
import pandas as pd
import numpy as np

columns_list = ['Row Number', 'Manufacturer', 'Model', 'Description', 'AorM', 'Transmission', 'Engine Capacity',
                   'Fuel Type', 'Metric Urban (Cold)', 'Metric Extra-Urban', 'Metric Combined', 'Imperial Urban (Cold)',
                   'Imperial Extra-Urban', 'Imperial Combined', 'CO2', 'Euro standard', 'Noise Level dB(A)',
                   'Emissions CO', 'THC Emissions', 'Emissions NOx', 'THC + NOx Emissions',
                   'Particulates', 'Date of change', 'Fuel Cost 12000 Miles', 'Tax band', 'Standard 12 months',
                   'Standard 6 Months', '1st year 12 months', '1st year 6 months']

file_name = "../../dissertation_datasets/merged_dataset.csv"

MY_ACCESS_KEY_ID = '*****'
MY_SECRET_ACCESS_KEY = '*******'

df = pd.read_csv(file_name)
df['Row Number'] = df.reset_index().index
print(df)

for i in df.columns:
    df[i] = df[i].astype(str)

myl=df.T.to_dict().values()

# Connect to DynamoDB using boto
resource = boto3.resource('dynamodb', aws_access_key_id=MY_ACCESS_KEY_ID, aws_secret_access_key=MY_SECRET_ACCESS_KEY,
                          region_name='*****')

# Connect to the DynamoDB table
table = resource.Table('fuel_dataset')

# Load the JSON object created in the step 3 using put_item method
for data in myl:
    table.put_item(Item=data)
