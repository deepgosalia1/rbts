import pandas as pd
from flask import jsonify
from pandas.core.dtypes.missing import notnull
import config as cg
from pandas.io import json

class Manager:
    
    def __init__(self,type,id,start_date,end_date):
        self.type = type
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
        df1 = pd.read_sql(qry1,conn)
        print(df1)
        qry2 = f"SELECT txdate,txamount FROM [dbo].[transactions] WHERE txdate>='{self.start_date}' AND txdate<='{self.end_date}'"
        df2 = pd.read_sql(qry2,conn)
        print(df2)
        for index,row in df2.iterrows():
            sum = 0
            avg = 0
            if not index%7==0:
                if row['txamount']:
                    sum = sum + row['txamount']
                    print("sum",sum)
                else:
                    break
            avg = sum/7
            print(avg)
        json_user_data = df1.to_json(orient = "index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
