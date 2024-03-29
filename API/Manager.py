import pandas as pd
import requests
import config as cg
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pandas.io import json


class Manager:

    def __init__(self, start_date=None, end_date=None, type=None, id=None):
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
        print(self.start_date)
        # get daily aggregates
        qry2 = f"SELECT txdate,MIN(txamount) as min,MAX(txamount) as max,AVG(txamount) as average,COUNT(txamount) as count,SUM(txamount) as sum FROM [dbo].[transactions] WHERE txdate >=? AND txdate <=? GROUP BY txdate"
        params = (self.start_date, self.end_date)
        df1 = pd.read_sql(qry2, conn, params=params).astype({"txdate": str})
        print(df1)
        json_user_data = df1.to_json(orient="index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)

    def retrieve_transaction_range_week(self):
        dfWeekly = pd.DataFrame(
            columns=['txdate', 'min', 'max', 'avg', 'count', 'sum'])
        conn = cg.connect_to_azure()
        qry2 = f"SELECT txdate,MIN(txamount) as min,MAX(txamount) as max,AVG(txamount) as average,COUNT(txamount) as count,SUM(txamount) as sum FROM [dbo].[transactions] WHERE txdate >=? AND txdate <=? GROUP BY txdate"
        params = (self.start_date, self.end_date)
        df2 = pd.read_sql(qry2, conn, params=params)
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
                date = f"{df2['txdate'][i-6]} - {df2['txdate'][i]}"
                dfWeekly = dfWeekly.append({'txdate': date, 'min': min(lismin), 'max': max(
                    lismax), 'avg': avg, 'count': cnttrans, 'sum': sum}, ignore_index=True)
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
        qry2 = f"SELECT txdate,MIN(txamount) as min,MAX(txamount) as max,AVG(txamount) as average,COUNT(txamount) as count,SUM(txamount) as sum FROM [dbo].[transactions] WHERE txdate >=? AND txdate <=? GROUP BY txdate"
        params = (self.start_date, self.end_date)
        df2 = pd.read_sql(qry2, conn, params=params)
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
                date = f"{df2['txdate'][i-29]} - {df2['txdate'][i]}"
                dfMonthly = dfMonthly.append({'txdate': date, 'min': min(
                    lismin), 'max': max(lismax), 'avg': avg, 'count': cnttrans, 'sum': sum})
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

    def updateClientStatus(self):
        currentDate = datetime.now()
        fromDate = currentDate + relativedelta(months=-1)
        currentDate = currentDate.strftime("%Y-%m-%d")
        fromDate = fromDate.strftime("%Y-%m-%d")
        try:
            uResponse = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            Jresponse = uResponse.text
            data = json.loads(Jresponse)
        except Exception as e:
            print(e)
        currBTC = data['bpi']['USD']['rate']
        currBTC = float(currBTC.replace(',',''))
        conn = cg.connect_to_azure()
        cursor = conn.cursor()
        qry2 = f"SELECT cid,SUM(txamount) as sum FROM [dbo].[transactions] WHERE txdate >=? AND txdate <=? GROUP BY cid"
        params = (fromDate, currentDate)
        df2 = pd.read_sql(qry2, conn, params=params)
        for i in range(len(df2['cid'])):
            cid = df2['cid'][i]
            if (df2['sum'][i]* currBTC) >= 100000:
                updqry = f"UPDATE client SET clientstatus = 1 WHERE cid={cid}"
                cursor.execute(updqry)
                conn.commit()
                cursor.close()
                conn.close()
