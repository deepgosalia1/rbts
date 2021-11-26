#//Template with the queries sent by deep in teams! 

import pandas as pd
from pandas.io import json
import config as cg
from flask import jsonify

class Transaction: 

    global id
    date = GETDATE()

    # // for clients only
    # //Transaction REQUEST from client to buy 50 BTC
    # //insert into transactions (cid, txdate, txtype, txstatus, txamount) values (1, date, 0,0, 50);
    # //insert into logs (cid, txid, time) values (1, txid, date);

    def __init__(self,cid, txdate, txtype, txstatus, txamount,txid,time,fiatamount,txstate):
        self.cid = cid
        self.txdate = txdate
        self.txtype = txtype
        self.txstatus = txstatus
        self.txamount = txamount
        self.txid = txid
        self.time = time
        self.fiatamount = fiatamount
        self.txstate = txstate
        

    def BuyBTC(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, txamount) VALUES ({self.cid},'{self.txdate}','{self.txtype}','{self.txstatus}','{self.txamount}')"
            qry2 = f"INSERT INTO [dbo].[logs](cid, txid, time) VALUES ({self.cid},{self.txid},{self.time})"
            #user_type = cursor.fetchone()[0]
            cursor.execute(qry1)
            cursor.execute(qry2)
            cursor.close()
            self.id = self.id + 1
            # user_type = cursor.fetchone()
        except Exception as e:
            print(e)

    # //Transaction REQUEST from client to sell 50 BTC:
    # //insert into transactions (cid, txdate, txtype, txstatus, txamount) values (1, GETDATE(), 1,0, 50);
    # //insert into logs (cid, txid, time) values (1, txid, date);

    def SellBTC(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, txamount) VALUES ({self.cid},'{self.txdate}','{self.txtype}','{self.txstatus}','{self.txamount}')"
            qry2 = f"INSERT INTO [dbo].[logs](cid, txid, time) VALUES ({self.cid},{self.txid},{self.time})"
            #user_type = cursor.fetchone()[0]
            cursor.execute(qry1)
            cursor.execute(qry2)
            cursor.close()
            self.id = self.id + 1
            # user_type = cursor.fetchone()
        except Exception as e:
            print(e)
    

    # //Transaction REQUEST from client to top up 50 usd into wallet:
    # //insert into transactions (cid, txdate, txtype, txstatus, fiatamount) values (1, GETDATE(), 2,0, 50);
    # //insert into logs (cid, txid, time) values (1, txid, date);

    def UpdateWallet(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, fiatamount) VALUES ({self.cid},'{self.txdate}','{self.txtype}','{self.txstatus}','{self.fiatamount}')"
            qry2 = f"INSERT INTO [dbo].[logs](cid, txid, time) VALUES ({self.cid},{self.txid},{self.time})"
            #user_type = cursor.fetchone()[0]
            cursor.execute(qry1)
            cursor.execute(qry2)
            cursor.close()
            self.id = self.id + 1
            # user_type = cursor.fetchone()
        except Exception as e:
            print(e)
    
    # //Client Queries END

    # //For traders only
    # //Fetch pending transactions in queue:
    # //select * from transactions where txstatus = 0;

    def GetPendingTransactions(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry1 = f"SELECT * FROM transactions WHERE txstatus=0"
            #Notrequired can be deleted--qry2 = f"INSERT INTO [dbo].[logs](cid, txid, time) VALUES ({self.cid},{self.txid},{self.time})"
            #user_type = cursor.fetchone()[0]
            cursor.execute(qry1)
            #cursor.execute(qry2)
            cursor.close()
            self.id = self.id + 1
            # user_type = cursor.fetchone()
        except Exception as e:
            print(e)


    # //Update a transaction from pending state to APPROVED state
    # //UPDATE transactions SET txstate = 1 WHERE txid=1;
    # //insert into logs (txid, time) values (txid, date);

    def UpdatePendingToApprovedTransaction(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry1 = f"UPDATE transactions SET txstate = 1 WHERE txid='{self.txid}"
            qry2 = f"INSERT INTO [dbo].[logs](txid, time) VALUES ({self.txid},{self.time})"
            #user_type = cursor.fetchone()[0]
            cursor.execute(qry1)
            cursor.execute(qry2)
            cursor.close()
            self.id = self.id + 1
            # user_type = cursor.fetchone()
        except Exception as e:
            print(e)



    # //Update a transaction from pending state to REJECTED state
    # //UPDATE transactions SET txstate = 2 WHERE txid=1;
    # //insert into logs (txid, time) values (txid, date);


    def UpdatePendingToRejectedTransaction(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry1 = f"UPDATE transactions SET txstate = 2 WHERE txid='{self.txid}'"
            qry2 = f"INSERT INTO [dbo].[logs](txid, time) VALUES ({self.txid},{self.time})"
            #user_type = cursor.fetchone()[0]
            cursor.execute(qry1)
            cursor.execute(qry2)
            cursor.close()
            self.id = self.id + 1
            # user_type = cursor.fetchone()
        except Exception as e:
            print(e)

    # //Traders Queries END
       
