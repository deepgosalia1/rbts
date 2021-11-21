#Establish connection to AzureSQL
import pyodbc
import pandas as pd
azure ={
'server' : 'bitcoinserver.database.windows.net',
'database' : 'bitcoin',
'username' : 'hita123',
'password' : 'Hita@123',   
'driver' : '{ODBC Driver 17 for SQL Server}'
}

def connect_to_azure():
    conn =  pyodbc.connect('DRIVER='+azure['driver']+';SERVER=tcp:'+azure['server']+';PORT=1433;DATABASE='+azure['database']+';UID='+azure['username']+';PWD='+ azure['password'],trusted_connection='no')
    return conn

# #Create a new Cursor object from connection
# cursor = conn.cursor()
# #Define a Select query for test
# select_sql = "SELECT * FROM [dbo].[user_accounts]"

# #Executing the query
# cursor.execute(select_sql)

# # ##INSERT##
# # #define an insert query
# # insert_sql = "INSERT INTO [table_name] (attributes) VALUES (?,?,?)"

# # #Define records
# # records = [
# #     ('ABX','ccn','400'),
# #     ('ABC','csxx','600')
# # ]


# # #Execute the insert statement
# # cursor.executemany(insert_sql,records)
# # ##

# # #Commit the transaction to see output in DB
# #cursor.commit()

# # #Grab the data
# data = cursor.fetchall()
# print(data)
# #Close connection once done
# cursor.close()