import pandas as pd
from flask import jsonify
from pandas.core import indexing
from pandas.core.dtypes.missing import notnull
import config as cg
from pandas.io import json


class Manager:

    def __init__(self, type, id, start_date, end_date):
        self.type = type
        self.id = id
        self.start_date = start_date
        self.end_date = end_date

    def retrieve_data(self):
        conn = cg.connect_to_azure()
        qry = f"SELECT * FROM [dbo].[{self.type}]"
        df = pd.read_sql(qry, conn)
        json_user_data = df.to_json(orient="index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)

    def retrieve_transaction_range_day(self):
        conn = cg.connect_to_azure()
        # get daily aggregates
        qry1 = f"SELECT txdate,MIN(txamount) as min,MAX(txamount) as max,AVG(txamount) as average,COUNT(txamount) as count,SUM(txamount) as sum FROM [dbo].[transactions] WHERE txdate >= '{self.start_date}' AND txdate <= '{self.end_date}' GROUP BY txdate"
        df1 = pd.read_sql(qry1, conn,).astype({"txdate": str})
        print(df1)
        json_user_data = df1.to_json(orient="index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)

    def retrieve_transaction_range_week(self):
        dfWeekly = pd.DataFrame(
            columns=['txdate', 'min', 'max', 'avg', 'count', 'sum'])
        conn = cg.connect_to_azure()
        qry2 = f"SELECT txdate,MIN(txamount) as min,MAX(txamount) as max,AVG(txamount) as average,COUNT(txamount) as count,SUM(txamount) as sum FROM [dbo].[transactions] WHERE txdate >= '{self.start_date}' AND txdate <= '{self.end_date}' GROUP BY txdate"
        df2 = pd.read_sql(qry2, conn)
        print(df2)
        sum = 0
        avg = 0
        count = 1
        cnttrans = 0
        lismin = []
        lismax = []
        for i in range(len(df2['txdate'])):
            sum += df2['sum'][i]
            cnttrans += df2['count'][i]
            lismin.append(df2['min'][i])
            lismax.append(df2['max'][i])
            if count % 7 == 0:
                avg = sum/cnttrans
                date = f"{df2['txdate'][i-7]} - {df2['txdate'][i]}"
                dfWeekly.append({'txdate': date, 'min': min(lismin), 'max': max(
                    lismax), 'avg': avg, 'count': count, 'sum': sum})
                lismax = []
                lismin = []
                sum = 0
                avg = 0
                count += 1
            elif not count % 7 == 0:
                count += 1
        json_user_data = dfWeekly.to_json(orient="index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)

    def retrieve_transaction_range_month(self):
        dfMonthly = pd.DataFrame(
            columns=['txdate', 'min', 'max', 'avg', 'count', 'sum'])
        conn = cg.connect_to_azure()
        qry2 = f"SELECT txdate,MIN(txamount) as min,MAX(txamount) as max,AVG(txamount) as average,COUNT(txamount) as count,SUM(txamount) as sum FROM [dbo].[transactions] WHERE txdate >= '{self.start_date}' AND txdate <= '{self.end_date}' GROUP BY txdate"
        df2 = pd.read_sql(qry2, conn)
        sum = 0
        avg = 0
        count = 1
        cnttrans = 0
        lismin = []
        lismax = []
        for i in range(len(df2['txdate'])):
            sum += df2['sum'][i]
            cnttrans += df2['count'][i]
            lismin.append(df2['min'][i])
            lismax.append(df2['max'][i])
            if count % 30 == 0:
                avg = sum/cnttrans
                date = f"{df2['txdate'][i-7]} - {df2['txdate'][i]}"
                dfMonthly.append({'txdate': date, 'min': min(lismin), 'max': max(
                    lismax), 'avg': avg, 'count': count, 'sum': sum})
                lismax = []
                lismin = []
                sum = 0
                avg = 0
                count += 1
            elif not count % 7 == 0:
                count += 1
        json_user_data = dfMonthly.to_json(orient="index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
