import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2


conn = psycopg2.connect("dbname = instacart user = tmccormack")
cur = conn.cursor()


cur.execute("SELECT COUNT(*),pname FROM heavyProducts GROUP BY pname ORDER BY COUNT(*) DESC;")
res = cur.fetchall()

c = []
pr = []

z = 0
for i in res:
    c.append(i[0])
    pr.append(z)
    z+= 1
    if(z == 11):
        break


plt.bar(pr,c,  color = ["aquamarine", "red", "pink", "blue", "yellow", "orange"
                        , "purple", "lavender","salmon", "fuchsia"])
plt.xlabel('product')
plt.ylabel('count')
plt.title('Distribution of Top 10 Products for Heavy Users')

plt.savefig("/var/www/NA/static/img/product.png")
plt.show()
    
