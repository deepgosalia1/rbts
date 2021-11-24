import pandas as pd
from pandas.io import json
import config as cg
from flask import jsonify

class Login:
    
    def __init__(self,username,password):
        # self.uid = uid
        self.username = username
        self.password = password

    def check_type(self):
        conn = cg.connect_to_azure()
        cursor = conn.cursor()
        chk = f"SELECT * FROM [dbo].[users] WHERE username='{self.username}' and pass_hash='{self.password}'"
        df = pd.read_sql(chk,conn)
        #user_type = cursor.fetchone()[0]
        # cursor.execute(chk)
        # user_type = cursor.fetchone()
        json_user_data = df.to_json(orient = "index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
    