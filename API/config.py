#Establish connection to AzureSQL

import pyodbc
import textwrap

server = 'appbt.database.windows.net'
database = 'bitcoin'
username = 'hita'
password = 'Gdhan@1234'   
driver= '{ODBC Driver 17 for SQL Server}'



conn =  pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password,trusted_connection='no')


#Create a new Cursor object from connection
cursor = conn.cursor()

#Define a Select query for test
select_sql = "SELECT * FROM sys.tables"

#Executing the query
cursor.execute(select_sql)
cursor.execute("SELECT * FROM sys.columns")
##INSERT##
#define an insert query
insert_sql = "INSERT INTO [table_name] (attributes) VALUES (?,?,?)"

#Define records
records = [
    ('ABX','ccn','400'),
    ('ABC','csxx','600')
]


#Execute the insert statement
cursor.executemany(insert_sql,records)
##

#Commit the transaction to see output in DB
cursor.commit()

#Grab the data
print(cursor.fetchall())

#Close connection once done
cursor.close()