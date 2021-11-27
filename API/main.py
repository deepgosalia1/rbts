from flask import Flask, request, jsonify
from flask_cors import CORS
import Login
import json
import CreateUser
import Manager
import Transaction
import Client
import Cancellations
import Trader

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

@app.route("/trader/search",methods=['GET','POST'])
def transactionSearch():
    data = request.get_json(force=True)
    key = data['key']
    oTrader = Trader.Trader(key)
    matchedData = oTrader.searchKey()
    return matchedData


#######MANAGER APIS#########

@app.route("/manager/", methods=['POST', 'GET'])
def managerData():
    data = request.get_json(force=True)
    type = data['type']
    id = data['id']
    start_date = data['start_date']
    end_date = data['end_date']
    oManager = Manager.Manager(type, id, start_date, end_date)
    TransData = oManager.retrieve_data()
    return TransData


@app.route("/manager/daily", methods=['POST', 'GET'])
def managerDaily():
    data = request.get_json(force=True)
    type = data['type']
    id = data['id']
    start_date = data['start_date']
    end_date = data['end_date']
    oManager = Manager.Manager(type, id, start_date, end_date)
    aggregateData = oManager.retrieve_transaction_range_day()
    return aggregateData


@app.route("/manager/weekly", methods=['POST', 'GET'])
def managerWeekly():
    data = request.get_json(force=True)
    type = data['type']
    id = data['id']
    start_date = data['start_date']
    end_date = data['end_date']
    oManager = Manager.Manager(type, id, start_date, end_date)
    aggregateData = oManager.retrieve_transaction_range_week()
    return aggregateData


@app.route("/manager/monthly", methods=['POST', 'GET'])
def managerMonthly():
    data = request.get_json(force=True)
    type = data['type']
    id = data['id']
    start_date = data['start_date']
    end_date = data['end_date']
    oManager = Manager.Manager(type, id, start_date, end_date)
    aggregateData = oManager.retrieve_transaction_range_month()
    return aggregateData


@app.route("/client/placetrade", methods=['POST', 'GET'])
def client_place_buyOrder():
    data = request.get_json(force=True)
    print(data)
    txamount = data['txamount']
    txtype = data['txtype']
    txstatus = 0  # pending, when the first time order is placed
    cid = data['cid']
    commtype = data['commtype']
    txdate = data['txdate']
    txn = Transaction.Transaction(
        cid, txdate, txtype, txstatus, commtype=commtype, txamount=txamount)
    return txn.BuyBTC()


@app.route("/client/transactions", methods=['POST', 'GET'])
def client_getTransactions():
    data = request.get_json(force=True)
    cid = data['cid']
    client = Client.Client(cid)
    transactions = client.get_transactions()
    return transactions


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


@app.route("/transactions/approvetopup", methods=['POST', 'GET'])
def ApproveTopUp():
    data = request.get_json(force=True)
    txid = data['txid']
    fiatamount = data['fiatamount']
    txstatus = 1
    cid = data['cid']
    txdate = data['txdate']
    txn = Transaction.Transaction(
        cid, txdate, txstatus, fiatamount=fiatamount, txid=txid)
    return txn.approvetopup()

@app.route("/transactions/rejecttopup", methods=['POST', 'GET'])
def RejectTopUp():
    data = request.get_json(force=True)
    txid = data['txid']
    txstatus = 2
    cid = data['cid']
    txdate = data['txdate']
    txn = Transaction.Transaction(
        cid, txdate, txstatus, txid=txid)
    return txn.rejecttopup()
########ADD USER APIS#######
#/newuser/0 - client /newuser/1 - trader .../2-manager
@app.route("/newuser/<id>",methods=['GET'])
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
    type=data['type']
    clientstreet = data['clientstreet']
    clientzip = data['clientzip']
    clientstate = data['clientstate']
    clientcountry = data['clientcountry']
    oCreateUser = CreateUser.CreateUser(first_name,last_name,age,ssn,email,username,password,ph_no,type,clientstreet,clientzip,clientstate,clientcountry)
    if id == "0":
        oCreateUser.createClient()
    elif id=="1":
        oCreateUser.createTrader()
    elif id=="2":
        oCreateUser.createManager()
    else:
        return "incorrect id"
    return "success"
        


# @app.route("/newuser/trader",method = ['GET'])
# def createTraderUser():
#     data = request.get_json(force=True)
#     name = data['name']
#     username = data['username']
#     password = data['password']

#     #oCreateTraderUser = CreateUser.CreateUser(name,username,password)

if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int("4000")
    )
