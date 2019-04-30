import pandas as pd
import numpy as np

columns_list = ['Manufacturer', 'Model', 'Description', 'AorM', 'Transmission', 'Engine Capacity',
                   'Fuel Type', 'Metric Urban (Cold)', 'Metric Extra-Urban', 'Metric Combined', 'Imperial Urban (Cold)',
                   'Imperial Extra-Urban', 'Imperial Combined', 'CO2', 'Euro standard', 'Noise Level dB(A)',
                   'Emissions CO', 'THC Emissions', 'Emissions NOx', 'THC + NOx Emissions',
                   'Particulates', 'Date of change', 'Fuel Cost 12000 Miles', 'Tax band', 'Standard 12 months',
                   'Standard 6 Months', '1st year 12 months', '1st year 6 months']

file_name = "../../dissertation_datasets/merged_dataset.csv"

data_frame = pd.read_csv(file_name, encoding = "ISO-8859-1", error_bad_lines=False)

data_frame['Engine Capacity'] = data_frame['Engine Capacity'].astype(str).str.replace("a997", "1997").astype(float)

data_frame['Metric Urban (Cold)'] = data_frame['Metric Urban (Cold)'].astype(str).str.replace('15..8','15.8').astype(float)

data_frame['Metric Extra-Urban'].apply(lambda x:float(x))
data_frame['Metric Combined'].apply(lambda x:float(x))
data_frame['Imperial Urban (Cold)'].apply(lambda x:float(x))
data_frame['Imperial Extra-Urban'].apply(lambda x:float(x))
data_frame['Imperial Combined'].apply(lambda x:float(x))
data_frame['CO2'].apply(lambda x:float(x))
data_frame['Noise Level dB(A)'].apply(lambda x:float(x))

data_frame['Emissions CO'] = data_frame['Emissions CO'].astype(str).str.replace('*','0').astype(float)

data_frame['THC Emissions'].apply(lambda x:float(x))

data_frame['Emissions NOx'] = data_frame['Emissions NOx'].astype(str).str.replace(',','.').replace('*','0').astype(float)

data_frame['THC + NOx Emissions'] = data_frame['THC + NOx Emissions'].astype(str).str.replace(',','.').astype(float)

data_frame['Particulates'] = data_frame['Particulates'].astype(str).str.replace(',','.').astype(float)

data_frame['Fuel Cost 12000 Miles'] = data_frame['Fuel Cost 12000 Miles'].astype(str).str.replace('Â£','')
data_frame['Fuel Cost 12000 Miles'] = data_frame['Fuel Cost 12000 Miles'].astype(str).str.replace(',','').astype(float)

data_frame['Standard 12 months'] = data_frame['Standard 12 months'].astype(str).str.replace('Â£','')
data_frame['Standard 12 months'] = data_frame['Standard 12 months'].astype(str).str.replace(',','').astype(float)

data_frame['Standard 6 Months'] = data_frame['Standard 6 Months'].astype(str).str.replace('Â£','').astype(float)

data_frame['1st year 12 months'] = data_frame['1st year 12 months'].astype(str).str.replace('Â£','')
data_frame['1st year 12 months'] = data_frame['1st year 12 months'].astype(str).str.replace(',','').astype(float)

data_frame['1st year 6 months'] = data_frame['1st year 6 months'].astype(str).str.replace('Â£','').astype(float)

print(data_frame)
data_frame.to_csv(file_name, index=False)