import config as cg
from flask import json

class CreateUser: 

    global id

    def __init__(self,first_name,last_name,age,ssn,email,password,ph_no):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ssn = ssn
        self.email = email
        self.password = password
        self.ph_no = ph_no
        self.id = id

    def __init__(self,name,username,password,type):
        self.name = name
        self.username = username
        self.password = password
        self.type = type
        self.id = id

    def createClient(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry1 = f"INSERT INTO [dbo].[users](userid,username,pass_hash,type) VALUES ({self.id},'{self.username}','{self.password}','{self.type}')"
            qry2 = f"INSERT INTO [dbo].[client](cid,email,btcwallet,fiatwallet,phone,fname,lname,clientstatus,clientstreet,clientzip,clientstate,clientcountry) VALUES ({id},'{self.email}',{self.btwallet},{self.fiatwallet},{self.phone},'{self.fname}','{self.lname}',{self.clientstatus},'{self.clientstreet}','{self.clientzip}','{self.clientstate}','{self.clientcountry}')"
            #user_type = cursor.fetchone()[0]
            cursor.execute(qry1)
            cursor.execute(qry2)
            cursor.close()
            self.id = self.id + 1
            # user_type = cursor.fetchone()
        except Exception as e:
            print(e)    

