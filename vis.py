import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
#import seaborn as sns
#color = sns.pallette()





orders = pd.read_csv('/var/www/NA/backEnd/orders.csv')
op = pd.read_csv('/var/www/NA/backEnd/order_products__prior.csv')
products = pd.read_csv('/var/www/NA/backEnd/products.csv')

print(orders.head(5))

conn = psycopg2.connect("dbname = instacart user = tmccormack")
cur = conn.cursor()

# test printing to std output
print("Hello World")
    
# now run a query that gathers the number of orders for given hours of the day
cur.execute("SELECT COUNT(*), order_hours_of_day FROM orders GROUP BY order_hours_of_day ORDER BY COUNT(*);")

# print to std out all of the hours in a day and their corresponding counts
res = cur.fetchall()

    
numOrders = []
hours = []
    
for i in res:
    print(i[0])
    print(type(i[0]))
    numOrders.append(i[0])
    hours.append(i[1])

#fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#ax.bar( hours,numOrders)
plt.bar(hours,numOrders, color = "aquamarine")
plt.xlabel('hours')
plt.ylabel('# orders')
plt.title('Distribution of Orders Throughout a Day')

plt.savefig("/var/www/NA/static/img/hours.png")
plt.show()

uniq_orders = len(set(op.order_id))
uniq_prod   = len(set(op.product_id))

#plt.bar(uniq_orders, uniq_prod)
#plt.show()
print(uniq_orders)
print(uniq_prod)

xA = [uniq_orders, uniq_prod]
yA = ["Orders", "Products"]

#plt.pie(xA, labels = yA)
#plt.savefig("/var/www/NA/static/img/circle_op.png")
#plt.show()

orderSizes = op.groupby("order_id")["add_to_cart_order"].aggregate("max").reset_index()
orderSizes = orderSizes.add_to_cart_order.value_counts()

f, ax = plt.subplots(figsize=(15,12))
plt.xticks(rotation = 'vertical')
plt.bar(orderSizes.index, orderSizes.values, color = 'aquamarine')


plt.ylabel('# Orders', fontsize=13)
plt.xlabel('Products in Order', fontsize=13)
plt.title('Number of Products in Orders')
plt.savefig("/var/www/NA/static/img/orderSize2.png")
plt.show()

dow = orders.groupby("order_id")["order_dow"].aggregate("sum").reset_index()
dow = dow.order_dow.value_counts()

f, ax = plt.subplots(figsize = (15,12))
plt.bar()








