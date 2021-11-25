import pandas as pd
from flask import jsonify
import config as cg
from pandas.io import json

class Manager:

    def __init__(self, type):
        self.type=type
    
    def __init__(self,id,start_date,end_date):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date

    def retrieve_data(self):
        conn = cg.connect_to_azure()
        qry = f"SELECT * FROM [dbo].[{self.type}]"
        df = pd.read_sql(qry,conn)
        json_user_data = df.to_json(orient = "index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
    
    def retrieve_transaction_range_day(self):
        conn = cg.connect_to_azure()
        #get daily aggregates
        qry1 = f"SELECT txdate,MIN(txamount),MAX(txamount),AVG(txamount),COUNT(txamount),SUM(txamount) FROM [dbo].[transactions] WHERE txdate>='{self.start_date}' AND txdate<='{self.end_date}' GROUP BY txdate"
        df = pd.read_sql(qry1,conn)
        json_user_data = df.to_json(orient = "index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
