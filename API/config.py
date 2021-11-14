#Establish connection to AzureSQL

import pyodbc
import textwrap

#specify driver
driver = '{ODBC Driver 17 for SQL Server}'

#specify server name and Database name
server_name =  ''
database_name = ''

#create server URL
server = ''

#define username and password
username = ''
password = ''

#create the full connection string
connection_string = textwrap.dedent('''
    Driver={driver};
    Server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
'''.format(
    driver=driver,
    server=server,
    database=database_name,
    username=username,
    password=password
))

#Create new pyodbc connection object
cnxn: pyodbc.Connection = pyodbc.connect(connection_string)

#Create a new Cursor object from connection
crsr: pyodbc.Cursor = cnxn.cursor()

#Define a Select query for test
select_sql = "SELECT * FROM [table_name]"

#Executing the query
crsr.execute(select_sql)
##INSERT##
#define an insert query
insert_sql = "INSERT INTO [table_name] (attributes) VALUES (?,?,?)"

#Define records
records = [
    ('ABX','ccn','400'),
    ('ABC','csxx','600')
]

#Define the datatypes of input values
crsr.setinputsize([
    (pyodbc.SQL_VARCHAR,50,0),
    (pyodbc.SQL_VARCHAR,50,0)
])

#Execute the insert statement
crsr.executemany(insert_sql,records)
##

#Commit the transaction to see output in DB
crsr.commit()

#Grab the data
print(crsr.fetchall())

#Close connection once done
cnxn.close()