from flask import Flask,request,jsonify
#from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS
import Login
import json

#initialize flask API
app = Flask(__name__)
api = CORS(app)

@app.route("/login",methods=['POST', 'GET'])
def login():
    # print('req',json.load(request.args))
    uid = request.args.get('uid')
    # or use request.form to get body
    username = request.args.get('username')
    pass_hash = request.args.get('pass_hash')
    oLogin = Login.Login(uid,username,pass_hash)
    #Return validation creds from API
    return oLogin.check_type()

@app.route("/trade")
def transaction():
    # txid = request.args.get('txid') or use request.form to get body
    # done_by = request.args.get('done_by')
    # comm_type = request.args.get('comm_type')
    # comm_paid = request.args.get('comm_paid') or use request.form to get body
    # amount = request.args.get('amount')
    # belongs_to= request.args.get('belongs_to')

    return

@app.route("/manager")
def manager():
    # mid = request.args.get('mid') or use request.form to get body
    return





if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int("4000")
    )


