from flask import Flask, request, jsonify
from flask_cors import CORS
import Login
import CreateUser
import ClientBuy
import Manager
import pandas as pd
import Transaction
import config as cg
from apscheduler.schedulers.background import BackgroundScheduler
import Client
import Cancellations
import Trader
import DependentTrade
# import zoneinfo
# from tzlocal import get_localzone
# tz = get_localzone()

oManager = Manager.Manager()

scheduler = BackgroundScheduler({'apscheduler.timezone': 'America/Jamaica'})
scheduler.add_job(oManager.updateClientStatus, 'interval', hours=730)
scheduler.start()
# initialize flask API
app = Flask(__name__)
api = CORS(app)


######LOGIN APIs#######

@app.route("/login", methods=['POST', 'GET'])
def login():
    data = request.get_json(force=True)
    username = data['username']
    pass_hash = data['pass_hash']
    oLogin = Login.Login(username, pass_hash)
    chk_type = oLogin.check_type()
    getc_details = oLogin.get_client_data()
    return getc_details


######TRADER APIS######

@app.route("/trader/search", methods=['GET', 'POST'])
def transactionSearch():
    data = request.get_json(force=True)
    key = data['key']
    type = data['type']
    oTrader = Trader.Trader(key=key, type=type)
    matchedData = oTrader.searchKey()
    return matchedData


@app.route("/trader/gettransactions", methods=['GET', 'POST'])
def transactionGet():
    oTrader = Trader.Trader()
    listData = oTrader.listTransactions()
    return listData


@app.route("/trader/getPendingTransactions", methods=['POST', 'GET'])
def pendingTransaction():
    oTrader = Trader.Trader()
    txns = oTrader.pendingTransactions()
    return txns


#######MANAGER APIS#########

@app.route("/manager/gettypedata", methods=['POST', 'GET'])
def managerData():
    data = request.get_json(force=True)
    type = data['type']
    oManager = Manager.Manager(type=type)
    TransData = oManager.retrieve_data()
    return TransData


@app.route("/manager/daily", methods=['POST', 'GET'])
def managerDaily():
    data = request.get_json(force=True)
    # type = data['type']
    # id = data['id']
    start_date = data['start_date']
    end_date = data['end_date']
    oManager = Manager.Manager(start_date, end_date)
    aggregateData = oManager.retrieve_transaction_range_day()
    return aggregateData


@app.route("/manager/weekly", methods=['POST', 'GET'])
def managerWeekly():
    data = request.get_json(force=True)
    # type = data['type']
    # id = data['id']
    start_date = data['start_date']
    end_date = data['end_date']
    oManager = Manager.Manager(start_date, end_date)
    aggregateData = oManager.retrieve_transaction_range_week()
    return aggregateData


@app.route("/manager/monthly", methods=['POST', 'GET'])
def managerMonthly():
    data = request.get_json(force=True)
    # type = data['type']
    # id = data['id']
    start_date = data['start_date']
    end_date = data['end_date']
    oManager = Manager.Manager(start_date, end_date)
    aggregateData = oManager.retrieve_transaction_range_month()
    return aggregateData

####CLIENT APIS######


@app.route("/client/transactions", methods=['POST', 'GET'])
def client_getTransactions():
    data = request.get_json(force=True)
    cid = data['cid']
    client = Client.Client(cid)
    transactions = client.get_transactions()
    return transactions


@app.route("/client/independentTrade", methods=['POST', 'GET'])
def client_place_buyOrders():
    data = request.get_json(force=True)
    txamount = data['txamount']
    txtype = data['txtype']
    txstatus = 1  # approved since indepenedent order
    cid = data['cid']
    txdate = data['txdate']
    currBTC = data['currBTC']
    print(data)
    txn = ClientBuy.ClientBuy(cid, txdate, txtype, txstatus, txamount, currBTC)
    return txn.BuyBTC()


@app.route("/client/dependentTrade", methods=['POST', 'GET'])
def client_place_traderTrade():
    data = request.get_json(force=True)
    txamount = data['txamount']
    txtype = data['txtype']
    txstatus = 0  # approved since indepenedent order
    cid = data['cid']
    commtype = data['commtype']
    txdate = data['txdate']
    currBTC = data['currBTC']
    print(data)
    # txn = ClientBuy.ClientBuy(cid, txdate, txtype, txstatus, txamount, currBTC)
    txn = DependentTrade.DependentTrade(
        cid, txdate, txtype, txstatus, txamount, currBTC, commtype)
    place_trade = txn.place_order()
    return place_trade

######TRANSACTION APIS#######


@app.route("/transactions/approveTrade", methods=['POST', 'GET'])
def ApproveTrade():
    # will only APPROVE either BUY or SELL trade (not topup/recharge)
    data = request.get_json(force=True)
    print(data)
    txid = data['txid']
    currBTC = data['currBTC']
    txtype = data['txtype']
    tid = data['tid']
    commtype = data['commtype']
    if commtype == '0':
        commtype = 'BTC'
    elif commtype == '1':
        commtype = 'USD'
    cid = data['cid']
    txdate = data['txdate']
    txamount = data['txamount']
    txstatus = 1
    approve_trade = DependentTrade.DependentTrade(
        cid, txdate, txtype, txstatus, txamount, currBTC, commtype, txid=txid, tid=tid)
    return approve_trade.approvetrade()


@app.route("/transactions/rejectTrade", methods=['POST', 'GET'])
def RejectTrade():
    # will only REJECT either BUY or SELL trade (not topup/recharge)
    data = request.get_json(force=True)
    txid = data['txid']
    txtype = data['txtype']
    txamount = data['txamount']
    txstatus = 0
    cid = data['cid']
    txdate = data['txdate']
    tid = data['tid']
    reject_trade = DependentTrade.DependentTrade(
        cid, txdate, txtype, txstatus, txamount, txid=txid, tid=tid)
    print("REJECT", reject_trade.rejecttrade())
    return reject_trade.rejecttrade()


@app.route("/transactions/topup", methods=['POST', 'GET'])
def placeTopUpRequest():
    data = request.get_json(force=True)
    fiatamount = data['fiatamount']
    txtype = data['txtype']
    txstatus = 0  # pending, when the first time order is placed
    cid = data['cid']
    txdate = data['txdate']
    txn = Transaction.Transaction(
        cid, txdate, txtype, txstatus, fiatamount=fiatamount)
    return txn.placeRechargeRequest()


@app.route("/transactions/approveTopup", methods=['POST', 'GET'])
def ApproveTopUp():
    data = request.get_json(force=True)
    txid = data['txid']
    txtype = None
    fiatamount = data['fiatamount']
    txstatus = 1
    cid = data['cid']
    txdate = data['txdate']
    tid = data['tid']
    txn = Transaction.Transaction(
        cid, txdate, txtype, txstatus, fiatamount=fiatamount, tid=tid, txid=txid)
    return txn.approvetopup()


@app.route("/transactions/rejecttopup", methods=['POST', 'GET'])
def RejectTopUp():
    data = request.get_json(force=True)
    txid = data['txid']
    txtype = None
    txstatus = 2
    cid = data['cid']
    txdate = data['txdate']
    tid = data['tid']
    txn = Transaction.Transaction(
        cid, txdate, txtype, txstatus, tid=tid, txid=txid)
    return txn.rejecttopup()


#!/usr/bin/env python3
########ADD USER APIS#######
# /newuser/0 - client /newuser/1 - trader .../2-manager


@app.route("/newuser/<id>", methods=['GET'])
def createUser(id):
    data = request.get_json(force=True)
    first_name = data['first_name']
    last_name = data['last_name']
    age = data['age']
    ssn = data['ssn']
    email = data['email']
    username = data['username']
    password = data['password']
    ph_no = data['ph_no']
    type = data['type']
    clientstreet = data['clientstreet']
    clientzip = data['clientzip']
    clientstate = data['clientstate']
    clientcountry = data['clientcountry']
    oCreateUser = CreateUser.CreateUser(first_name, last_name, age, ssn, email, username,
                                        password, ph_no, type, clientstreet, clientzip, clientstate, clientcountry)
    if id == "0":
        oCreateUser.createClient()
    elif id == "1":
        oCreateUser.createTrader()
    elif id == "2":
        oCreateUser.createManager()
    else:
        return "incorrect id"
    return "success"


if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int("4000")
    )
