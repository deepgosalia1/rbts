import config as cg
from flask import json

class CreateUser: 

    id = 1

    def __init__(self,first_name,last_name,age,ssn,email,password,ph_no):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ssn = ssn
        self.email = email
        self.password = password
        self.ph_no = ph_no

    def __init__(self,name,username,password,type):
        self.name = name
        self.username = username
        self.password = password
        self.type = type

    def createClient(self):
        conn = cg.connect_to_azure()
        cursor = conn.cursor()
        qry1 = f"INSERT INTO [dbo].[users](userid,username,pass_hash,type) VALUES ({id},'{self.username}','{self.password}','{self.type}')"
        qry2 = f"INSERT INTO [dbo].[client](cid,email,btcwallet,fiatwallet,phone,fname,lname,clientstatus,clientstreet,clientzip,clientstate,clientcountry) VALUES ({id},'{self.email}',{self.btwallet},{self.fiatwallet},)"
        #user_type = cursor.fetchone()[0]
        # cursor.execute(chk)
        # user_type = cursor.fetchone()
        json_user_data = df.to_json(orient = "index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
