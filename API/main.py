from flask import Flask,request,jsonify
from flask_cors import CORS
import Login
import json
import CreateUser
import Manager

#initialize flask API
app = Flask(__name__)
api = CORS(app)


######LOGIN APIs#######

@app.route("/login",methods=['POST', 'GET'])
def login():
    data = request.get_json(force=True)
    username = data['username']
    pass_hash = data['pass_hash']
    oLogin = Login.Login(username,pass_hash)
    chk_type = oLogin.check_type()
    getc_details = oLogin.get_client_data()
    return getc_details



######TRADER APIS######

# @app.route("/trade")
# def transaction():
#     # txid = request.args.get('txid') or use request.form to get body
#     # done_by = request.args.get('done_by')
#     # comm_type = request.args.get('comm_type')
#     # comm_paid = request.args.get('comm_paid') or use request.form to get body
#     # amount = request.args.get('amount')
#     # belongs_to= request.args.get('belongs_to')

#     return


#######MANAGER APIS#########

@app.route("/manager/",methods=['POST','GET'])
def managerData():
    data = request.get_json(force=True)
    type = data['type']
    id = data['id']
    start_date = data['start_date']
    end_date = data['end_date']
    oManager = Manager.Manager(type,id,start_date,end_date)
    TransData = oManager.retrieve_data()
    return TransData

@app.route("/manager/daily",methods=['POST','GET'])
def managerDaily():
    data = request.get_json(force=True)
    type = data['type']
    id = data['id']
    start_date = data['start_date']
    end_date = data['end_date']
    oManager = Manager.Manager(type,id,start_date,end_date)
    aggregateData = oManager.retrieve_transaction_range_day()
    return aggregateData

@app.route("/manager/weekly",methods=['POST','GET'])
def managerWeekly():
    data = request.get_json(force=True)
    type = data['type']
    id = data['id']
    start_date = data['start_date']
    end_date = data['end_date']
    oManager = Manager.Manager(type,id,start_date,end_date)
    aggregateData = oManager.retrieve_transaction_range_week()
    return aggregateData

@app.route("/manager/monthly",methods=['POST','GET'])
def managerMonthly():
    data = request.get_json(force=True)
    type = data['type']
    id = data['id']
    start_date = data['start_date']
    end_date = data['end_date']
    oManager = Manager.Manager(type,id,start_date,end_date)
    aggregateData = oManager.retrieve_transaction_range_month()
    return aggregateData
    


########ADD USER APIS#######

# @app.route("/newuser/cient",method=['GET'])
# def createClientUser():
#     data = request.get_json(force=True)
#     first_name = data['first_name']
#     last_name = data['last_name']
#     age = data['age']
#     ssn = data['ssn']
#     email = data['email']
#     username = data['username']
#     password = data['password']
#     ph_no = data['ph_no']

#     #oCreateTraderUser = CreateUser.CreateUser(first_name,last_name,age,ssn,email,username,password,ph_no)


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


