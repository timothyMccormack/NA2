import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
#import seaborn as sns
#color = sns.pallette()





orders = pd.read_csv('/var/www/NA/backEnd/orders.csv')
op = pd.read_csv('/var/www/NA/backEnd/order_products__prior.csv')
products = pd.read_csv('/var/www/NA/backEnd/products.csv')

#print(orders.head(5))

conn = psycopg2.connect("dbname = instacart user = tmccormack")
cur = conn.cursor()

'''
# now run a query that gathers the number of orders for given hours of the day
cur.execute("SELECT COUNT (*),user_id FROM orders GROUP BY (user_id) ORDER BY COUNT(*) DESC;")

# print to std out all of the hours in a day and their corresponding counts
res = cur.fetchall()

no = []

for i in res:
    #print(i)
    no.append(i[0])
    
plt.hist(no, bins = 20, color = "red")
plt.title("Distribution of Orders per User")
plt.xlabel("# orders")
plt.ylabel("# users")
plt.savefig("/var/www/NA/static/img/uo3.png")
plt.show()

'''    

cur.execute("SELECT user_id FROM heavyusers WHERE user_id = 67023;")
res = cur.fetchall()

heavyUsers = []

for i in res:
    heavyUsers.append(i[0])

print(heavyUsers)

oids = []

z = 0
ix = 0
for j in heavyUsers:
    cur.execute("SELECT order_id FROM orders WHERE user_id = %s;",(j,))
    res2 = cur.fetchall()
    
    for k in res2:
        oids.append(k[0])
    
    z += 1
    #if(z > 3):
        #break
        
    

print(oids)


pid = []
ix = 0
for l in oids:
    cur.execute("SELECT product_id FROM orderproducts WHERE order_id = %s;",(l,))
    res3 = cur.fetchall()

    for m in res3:
        pid.append(m[0])
        ix += 1
        #if(ix > 3):
            #break
    #if(ix > 3):
        #break

print(pid)

pnames = []
for o in pid:
    cur.execute("SELECT product_name FROM products WHERE product_id = %s;", (o,))
    res4 = cur.fetchall()
    for i in res4:
        pnames.append(i[0])

print(pnames)
    
    
#plt.hist(pnames, color = "red")
#plt.title("Distribution of Heavy User Purchases")
#plt.xlabel("product")
#plt.ylabel("frequecy")
#plt.savefig("/var/www/NA/static/img/pro1.png")
#plt.show()

#pnames = ["juice", "apples", "carrots"]

for h in range(len( pnames)):
    cur.execute("INSERT INTO heavyProducts (pname) VALUES (%s);", (pnames[h],))
    #cur.execute("INSERT INTO heavyProducts (pname) VALUES('juice');")
#print(pnames)



conn.commit()
cur.close()
conn.close()
