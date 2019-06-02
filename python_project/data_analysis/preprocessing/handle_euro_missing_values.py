import os
import pandas as pd

count_files = 0

file_name = "../../dissertation_datasets/merged_dataset.csv"

for root, dirs, files in os.walk("../../dissertation_datasets", topdown=False):
    for name in files:
        if (name.endswith(".csv")) and ("merged_dataset.csv" not in name):
            fileName = os.path.join(root, name)
            print(fileName)
            data_frame = pd.read_csv(fileName, encoding = "ISO-8859-1", error_bad_lines=False)
            file_columns = data_frame.columns.values.tolist()
            flag = 0
            for column in file_columns:

                if column.lower() == 'euro standard':
                    flag = 1
                    if data_frame[column].isna().any():
                        print("NA")
                        print(data_frame[column])

            if flag == 0:
                print("No column")

