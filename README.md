# DillardsAPI
The Dillard’s API provides access to JSON endpoints for Dillard’s transactions that took place from 2014-2016.

Dillard’s Transaction Data API
<h2>Introduction</h2>
The Dillard’s API provides access to JSON endpoints for Dillard’s transactions that took place from 2014-2016. They are designed to meet the demands of enterprise business platforms to understand the customers better.

This API collects different portions of the Dillard’s database. The Dillard’s Department Store Database (UA_Dillards_2016) contains millions of records of information gathered from sales transactions from the Dillard’s stores. For this API, the focus is on the Transaction table within the database. The API returns a JSON object that can be utilized for integration and development.

<h2>Dillard's Transaaction Table</h2>
<img src="https://imgur.com/a/vUY52Ql" alt="Dillard's Transaction Table">

<h2>Endpoint Overview</h2>

/tranamount/
	Endpoint that return data on the number of customers that spent over $500 by transaction date.

/transaction/
	Endpoints that return data around transaction information such as date, time, transaction type, amount, etc.
  
  List amount of customers that spent over $500 (Static API)
  •	For a static API with information on the number of customers that spent over $500 in 2014-2016 by transaction date.
  
  Sample Output
  

