import pandas as pd
import numpy as np

products = pd.read_csv("products.csv")
order_products__prior = pd.read_csv("order_products__prior.csv")
order_products__prior.head(5)
products.head(5)


products_count = order_products__prior.groupby("product_id").size().reset_index(name='counts')
print(products_count.head())
print(products_count.sort_values(by='counts', ascending=False)[:20])

# how frequent products are ordered in a year
products_count.sort_values(by='counts', ascending=False).plot()
products_count.sort_values(by='counts', ascending=False)[:20].plot()

# top 20 products (order freq)
array = products_count.sort_values(by='counts', ascending=False)[:20]["product_id"]
products[["product_id", "product_name"]].loc[products['product_id'].isin(array)]

array = products_count.sort_values(by='counts', ascending=False)[:20]
array = products_count.sort_values(by='counts', ascending=False)[:20]
print(array["product_id"])

# top 20 products IDs
number_column = array.loc[:,'product_id']
array = number_column.values
print(array)
products.loc[products['product_id'].isin(array)]