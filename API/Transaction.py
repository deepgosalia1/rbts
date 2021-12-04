import pandas as pd
from flask import jsonify
from pandas.core import indexing
from pandas.core.dtypes.missing import notnull
import config as cg
from pandas.io import json


class Transaction:

    global id
    # date = GETDATE()

    # // for clients only
    # //Transaction REQUEST from client to buy 50 BTC
    # //insert into transactions (cid, txdate, txtype, txstatus, txamount) values (1, date, 0,0, 50);
    # //insert into logs (cid, txid, time) values (1, txid, date);

    def __init__(self, cid, txdate, txtype, txstatus, txamount=None, fiatamount=None, btcamount=None, commamount=None, tid=None, commtype=None, txid=None):
        self.cid = cid
        self.txdate = txdate
        self.txtype = txtype
        self.txstatus = txstatus
        self.txamount = txamount
        self.fiatamount = fiatamount
        self.fiatwallet = fiatamount
        self.btcamount = btcamount
        self.commamount = commamount
        self.commtype = commtype
        self.tid = tid
        self.txid = txid
        # self.txstate = txstate

    # when user places a buy transaction order for BTC
    def BuyBTC(self):
        conn = cg.connect_to_azure()
        action = ''
        action = 'Pending' if self.txstatus == 0 else 'Approved' if self.txstatus == 1 else 'Rejected'
        try:
            cursor = conn.cursor()
            qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, txamount) VALUES ({self.cid},'{self.txdate}',{self.txtype},{self.txstatus},{self.txamount})"
            c = cursor.execute(qry1)
            qry2 = f"SELECT TOP 1 * FROM transactions ORDER BY txid DESC"
            df2 = pd.read_sql(qry2, conn)
            txid = df2.at[0, 'txid']
            print('df2:', df2, '\n', c, 'txid', txid)
            qry2 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({txid},{self.cid},'{self.txdate}','{action}')"
            c = cursor.execute(qry2)
            conn.commit()
            cursor.close()
            conn.close()
            #user_type = cursor.fetchone()[0]
            # self.id = self.id + 1
            # print(df2.at[0, 'txid'] + 5, type(df2.at[0, 'txid']))
            # user_type = cursor.fetchone()
            return "success"
        except Exception as e:
            return f"an Error Occured {e}"

    def placeRechargeRequest(self):
        conn = cg.connect_to_azure()
        action = ''
        action = 'Pending'
        try:
            cursor = conn.cursor()
            qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, fiatamount) VALUES ({self.cid},'{self.txdate}',{self.txtype},{self.txstatus},{self.fiatamount})"
            cursor.execute(qry1)
            qry2 = f"SELECT TOP 1 * FROM transactions ORDER BY txid DESC"
            df2 = pd.read_sql(qry2, conn)
            txid = df2.at[0, 'txid']
            print('df2:', df2, '\n', 'txid', txid)
            qry2 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({int(txid)},{self.cid},'{self.txdate}','{action}')"
            cursor.execute(qry2)
            conn.commit()
            cursor.close()
            conn.close()
            #user_type = cursor.fetchone()[0]
            # self.id = self.id + 1
            # print(df2.at[0, 'txid'] + 5, type(df2.at[0, 'txid']))
            # user_type = cursor.fetchone()
            return "success"
        except Exception as e:
            print(e)
            return f"an Error Occured {e}"

    def approvetopup(self):
        conn = cg.connect_to_azure()
        action = 'Approved'
        try:
            cursor = conn.cursor()
            qry0 = f"UPDATE transactions SET txstatus = 1, tid = {self.tid} WHERE txid={self.txid}"
            cursor.execute(qry0)
            clientDataFetch = f"SELECT fiatwallet FROM client WHERE cid={self.cid}"
            df2 = pd.read_sql(clientDataFetch, conn)
            fiatamount = df2.at[0, 'fiatwallet']
            print('hhihihihihihihi')
            fiatamount = int(fiatamount) + self.fiatamount
            qry = f"UPDATE client SET fiatwallet = {fiatamount} WHERE cid={self.cid}"
            cursor.execute(qry)
            print('hhihihihihihihi222222')
            qry2 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({int(self.txid)},{self.cid},'{self.txdate}','{action}')"
            cursor.execute(qry2)
            print('hhihihihihihihi33333333')
            conn.commit()
            cursor.close()
            conn.close()
            # json_user_data = df.to_json(orient="index")
            # parsed_json = json.loads(json_user_data)
            return "success"
        except Exception as e:
            print(e)
            return f"an Error Occured {e}"

    def rejecttopup(self):
        conn = cg.connect_to_azure()
        action = 'Rejected'
        try:
            cursor = conn.cursor()
            qry = f"UPDATE transactions SET txstatus = 2, tid = {self.tid} WHERE txid={self.txid}"
            cursor.execute(qry)
            qry2 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({self.txid},{self.cid},'{self.txdate}','{action}')"
            cursor.execute(qry2)
            qry3 = f"INSERT INTO [dbo].[cancellations](txid) VALUES ({self.txid})"
            cursor.execute(qry3)
            conn.commit()
            cursor.close()
            conn.close()
            # json_user_data = df.to_json(orient="index")
            # parsed_json = json.loads(json_user_data)
            return "success"
        except Exception as e:
            return f"an Error Occured {e}"
# t = Transaction(1, '2020-05-15', 0, 0, 5)
# t.BuyBTC()
# //Transaction REQUEST from client to sell 50 BTC:
# //insert into transactions (cid, txdate, txtype, txstatus, txamount) values (1, GETDATE(), 1,0, 50);
# //insert into logs (cid, txid, time) values (1, txid, date);

# def SellBTC(self):
#     conn = cg.connect_to_azure()
#     try:
#         cursor = conn.cursor()
#         qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, txamount) VALUES ({self.cid},'{self.txdate}','{self.txtype}','{self.txstatus}','{self.txamount}')"
#         qry2 = f"INSERT INTO [dbo].[logs](cid, txid, time) VALUES ({self.cid},{self.txid},{self.time})"
#         #user_type = cursor.fetchone()[0]
#         cursor.execute(qry1)
#         cursor.execute(qry2)
#         cursor.close()
#         self.id = self.id + 1
#         # user_type = cursor.fetchone()
#     except Exception as e:
#         print(e)

# # //Transaction REQUEST from client to top up 50 usd into wallet:
# # //insert into transactions (cid, txdate, txtype, txstatus, fiatamount) values (1, GETDATE(), 2,0, 50);
# # //insert into logs (cid, txid, time) values (1, txid, date);

# def UpdateWallet(self):
#     conn = cg.connect_to_azure()
#     try:
#         cursor = conn.cursor()
#         qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, fiatamount) VALUES ({self.cid},'{self.txdate}','{self.txtype}','{self.txstatus}','{self.fiatamount}')"
#         qry2 = f"INSERT INTO [dbo].[logs](cid, txid, time) VALUES ({self.cid},{self.txid},{self.time})"
#         #user_type = cursor.fetchone()[0]
#         cursor.execute(qry1)
#         cursor.execute(qry2)
#         cursor.close()
#         self.id = self.id + 1
#         # user_type = cursor.fetchone()
#     except Exception as e:
#         print(e)

# # //Client Queries END

# # //For traders only
# # //Fetch pending transactions in queue:
# # //select * from transactions where txstatus = 0;

# def GetPendingTransactions(self):
#     conn = cg.connect_to_azure()
#     try:
#         cursor = conn.cursor()
#         qry1 = f"SELECT * FROM transactions WHERE txstatus=0"
#         # Notrequired can be deleted--qry2 = f"INSERT INTO [dbo].[logs](cid, txid, time) VALUES ({self.cid},{self.txid},{self.time})"
#         #user_type = cursor.fetchone()[0]
#         cursor.execute(qry1)
#         # cursor.execute(qry2)
#         cursor.close()
#         self.id = self.id + 1
#         # user_type = cursor.fetchone()
#     except Exception as e:
#         print(e)

# # //Update a transaction from pending state to APPROVED state
# # //UPDATE transactions SET txstate = 1 WHERE txid=1;
# # //insert into logs (txid, time) values (txid, date);

# def UpdatePendingToApprovedTransaction(self):
#     conn = cg.connect_to_azure()
#     try:
#         cursor = conn.cursor()
#         qry1 = f"UPDATE transactions SET txstate = 1 WHERE txid='{self.txid}"
#         qry2 = f"INSERT INTO [dbo].[logs](txid, time) VALUES ({self.txid},{self.time})"
#         #user_type = cursor.fetchone()[0]
#         cursor.execute(qry1)
#         cursor.execute(qry2)
#         cursor.close()
#         self.id = self.id + 1
#         # user_type = cursor.fetchone()
#     except Exception as e:
#         print(e)

# # //Update a transaction from pending state to REJECTED state
# # //UPDATE transactions SET txstate = 2 WHERE txid=1;
# # //insert into logs (txid, time) values (txid, date);

# def UpdatePendingToRejectedTransaction(self):
#     conn = cg.connect_to_azure()
#     try:
#         cursor = conn.cursor()
#         qry1 = f"UPDATE transactions SET txstate = 2 WHERE txid='{self.txid}'"
#         qry2 = f"INSERT INTO [dbo].[logs](txid, time) VALUES ({self.txid},{self.time})"
#         #user_type = cursor.fetchone()[0]
#         cursor.execute(qry1)
#         cursor.execute(qry2)
#         cursor.close()
#         self.id = self.id + 1
#         # user_type = cursor.fetchone()
#     except Exception as e:
#         print(e)

# //Traders Queries END
