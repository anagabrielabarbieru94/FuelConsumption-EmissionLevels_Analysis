import os
import pandas as pd

count_files = 0


columns_list = ['Manufacturer', 'Model', 'Description', 'AorM', 'Transmission', 'Engine Capacity',
                   'Fuel Type', 'Metric Urban (Cold)', 'Metric Extra-Urban', 'Metric Combined', 'Imperial Urban (Cold)',
                   'Imperial Extra-Urban', 'Imperial Combined', 'CO2', 'Euro standard', 'Noise Level dB(A)',
                   'Emissions CO', 'THC Emissions', 'Emissions NOx', 'THC + NOx Emissions',
                   'Particulates', 'Date of change', 'Fuel Cost 12000 Miles', 'Tax band', 'Standard 12 months',
                   'Standard 6 Months', '1st year 12 months', '1st year 6 months']

file_name = "../../dissertation_datasets/merged_dataset.csv"

merge_df = pd.DataFrame(columns=columns_list)
print(merge_df)

for root, dirs, files in os.walk("../../dissertation_datasets", topdown=False):
    for name in files:
        if (name.endswith(".csv")) and ("merged_dataset.csv" not in name):
            fileName = os.path.join(root, name)
            print(fileName)
            data_frame = pd.read_csv(fileName, encoding = "ISO-8859-1", error_bad_lines=False)
            file_columns = data_frame.columns.values.tolist()

            df = pd.DataFrame()
            idx = 0
            for column in columns_list:
                match = [x for x in file_columns if column.lower() in x.lower()]
                if len(match) != 0:
                    data = data_frame.get(match[0])
                    df.insert(loc = idx, column = column, value=data)
                else:
                    df.insert(loc = idx, column = column, value=None)
                idx += 1

            if count_files == 0:
                merge_df = df
            else:
                merge_df = merge_df.append(df, ignore_index=True)

            count_files += 1

merge_df.to_csv(file_name, index=False)

