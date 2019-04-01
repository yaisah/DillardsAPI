#Yaisah Granillo
#Assignment 3A - Static API
##
#Import Modules
import urllib.request, urllib.parse, urllib.error
import json
import pypyodbc #since I wanted to play with the Dillards database, I couldn't use mysql-connector
import collections ##New Module to work with dictionary objects

##Database connection to my specific student database from the first semester 2017
db_host = 'XXX'
db_name = 'XXX'
db_user = 'XXX'
db_password = 'XXX'
connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
conn2 = pypyodbc.connect(connection_string)

c = conn2.cursor()

#Query I'll be using is - How many customers spent more than $500 in a transaction
c.execute("SELECT COUNT(CUST_ID) as TotalCustomers, TRAN_DATE as TransactionDate FROM TRANSACT WHERE TRAN_AMT > 500 GROUP BY TRAN_DATE ORDER BY TRAN_DATE desc")

results = c.fetchall()
conn2.close()
objects_list = []

##Adding a dictionary - Loop through each of the rows in the result set
for row in results:
    d = collections.OrderedDict()
    d['TotalCustomers'] = row[0]
    d['TransactionDate'] = row[1]
    objects_list.append(d)

##Print out JSON
js = json.dumps(objects_list, indent=4)

##Output to a flat file
##Print out raw JSON to console
print(json.dumps(js, indent=4))

##Save raw JSON to text file
fileOut = open('myStaticAPI.json', 'wt')

fileOut.write(js)

fileOut.close()
