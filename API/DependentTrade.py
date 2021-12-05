import pandas as pd
from flask import jsonify
from pandas.core import indexing
from pandas.core.dtypes.missing import notnull
import config as cg
from pandas.io import json


class DependentTrade:

    global id

    def __init__(self, cid, txdate, txtype, txstatus, txamount, currBTC=None, commtype=None, txid=None,tid=None):
        self.cid = cid
        self.txdate = txdate
        self.txtype = txtype
        self.txstatus = txstatus
        self.txamount = txamount
        self.currBTC = currBTC
        self.txid = txid
        self.commtype = commtype
        self.tid = tid

    def place_order(self):
        conn = cg.connect_to_azure()
        action = ''
        action = 'Pending'
        try:
            cursor = conn.cursor()
            qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, txamount,commtype) VALUES ({self.cid},'{self.txdate}',{self.txtype},{self.txstatus},{self.txamount},'{self.commtype}')"
            cursor.execute(qry1)
            qry2 = f"SELECT TOP 1 * FROM transactions ORDER BY txid DESC"
            df2 = pd.read_sql(qry2, conn)
            txid = df2.at[0, 'txid']
            print('df2:', df2, '\n', 'txid', txid)
            qry2 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({txid},{self.cid},'{self.txdate}','{action}')"
            cursor.execute(qry2)
            conn.commit()
            cursor.close()
            conn.close()
            return "success"
        except Exception as e:
            return f"an Error Occured {e}"

    def approvetrade(self):
        conn = cg.connect_to_azure()
        action = 'Approved'
        try:
            cursor = conn.cursor()
            qry2 = f"SELECT btcwallet,fiatwallet,clientstatus FROM [dbo].[client] WHERE cid = {self.cid}"
            c = pd.read_sql(qry2, conn)
            # btc_wallet
            btc_wallet = c['btcwallet'][0]
            print("btc", btc_wallet)
            # fiat wallet
            fiat_wallet = c['fiatwallet'][0]
            print("fiat", fiat_wallet)
            client_status = c['clientstatus'][0]
            print("clientstatus", client_status)
            amount = self.txamount*self.currBTC
            if (self.txtype == 0):
                if(self.commtype == 'BTC'):
                    if (client_status == 1):
                        btc_amount_check = 0.005 * self.txamount
                        amount_check_fiat = self.txamount * self.currBTC
                    if ( client_status == 0):
                        btc_amount_check = 0.0025 * self.txamount
                        amount_check_fiat = self.txamount * self.currBTC
                        print("BTC",btc_amount_check)
                        print("FIAT",amount_check_fiat)
                    if (btc_wallet >= btc_amount_check and fiat_wallet >= amount_check_fiat):
                        btc_wallet = btc_wallet + self.txamount
                        fiat_wallet = fiat_wallet - amount_check_fiat
                        qry3 = f"UPDATE [dbo].[client] SET btcwallet={btc_wallet},fiatwallet={fiat_wallet} WHERE cid = {self.cid}"
                        cursor.execute(qry3)
                        qry1 = f"UPDATE transactions SET txstatus = 1,tid = {self.tid},commamount = {btc_amount_check} WHERE txid={self.txid}"
                        cursor.execute(qry1)
                        qry4 = f"SELECT TOP 1 * FROM transactions ORDER BY txid DESC"
                        df2 = pd.read_sql(qry4, conn)
                        txid = df2.at[0, 'txid']
                        qry2 = f"INSERT INTO [dbo].[log](txid,tid, cid, time, action) VALUES ({txid},{self.tid},{self.cid},'{self.txdate}','{action}')"
                        cursor.execute(qry2)
                        conn.commit()
                        cursor.close()
                        conn.close()
                        return "success"
                    else:
                        return "Error"
                if ( self.commtype == 'USD'):
                    if ( client_status == 1):
                        amount_check = amount + 0.008 * amount
                    if ( client_status == 0):
                        amount_check = amount + 0.004 * amount
                    if ( fiat_wallet > amount_check):
                        btc_wallet = btc_wallet + self.txamount
                        fiat_wallet = fiat_wallet - amount_check
                        qry3 = f"UPDATE [dbo].[client] SET btcwallet={btc_wallet},fiatwallet={fiat_wallet} WHERE cid = {self.cid}"
                        cursor.execute(qry3)
                        qry1 = f"UPDATE transactions SET txstatus = 1,tid = {self.tid},commamount = {amount_check} WHERE txid={self.txid}"
                        qry1 = f"UPDATE transactions SET txstatus = 1,tid = {self.tid},commamount = {float(amount_check)} WHERE txid={self.txid}"
                        cursor.execute(qry1)
                        qry4 = f"SELECT TOP 1 * FROM transactions ORDER BY txid DESC"
                        df2 = pd.read_sql(qry4, conn)
                        txid = df2.at[0, 'txid']
                        qry2 = f"INSERT INTO [dbo].[log](txid,tid, cid, time, action) VALUES ({txid},{self.tid},{self.cid},'{self.txdate}','{action}')"
                        cursor.execute(qry2)
                        conn.commit()
                        cursor.close()
                        conn.close()
                        return "success"
                    else:
                        return "Error"
            if (self.txtype == 1):
                if(self.commtype == 'BTC'):
                    if (client_status == 1):
                        btc_amount_check = 0.005 * self.txamount + self.txamount
                    if ( client_status == 0):
                        btc_amount_check = 0.0025 * self.txamount + self.txamount
                    if (btc_wallet > btc_amount_check):
                        btc_wallet = btc_wallet - btc_amount_check
                        fiat_wallet = fiat_wallet + btc_amount_check * self.currBTC
                        qry3 = f"UPDATE [dbo].[client] SET btcwallet={btc_wallet},fiatwallet={fiat_wallet} WHERE cid = {self.cid}"
                        cursor.execute(qry3)
                        qry1 = f"UPDATE transactions SET txstatus = 1,tid = {self.tid},commamount = {btc_amount_check} WHERE txid={self.txid}"
                        cursor.execute(qry1)
                        qry4 = f"SELECT TOP 1 * FROM transactions ORDER BY txid DESC"
                        df2 = pd.read_sql(qry4, conn)
                        txid = df2.at[0, 'txid']
                        qry2 = f"INSERT INTO [dbo].[log](txid, tid, cid, time, action) VALUES ({txid},{self.tid},{self.cid},'{self.txdate}','{action}')"
                        cursor.execute(qry2)
                        conn.commit()
                        cursor.close()
                        conn.close()
                        return "success"
                if(self.commtype == 'USD'):
                    if (client_status == 1):
                        amount_check_new = self.txamount
                        amount_check_fiat_new = 0.005 * self.txamount * self.currBTC
                    if ( client_status == 0):
                        amount_check_new = self.txamount
                        amount_check_fiat_new = 0.0025 * self.txamount * self.currBTC
                    if ( btc_wallet >= amount_check_new and fiat_wallet >= amount_check_fiat_new):
                          btc_wallet = btc_wallet - amount_check_new
                          fiat_wallet = fiat_wallet + (self.txamount * self.currBTC) - amount_check_fiat_new
                          qry3 = f"UPDATE [dbo].[client] SET btcwallet={btc_wallet},fiatwallet={fiat_wallet} WHERE cid = {self.cid}"
                          cursor.execute(qry3)
                          qry1 = f"UPDATE transactions SET txstatus = 1,tid = {self.tid}, commamount = {amount_check_fiat_new} WHERE txid={self.txid}"
                          cursor.execute(qry1)
                          qry4 = f"SELECT TOP 1 * FROM transactions ORDER BY txid DESC"
                          df2 = pd.read_sql(qry4, conn)
                          txid = df2.at[0, 'txid']
                          qry2 = f"INSERT INTO [dbo].[log](txid,tid, cid, time, action) VALUES ({txid},{self.tid},{self.cid},'{self.txdate}','{action}')"
                          cursor.execute(qry2)
                          conn.commit()
                          cursor.close()
                          conn.close()
                          return "success"

                    else:
                        return "No sufficient Bitcoins to sell"
                
            

        except Exception as e:
            return f"an Error Occured {e}"

    def rejecttrade(self):
        conn = cg.connect_to_azure()
        action = 'Rejected'
        try:
            cursor = conn.cursor()
            qry = f"UPDATE transactions SET txstatus = 2, tid = {self.tid} WHERE txid={self.txid}"
            cursor.execute(qry)
            qry2 = f"SELECT TOP 1 * FROM cancellations ORDER BY txid DESC"
            df2 = pd.read_sql(qry2, conn)
            canid = df2.at[0, 'canid']
            print('df2:', df2, '\n', 'caind', canid)
            qry2 = f"INSERT INTO [dbo].[cancellations](txid) VALUES ({self.txid})"
            cursor.execute(qry2)
            qry4 = f"INSERT INTO [dbo].[log](txid,tid, cid, time, action) VALUES ({self.txid},{self.tid},{self.cid},'{self.txdate}','{action}')"
            cursor.execute(qry4)
            conn.commit()
            cursor.close()
            conn.close()
            return "success"

        except Exception as e:
            return f"an Error Occured {e}"