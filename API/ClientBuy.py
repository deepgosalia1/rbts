import config as cg
import pandas as pd


class ClientBuy:

    global id

    def __init__(self, cid, txdate, txtype, txstatus, txamount, currBTC):
        self.cid = cid
        self.txdate = txdate
        self.txtype = txtype
        self.txstatus = txstatus
        self.txamount = txamount
        self.btc_amount = 0.1
        self.currBTC = currBTC
        self.txid = None

    def BuyBTC(self):
        conn = cg.connect_to_azure()
        try:
            cursor = conn.cursor()
            qry2 = f"SELECT btcwallet,fiatwallet FROM [dbo].[client] WHERE cid = {self.cid}"
            c = pd.read_sql(qry2, conn)
            # btc_wallet
            btc_wallet = c['btcwallet'][0]
            print("btc", btc_wallet)
            # fiat wallet
            fiat_wallet = c['fiatwallet'][0]
            print("fiat", fiat_wallet)
            amount = self.txamount * self.currBTC
            if (self.txtype == 0):

                if (fiat_wallet > amount):
                    fiat_wallet = fiat_wallet - amount
                    btc_wallet = btc_wallet + self.txamount
                    qry3 = f"UPDATE [dbo].[client] SET btcwallet={btc_wallet},fiatwallet={fiat_wallet} WHERE cid = {self.cid}"
                    cursor.execute(qry3)
                    print('tetinggg')
                    qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, txamount) VALUES ({self.cid},'{self.txdate}',{self.txtype},{self.txstatus},{self.txamount})"
                    cursor.execute(qry1)
                    qry2 = f"SELECT TOP 1 * FROM transactions ORDER BY txid DESC"
                    df2 = pd.read_sql(qry2, conn)
                    txid = df2.at[0, 'txid']
                    qry2 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({txid},{self.cid},'{self.txdate}','1')"
                    cursor.execute(qry2)
                    print('qry2', qry1)
                    conn.commit()
                    cursor.close()
                    conn.close()
                    return "success"
                else:
                    return "No sufficient Balance to execute buy request"
            if (self.txtype == 1):
                if (btc_wallet > self.txamount):
                    btc_wallet = btc_wallet - self.txamount
                    fiat_wallet = fiat_wallet + amount
                    qry3 = f"UPDATE [dbo].[client] SET btcwallet={btc_wallet},fiatwallet={fiat_wallet} WHERE cid = {self.cid}"
                    cursor.execute(qry3)
                    qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, txamount) VALUES ({self.cid},'{self.txdate}',{self.txtype},{self.txstatus},{self.txamount})"
                    cursor.execute(qry1)
                    qry2 = f"SELECT TOP 1 * FROM transactions ORDER BY txid DESC"
                    df2 = pd.read_sql(qry2, conn)
                    txid = df2.at[0, 'txid']
                    qry2 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({txid},{self.cid},'{self.txdate}','1')"
                    cursor.execute(qry2)
                    conn.commit()
                    cursor.close()
                    conn.close()
                    return "success"
                else:
                    return "No sufficient Bitcoins to sell"
        except Exception as e:
            return f"an Error Occured {e}"
