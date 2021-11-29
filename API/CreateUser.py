import config as cg
from flask import json
import pandas as pd

class CreateUser: 

    global id

    def __init__(self,first_name,last_name,age,ssn,email,username,password,ph_no,type,clientstreet,clientzip,clientstate,clientcoutnry):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ssn = ssn
        self.email = email
        self.password = password
        self.ph_no = ph_no
        self.username = username
        self.password = password
        self.type = type
        self.clientstreet = clientstreet
        self.clientzip = clientzip
        self.clientstate = clientstate
        self.clientcountry = clientcoutnry
        self.id = 1
    

    def createClient(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry1 = f"INSERT INTO [dbo].[users](username,pass_hash,type) VALUES ('{self.username}','{self.password}','{self.type}')"
            cursor.execute(qry1)
            conn.commit()
            qry_id = f"SELECT userid FROM [dbo].[users] WHERE username = '{self.username}' and pass_hash = '{self.password}'"
            df = pd.read_sql(qry_id,conn)
            c_id = int(df['userid'][0])
            qry2 = f"INSERT INTO [dbo].[client](cid,email,btcwallet,fiatwallet,phone,fname,lname,clientstatus,clientstreet,clientzip,clientstate,clientcountry) VALUES ({c_id},'{self.email}',0,0,{self.ph_no},'{self.first_name}','{self.last_name}',0,'{self.clientstreet}','{self.clientzip}','{self.clientstate}','{self.clientcountry}')"
            #user_type = cursor.fetchone()[0]
            cursor.execute(qry2)
            conn.commit()
            cursor.close()
            conn.close()
            self.id = self.id + 1
            # user_type = cursor.fetchone()
        except Exception as e:
            print(e)    

    def createTrader(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry1 = f"INSERT INTO [dbo].[users](userid,username,pass_hash,type) VALUES ({self.id},'{self.username}','{self.password}','{self.type}')"
            qry2 = f"INSERT INTO [dbo].[trader](tid,fname,lname) VALUES ({id},'{self.first_name}',{self.last_name}')"
            #user_type = cursor.fetchone()[0]
            cursor.execute(qry1)
            cursor.execute(qry2)
            conn.commit()
            cursor.close()
            conn.close()
            self.id = self.id + 1
            # user_type = cursor.fetchone()
        except Exception as e:
            print(e) 

    def createManager(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry1 = f"INSERT INTO [dbo].[users](userid,username,pass_hash,type) VALUES ({self.id},'{self.username}','{self.password}','{self.type}')"
            qry2 = f"INSERT INTO [dbo].[client](mid,fname,lname) VALUES ({id},'{self.first_name}','{self.last_name}')"
            #user_type = cursor.fetchone()[0]
            cursor.execute(qry1)
            cursor.execute(qry2)
            conn.commit()
            cursor.close()
            conn.close()
            self.id = self.id + 1
            # user_type = cursor.fetchone()
        except Exception as e:
            print(e)    

    

