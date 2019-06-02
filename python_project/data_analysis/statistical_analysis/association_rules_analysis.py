import pandas as pd
from IPython.display import display
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#from apyori import apriori

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

file_name = "../../dissertation_datasets/merged_dataset.csv"
data_frame = pd.read_csv(file_name, encoding = "ISO-8859-1", error_bad_lines=False)

audi_data = (data_frame[data_frame['Manufacturer'] =="AUDI"])
display(audi_data)

oht = TransactionEncoder()
oht_ary = oht.fit(audi_data).transform(audi_data)
df = pd.DataFrame(oht_ary, columns=oht.columns_)

frequent_itemsets = apriori(df, min_support=0.001, use_colnames=True)
print(frequent_itemsets)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
display(rules)

# records = []
# for i in range(0, audi_data.shape[0]):
#     records.append([str(audi_data.values[i,j]) for j in range(0, audi_data.shape[1])])
#
# association_rules = apriori(records, min_support=0.0045, min_confidence=0.5, min_lift=1, min_length=3)
# association_results = list(association_rules)
#
# print(association_results[0])
