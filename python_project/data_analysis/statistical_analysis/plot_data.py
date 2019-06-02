import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd

plotly.tools.set_credentials_file(username='anagabriela.barbieru', api_key='L2wWe1NTSxLvishVA3O1')
file_name = "../../dissertation_datasets/merged_dataset.csv"
data = pd.read_csv(file_name, encoding = "ISO-8859-1", error_bad_lines=False)


x = data['Euro standard']
euro_hist = [go.Histogram(
    x=x, ybins=dict(start=np.min(x.value_counts()), size=0.25, end=np.max(x.value_counts())),
    marker=dict(color='rgb(0, 0, 100)'),
    )]

py.plot(euro_hist, filename='euro-standard histogram')

x = data['Manufacturer']
manufacturer_hist = [go.Histogram(
    x=x, ybins=dict(start=np.min(x.value_counts()), size=0.25, end=np.max(x.value_counts())),
    marker=dict(color='rgb(0, 0, 100)'),
    )]

py.plot(manufacturer_hist, filename='manufacturer histogram')


x = data['Fuel Type']
fuel_type_hist = [go.Histogram(
    x=x, ybins=dict(start=np.min(x.value_counts()), size=0.25, end=np.max(x.value_counts())),
    marker=dict(color='rgb(0, 0, 100)'),
    )]

py.plot(fuel_type_hist, filename='fuel type histogram')


euro_group =  data.groupby('Euro standard')

euro_co2 = [go.Scatter(
    x = [k  for  k in  euro_group.indices],
    y = euro_group['CO2'].mean()
)]

py.plot(euro_co2, filename='Euro CO2 Mean Plots')

euro_urban_cold = [go.Scatter(
    x = [k  for  k in  euro_group.indices],
    y = euro_group['Metric Urban (Cold)'].mean()
)]

py.plot(euro_urban_cold, filename='Euro - Metric Urban Cold Mean Plot')

euro_metric_extra_urban = [go.Scatter(
    x = [k  for  k in  euro_group.indices],
    y = euro_group['Metric Extra-Urban'].mean()
)]

py.plot(euro_metric_extra_urban, filename='Euro - Metric Extra-Urban Mean Plot')