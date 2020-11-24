import psycopg2
import csv
import matplotlib

def main():

    conn = psycopg2.connect("dbname = instacart user = tmccormack")
    cur = conn.cursor()

    # test printing to std output
    print("Hello World")
    
    # now run a query that gathers the number of orders for given hours of the day
    cur.execute("SELECT COUNT(*), order_hours_of_day FROM orders GROUP BY order_hours_of_day ORDER BY COUNT(*);")

    # print to std out all of the hours in a day and their corresponding counts
    res = cur.fetchall()

    
    numOrders = []
    
    for i in res:
        print(i[0])
        print(type(i[0]))

main()
