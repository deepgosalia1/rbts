import pandas as pd
from pandas.io import json
import config as cg
from flask import jsonify


class Trader:

    def __init__(self, key=None, type=None):
        self.key = key
        self.type = type

    def searchKey(self):
        conn = cg.connect_to_azure()
        qry = f"SELECT * FROM [dbo].[{self.type}]"
        df = pd.read_sql(qry, conn)
        dfMatch = df[df.apply(lambda row: row.astype(
            str).str.contains(str(self.key)).any(), axis=1)]
        json_user_data = dfMatch.to_json(orient="index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)

    def listTransactions(self):
        conn = cg.connect_to_azure()
        qry = f"SELECT * FROM [dbo].[transactions] ORDER BY txid DESC"
        df = pd.read_sql(qry, conn)
        json_user_data = df.to_json(orient="index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)

    def pendingTransactions(self):
        conn = cg.connect_to_azure()
        qry = f"select * from transactions t where t.txstatus = 0 order by txid asc"
        df = pd.read_sql(qry, conn)
        dfMatch = df[df.apply(lambda row: row.astype(
            str).str.contains(str(self.key)).any(), axis=1)]
        json_user_data = dfMatch.to_json(orient="index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
