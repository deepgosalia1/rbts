import pandas as pd
from pandas.io import json
import config as cg
from flask import jsonify

class Trader:
    
    def __init__(self,key):
        self.key = key

    def searchKey(self):
        conn = cg.connect_to_azure()
        qry = f"SELECT txid,t.cid,txdate,txtype,txstatus,commamount,commtype,btcamount,fiatamount,txamount,tid,email,btcwallet,fiatwallet,phone,fname,lname,clientstatus,clientstreet,clientzip,clientstate,clientcountry FROM [dbo].[transactions] t, [dbo].[client] c WHERE t.cid = c.cid"
        df = pd.read_sql(qry,conn)
        dfMatch = df[df.apply(lambda row : row.astype(str).str.contains(str(self.key)).any(), axis=1)]
        json_user_data = dfMatch.to_json(orient = "index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
    
    def listTransactions(slef):
        conn = cg.connect_to_azure()
        qry = f"SELECT * FROM [dbo].[transactions]"
        df = pd.read_sql(qry,conn)
        json_user_data = df.to_json(orient = "index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
