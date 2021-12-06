import pandas as pd
from flask import jsonify
from pandas.core import indexing
from pandas.core.dtypes.missing import notnull
import config as cg
from pandas.io import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Client:
    def __init__(self, cid=None, fiatwallet=None):
        self.cid = cid
        self.fiatwallet = fiatwallet

    def get_transactions(self):
        conn = cg.connect_to_azure()
        qry = f"SELECT * FROM [dbo].[transactions] WHERE cid={self.cid} ORDER BY txid ASC;"
        df = pd.read_sql(qry, conn)
        json_user_data = df.to_json(orient="index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
    
    def updateClientStatus(self):
        currentDate = datetime.now()
        fromDate = currentDate + relativedelta(months=-1)
        currentDate = currentDate.strftime("%Y-%m-%d")
        fromDate = fromDate.strftime("%Y-%m-%d")
        print(currentDate,fromDate)
        conn = cg.connect_to_azure()
        cursor = conn.cursor()
        qry2 = f"SELECT cid,SUM(txamount) as sum FROM [dbo].[transactions] WHERE txdate >=? AND txdate <=? GROUP BY cid"
        params = (fromDate, currentDate)
        df2 = pd.read_sql(qry2, conn, params=params)
        print(df2)
        for i in range(len(df2['cid'])):
            cid = df2['cid'][i]
            if df2['sum'][i] >= 100000:
                updqry = f"UPDATE client SET clientstatus = 1 WHERE cid={cid}"
                cursor.execute(updqry)
                conn.commit()
                cursor.close()
                conn.close()