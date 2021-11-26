import pandas as pd
from flask import jsonify
from pandas.core import indexing
from pandas.core.dtypes.missing import notnull
import config as cg
from pandas.io import json


class Logs:
    def __init__(self, txid, date, tid=None, cid=None, action=None):
        self.txid = txid
        self.date = date
        self.tid = tid
        self.cid = cid
        self.action = action

    def insertLog(self):
        conn = cg.connect_to_azure()
        qry = f"INSERT INTO [dbo].[log] VALUES ({self.txid},'{self.date}',{self.tid},{self.cid},'{self.action}')"
        df = pd.read_sql(qry, conn)
        json_user_data = df.to_json(orient="index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
