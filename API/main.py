from flask import Flask, request, jsonify
from flask_cors import CORS
import Login
import json
import CreateUser
import ClientBuy
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

@app.route("/trader/search", methods=['GET', 'POST'])
def transactionSearch():
    data = request.get_json(force=True)
    key = data['key']
    oTrader = Trader.Trader(key)
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
    # cid, txamount, txtype, commtype, txdate, currBTC
    txamount = data['txamount']
    txtype = data['txtype']
    txstatus = 0  # approved since indepenedent order
    cid = data['cid']
    commtype = data['commtype']
    txdate = data['txdate']
    currBTC = data['currBTC']
    print(data)
    # txn = ClientBuy.ClientBuy(cid, txdate, txtype, txstatus, txamount, currBTC)
    return ""

######TRANSACTION APIS#######


@app.route("/transactions/approveTrade", methods=['POST', 'GET'])
def ApproveTrade():
    # will only APPROVE either BUY or SELL trade (not topup/recharge)
    data = request.get_json(force=True)
    txid = data['txid']
    currBTC = data['currBTC']
    # pending api
    return ''


@app.route("/transactions/rejectTrade", methods=['POST', 'GET'])
def RejectTrade():
    # will only REJECT either BUY or SELL trade (not topup/recharge)
    data = request.get_json(force=True)
    txid = data['txid']
    # pending api
    return ''


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
    txtype = data['txtype']
    fiatamount = data['fiatamount']
    txstatus = 1
    cid = data['cid']
    txdate = data['txdate']
    txn = Transaction.Transaction(
        cid, txdate, txtype, txstatus, fiatamount=fiatamount, txid=txid)
    return txn.approvetopup()


@app.route("/transactions/rejecttopup", methods=['POST', 'GET'])
def RejectTopUp():
    data = request.get_json(force=True)
    txid = data['txid']
    txtype = data['txtype']
    txstatus = 2
    cid = data['cid']
    txdate = data['txdate']
    fiatamount = data['fiatamount']
    txn = Transaction.Transaction(
        cid, txdate, txtype, txstatus, fiatamount=fiatamount, txid=txid)
    return txn.rejecttopup()


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
