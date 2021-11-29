import config as cg
import pandas as pd
class ClientBuy:

    global id
    # date = GETDATE()

    # // for clients only
    # //Transaction REQUEST from client to buy 50 BTC
    # //insert into transactions (cid, txdate, txtype, txstatus, txamount) values (1, date, 0,0, 50);
    # //insert into logs (cid, txid, time) values (1, txid, date);

    def __init__(self, cid, txdate, txtype, txstatus, txamount, txid=None):
        self.cid = cid
        self.txdate = txdate
        self.txtype = txtype
        self.txstatus = txstatus
        self.txamount = txamount
        self.txid = txid

    def BuyBTC(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry2 = f"SELECT btcwallet,fiatwallet FROM [dbo].[client] WHERE cid = {self.cid}"
            c = pd.read_sql(qry2,conn)
            #btc_wallet
            btc_wallet = c['btcwallet'][0]
            print("btc",btc_wallet)
            #fiat wallet
            fiat_wallet = c['fiatwallet'][0]
            print("fiat",fiat_wallet)
            btc_amount = 20 #We need to get it dynamically from the coin desk api.
            amount = self.txamount * btc_amount
            if ( self.txstatus == 0 ) :
                if ( fiat_wallet > amount ) :
                        fiat_wallet = fiat_wallet - amount
                        btc_wallet = btc_wallet + amount
                        qry3 = f"UPDATE [dbo].[client] SET btcwallet=btc_wallet,fiatwallet=fiat_wallet WHERE cid = {self.cid}"
                        qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, txamount) VALUES ({self.cid},'{self.txdate}','{self.txtype}','{self.txstatus}','{self.txamount}')"
                        qry4 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({self.txid},{self.cid},'{self.txdate}','1')"
                        cursor.execute(qry3)
                        cursor.execute(qry1)
                        cursor.execute(qry4)
                        conn.commit()
                        cursor.close()
                        conn.close()
                        return "success"
                else :
                        return "No sufficient Balance to execute buy request"
            if ( self.txstatus == 1):
                if ( btc_wallet > self.txamount) :
                        btc_wallet = btc_wallet - self.txamount
                        fiat_wallet = fiat_wallet + amount
                        qry3 = f"UPDATE [dbo].[client] SET btcwallet=btc_wallet,fiatwallet=fiat_wallet WHERE cid = {self.cid}"
                        qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, txamount) VALUES ({self.cid},'{self.txdate}','{self.txtype}','{self.txstatus}','{self.txamount}')"
                        qry4 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({self.txid},{self.cid},'{self.txdate}','1')"
                        cursor.execute(qry3)
                        cursor.execute(qry1)
                        cursor.execute(qry4)
                        conn.commit()
                        cursor.close()
                        conn.close()
                        return "success"
                else:
                        return "No sufficient Bitcoins to sell"
        except Exception as e:
            return f"an Error Occured {e}"