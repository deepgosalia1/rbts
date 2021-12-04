# if he is buys:
#     if he his btc comm: 
#         amount_to_check_BTC = 0.005*txamount
#         amount_to_check_fiat = txamount * btcprice 
#         if btc_wallet >= amount_to_check_BTC and fiat_wallet >= amount_to_check_fiat:
#            btc_wallet = btc_wallet + txamount
#            fiat_wallet = fiat_wallet - amount_to_check_fiat
#         else: error
#     else: usd comm:
#         amount_to_check = txamount * btcprice + (0.008 * txamount * btcprice)
#         if fiat_wallet >= amount_to_check:
#             btc_wallet = btc_wallet + txamount
#             fiat_wallet = fiat_wallet - amount_to_check
#         else: error
# else:
#     if he his btc comm: 
#         amount_to_check_BTC = 0.005*txamount + txamount
#         if btc_wallet >= amount_to_check_BTC:
#            btc_wallet = btc_wallet - amount_to_check_BTC
#            fiat_wallet = fiat_wallet + amount_to_check_BTC * btcprice
#         else: error
#     else: usd comm:
#         amount_to_check_BTC = txamount
#         amount_to_check_fiat = 0.005 * txamount * btcprice 
#         if btc_wallet>=amount_to_check_BTC and fiat_wallet >= amount_to_check_fiat:
#             btc_wallet = btc_wallet - amount_to_check_BTC
#             fiat_wallet = fiat_wallet + (txamount * btcprice) - amount_to_check_fiat
#         else: error

import pandas as pd
from flask import jsonify
from pandas.core import indexing
from pandas.core.dtypes.missing import notnull
import config as cg
from pandas.io import json


class DependentTrade:

    global id

    def __init__(self, cid, txdate, txtype, txstatus, txamount, currBTC, commtype, txid=None):
        self.cid = cid
        self.txdate = txdate
        self.txtype = txtype
        self.txstatus = txstatus
        self.txamount = txamount
        self.currBTC = currBTC
        self.txid = txid
        self.commtype = commtype

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
            amount = self.txamount * self.currBTC
            comm_amount = 0
            # for sell, 
            if (client_status == 0): #  gold
                if (self.commtype == 'BTC'):
                    comm_amount = 0.003 * self.txamount # 0.003 * currBTC price
                    self.txamount += comm_amount
                if (self.commtype == 'USD'):
                    comm_amount = 0.005 * amount # 0.005 * amount
                    amount += comm_amount
            if (client_status == 1):
                if(self.commtype == 'BTC'): # 0.007 * currBTC price
                    comm_amount = 0.005 * self.txamount
                    self.txamount += comm_amount
                if(self.commtype == 'USD'): # 0.01 * amount
                    comm_amount = 0.008 * amount
            # amount += comm_amount
            # for buy if amount < fiat_wallet: # do things
            # else: err
            # for sellcheck comm_am < fiatWall #do things else err
            if (self.txtype == 0):
                if (fiat_wallet > amount):
                    fiat_wallet = fiat_wallet - amount
                    btc_wallet = btc_wallet + self.txamount

                    qry3 = f"UPDATE [dbo].[client] SET btcwallet={btc_wallet},fiatwallet={fiat_wallet} WHERE cid = {self.cid}"
                    cursor.execute(qry3)
                    qry1 = f"UPDATE transactions SET txstatus = 1 WHERE txid={self.txid}"
                    cursor.execute(qry1)
                    qry4 = f"SELECT TOP 1 * FROM transactions ORDER BY txid DESC"
                    df2 = pd.read_sql(qry4, conn)
                    txid = df2.at[0, 'txid']
                    qry2 = f"INSERT INTO [dbo].[log](txid, cid, time, action,commtype,commamount) VALUES ({txid},{self.cid},'{self.txdate}','{action}','{self.commtype}',{comm_amount})"
                    cursor.execute(qry2)
                    conn.commit()
                    cursor.close()
                    conn.close()
                    return "success"
                else:
                    return "No sufficient Bitcoins to buy"
            if (self.txtype == 1):
                if (btc_wallet > self.txamount):
                    btc_wallet = btc_wallet - {self.txamount}
                    fiat_wallet = fiat_wallet + amount
                    qry3 = f"UPDATE [dbo].[client] SET btcwallet={btc_wallet},fiatwallet={fiat_wallet} WHERE cid = {self.cid}"
                    cursor.execute(qry3)
                    qry1 = f"UPDATE transactions SET txstatus = 1 WHERE txid={self.txid}"
                    cursor.execute(qry1)
                    qry4 = f"SELECT TOP 1 * FROM transactions ORDER BY txid DESC"
                    df2 = pd.read_sql(qry4, conn)
                    txid = df2.at[0, 'txid']
                    qry2 = f"INSERT INTO [dbo].[log](txid, cid, time, action,commtype,commamount) VALUES ({txid},{self.cid},'{self.txdate}','{action}','{self.commtype}',{comm_amount})"
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
            qry1 = f"UPDATE transactions SET txstatus = 2 WHERE txid={self.txid}"
            cursor.execute(qry1)
            qry3 = f"INSERT INTO [dbo].[cancellations](txid) VALUES({self.txid})"
            cursor.execute(qry3)
            qry2 = f"SELECT TOP 1 * FROM cancellations ORDER BY txid DESC"
            df2 = pd.read_sql(qry2, conn)
            canid = df2.at[0, 'canid']
            print('df2:', df2, '\n', 'caind', canid)
            qry2 = f"INSERT INTO [dbo].[cancellations](canid,txid) VALUES ({int(canid)},{self.txid})"
            cursor.execute(qry2)
            qry4 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({self.txid},{self.cid},'{self.txdate}','{action}')"
            cursor.execute(qry4)
            conn.commit()
            cursor.close()
            conn.close()
            return "success"

        except Exception as e:
            return f"an Error Occured {e}"
