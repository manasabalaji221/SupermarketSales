SupermarketSales
Name : Manasa Balaji 
Mail:  manasa.balaji@mavs.uta.edu

Link to Github Repository:
https://github.com/manasabalaji221/SupermarketSales

Link to the web application:
https://marketsalesapp1.azurewebsites.net/

For this web application, I have used the Supermarket Sales Dataset from Kaggle. It has a list of invoices created at a supermarket and it’s details. There are 17 attributes in this dataset and around 1000 values. The attributes are [Invoice ID], Branch, City, [Customer type], Gender, [Product line], [Unit price], Quantity, [Tax 5%], Total, Date, Time, Payment, cogs, [gross margin percentage], [gross income] and Rating. 

The application is built on a Python Flask application with the front end being HTML, CSS. I hosted this application on Microsoft Azure App Service. The database server used was an SQL server and the database was the SQL database on Azure. 

I implemented the given problems in 4 questions. 
1.	Fetch required data from the database.
Used a form for the user to enter a date and it return all the transactions that took place on that particular date.

2.	Record a sale
This uses a form to allow the user to manually enter the details of a sale that occurred. The total, tax, GMP, GI, etc is calculated and would display a message once the invoice has been entered into the database.

3.	Change the type of Customer (Member/Normal)
Here, we can change the type of user from member to normal or vice versa.

4.	Analysis of data
The different categories and their impact on the sales is reflected using charts.

 


Reference links:
Dataset: https://www.kaggle.com/aungpyaeap/supermarket-sales
https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/
https://www.w3schools.com/python/python_mysql_insert.asp
https://azure.microsoft.com/en-us/services/app-service/#features

