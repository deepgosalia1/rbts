from flask import Flask,request,jsonify
#from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS
import Login
import json
import CreateUser
import Manager

#initialize flask API
app = Flask(__name__)
api = CORS(app)

@app.route("/login",methods=['POST', 'GET'])
def login():
    # print('req',json.load(request.args))
    data = request.get_json(force=True)
    # or use request.form to get body
    username = data['username']
    pass_hash = data['pass_hash']
    oLogin = Login.Login(username,pass_hash)
    #Return validation creds from API
    return oLogin.check_type()

# @app.route("/trade")
# def transaction():
#     # txid = request.args.get('txid') or use request.form to get body
#     # done_by = request.args.get('done_by')
#     # comm_type = request.args.get('comm_type')
#     # comm_paid = request.args.get('comm_paid') or use request.form to get body
#     # amount = request.args.get('amount')
#     # belongs_to= request.args.get('belongs_to')

#     return

# @app.route("/manager",method=['POST','GET'])
# def manager():
#     # mid = request.args.get('mid') or use request.form to get body
#     data = request.get_json(force=True)
#     type = data['type']
#     #oManager = Manager.Manager(type)


#     return

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


