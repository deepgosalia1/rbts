import pandas as pd
from flask import jsonify
from pandas.core import indexing
from pandas.core.dtypes.missing import notnull
import config as cg
from pandas.io import json


class Client:
    def __init__(self, cid, fiatwallet=None):
        self.cid = cid
        self.fiatwallet = fiatwallet

    def get_transactions(self):
        conn = cg.connect_to_azure()
        qry = f"SELECT * FROM [dbo].[transactions] WHERE cid={self.cid}"
        df = pd.read_sql(qry, conn)
        json_user_data = df.to_json(orient="index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)