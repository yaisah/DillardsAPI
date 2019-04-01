#Yaisah Granillo
#Assignment 3A - Dynamic API
##
#Import Modules
from flask import Flask
import urllib.request, urllib.parse, urllib.error
import json
import mysql.connector
import pypyodbc #since I wanted to play with the Dillards database, I couldn't use mysql-connector
import collections ##New Module to work with dictionary objects

#definition of the flask app
app = Flask(__name__)

#Route for index page
@app.route('/')
def index():
    ##Database connection and sample query of results
    conn = mysql.connector.connect(host="test", user="TESTUSER", password="TESTUSER", database="TESTUSER")
    c = conn.cursor()
    c.execute("select lat, lng from ADDRESSES") ##Should return a list of query results
    results = c.fetchall() ##Grab the data and save into a variable called "results"
    conn.close()
    objects_list = [] ##Create a new array to hold the records

    ##Loop through each of the rows in the result set and add to the dictionary
    for row in results:
       d = collections.OrderedDict() ##Create a new dictionary
       d['lat'] = row[0]
       d['lng'] = row[1]
       objects_list.append(d) ##Add dictionary to end of list

    ##Print out JSON
    jsonOut = json.dumps(objects_list, indent=4) ##Output the JSON data to a new string called "j" to output or return.

    return jsonOut

##Route for ticker
#Query I'll be using is - How many customers spent more than $500 in a transaction
@app.route('/tranamount/')
def tranamount():
    ##Database connection 
    db_host = 'XXX'
    db_name = 'XXX'
    db_user = 'XXX'
    db_password = 'XXX'
    connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
    conn2 = pypyodbc.connect(connection_string)

    c = conn2.cursor()
    c.execute("SELECT COUNT(CUST_ID) as TotalCustomers, TRAN_DATE as TransactionDate FROM TRANSACT WHERE TRAN_AMT > 500 GROUP BY TRAN_DATE ORDER BY TRAN_DATE desc")
    results = c.fetchall() ##Grab the data and save into a variable called "results"
    conn2.close()
    objects_list = [] ##Create a new array to hold the records
    
    ##Loop through each of the rows in the result set and add to the dictionary
    for row in results:
       d = collections.OrderedDict() ##Create a new dictionary
       d['TotalCustomers'] = row[0]
       d['TransactionDate'] = row[1]
       objects_list.append(d) ##Add dictionary to end of list

    ##Print out JSON
    jsonOut = json.dumps(objects_list, indent=4) ##Output the JSON data to a new string called "j" to output or return.

    return jsonOut

##Route for Ticker with ID
@app.route('/transaction/<ID>')
def transactionSpecific(ID):
    ##Get the ID variable
    transactionID = ID
    ##Database connection and sample query of results
    db_host = 'XXX'
    db_name = 'UA_DILLARDS_2016'
    db_user = 'XXX'
    db_password = 'XXX'
    connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
    conn2 = pypyodbc.connect(connection_string)

    c = conn2.cursor()
    c.execute("SELECT * FROM TRANSACT WHERE TRANSACTION_ID = '" + transactionID + "'")
    results = c.fetchall() ##Grab the data and save into a variable called "results"
    conn2.close()
    objects_list = [] ##Create a new array to hold the records

    ##Loop through each of the rows in the result set and add to the dictionary
    for row in results:
       d = collections.OrderedDict() ##Create a new dictionary
       d['TRANSACTION_ID'] = row[0]
       d['TRAN_DATE'] = row[1]
       d['STORE'] = row[2]
       d['REGISTER'] = row[3]
       d['TRAN_NUM'] = row[4]
       d['TRAN_TIME'] = row[5]
       d['CUST_ID'] = row[6]
       d['TRAN_LINE_NUM'] = row[7]
       d['DEPT'] = row[8]
       d['MIC'] = row[9]
       d['SKU'] = row[10]
       d['TRAN_TYPE'] = row[11]
       d['ORIG_PRICE'] = str(row[12])
       d['SALE_PRICE'] = str(row[13])
       d['TRAN_AMT'] = str(row[14])
       d['TENDER_TYPE'] = row[15]
       d['ITEM_ID'] = row[16]
       d['ONLINE'] = row[17]
       objects_list.append(d) ##Add dictionary to end of list

    ##Print out JSON
    jsonOut = json.dumps(objects_list, indent=4) ##Output the JSON data to a new string called "j" to output or return.

    return jsonOut

if __name__ == "__main__":
    app.run(debug=True)



