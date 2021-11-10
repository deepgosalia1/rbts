from flask import Flask,request
#from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS
import Login

#initialize flask API
app = Flask(__name__)
api = CORS(app)

@app.route("/login")
def login():
    # uid = request.args.get('uid')
    # username = request.args.get('username')
    # pass_hash = request.args.get('pass_hash')
    uid = 1
    username = "btcUser"
    pass_hash = "abc!242@4dsd"
    oLogin = Login.Login(uid,username,pass_hash)
    return oLogin.testOutput()

if __name__ == '__main__':
    app.run(debug=True)


