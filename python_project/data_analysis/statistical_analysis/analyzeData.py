import pandas as pd
import matplotlib.pyplot as plt
import plotly

columns_list = ['Manufacturer', 'Model', 'Description', 'AorM', 'Transmission', 'Engine Capacity',
                   'Fuel Type', 'Metric Urban (Cold)', 'Metric Extra-Urban', 'Metric Combined', 'Imperial Urban (Cold)',
                   'Imperial Extra-Urban', 'Imperial Combined', 'CO2', 'Euro standard', 'Noise Level dB(A)',
                   'Emissions CO', 'THC Emissions', 'Emissions NOx', 'THC + NOx Emissions',
                   'Particulates', 'Date of change', 'Fuel Cost 12000 Miles', 'Tax band', 'Standard 12 months',
                   'Standard 6 Months', '1st year 12 months', '1st year 6 months']

file_name = "../../dissertation_datasets/merged_dataset.csv"
data_frame = pd.read_csv(file_name, encoding = "ISO-8859-1", error_bad_lines=False)

# fig = plt.figure(figsize=(20, 25))
# data_frame.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
# plt.savefig("plots/all_density_plot.png")
# plt.close(fig)
#
# scatter_matrix(data_frame)
# plt.show()

# data_frame['Fuel Type'].value_counts().plot('bar')
# plt.show()

fig = plt.figure(figsize=(10, 10))
data_frame['Euro standard'].value_counts().plot('bar')
plt.savefig("plots/euro_standard_hist.png")
plt.close(fig)

fig = plt.figure(figsize=(20, 14))
data_frame['Manufacturer'].value_counts().plot('bar')
plt.savefig("plots/manufacturer_hist.png")
plt.close(fig)

fig = plt.figure(figsize=(20, 14))
data_frame['Engine Capacity'].value_counts().plot('bar')
plt.savefig("plots/engine_capacity_hist.png")
plt.close(fig)

data_frame.hist()
plt.show()