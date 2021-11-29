class ClientBuy:

    global id
    # date = GETDATE()

    # // for clients only
    # //Transaction REQUEST from client to buy 50 BTC
    # //insert into transactions (cid, txdate, txtype, txstatus, txamount) values (1, date, 0,0, 50);
    # //insert into logs (cid, txid, time) values (1, txid, date);

    def _init_(self, cid, txdate, txtype, txstatus, txamount=None, fiatamount=None, btcamount=None, commamount=None, tid=None, commtype=None, txid=None):
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
            c = cursor.execute(qry2)
            #btc_wallet
            btc_wallet = c.fetchall()[0][0]
            #fiat wallet
            fiat_wallet = c.fetchall()[0][1]
            btc_amount = 20 #We need to get it dynamically from the coin desk api.
            amount = {self.txamount} * btc_amount
            if ( {self.txstatus} == 0 ) :
                if ( fiat_wallet > amount ) :
                        fiat_wallet = fiat_wallet - amount
                        btc_wallet = btc_wallet + amount
                        qry3 = f"UPDATE [dbo].[client] SET btcwallet=btc_wallet,fiatwallet=fiat_wallet WHERE cid = {self.cid}"
                        qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, txamount) VALUES ({self.cid},'{self.txdate}','{self.txtype}','{self.txstatus}','{self.txamount}')"
                        qry4 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({txid},{self.cid},'{self.txdate}','1')"
                        cursor.execute(qry3)
                        cursor.execute(qry1)
                        cursor.execute(qry4)
                        return "success"
                else :
                        return "No sufficient Balance to execute buy request"
            if ( {self.txstatus} == 1):
                if ( btc_wallet > {self.txamount}) :
                        btc_wallet = btc_wallet - {self.txamount}
                        fiat_wallet = fiat_wallet + amount
                        qry3 = f"UPDATE [dbo].[client] SET btcwallet=btc_wallet,fiatwallet=fiat_wallet WHERE cid = {self.cid}"
                        qry1 = f"INSERT INTO [dbo].[transactions](cid, txdate, txtype, txstatus, txamount) VALUES ({self.cid},'{self.txdate}','{self.txtype}','{self.txstatus}','{self.txamount}')"
                        qry4 = f"INSERT INTO [dbo].[log](txid, cid, time, action) VALUES ({txid},{self.cid},'{self.txdate}','1')"
                        cursor.execute(qry3)
                        cursor.execute(qry1)
                        cursor.execute(qry4)
                        return "success"
                else:
                        return "No sufficient Bitcoins to sell"
                cursor.commit()
                cursor.close()
        except Exception as e:
            return f"an Error Occured {e}"