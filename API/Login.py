import pandas as pd
from pandas.io import json
import config as cg
from flask import jsonify

class Login:
    
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def check_type(self):
        conn = cg.connect_to_azure()
        cursor = conn.cursor()
        chk = f"SELECT * FROM users WHERE username='{self.username}' and pass_hash='{self.password}'"
        self.df1 = pd.read_sql(chk,conn)
        self.id = int(self.df1['userid'][0])
        # user_type = cursor.fetchone()[0]
        # cursor.execute(chk)
        # user_type = cursor.fetchone()
        json_user_data = self.df1.to_json(orient = "index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)

    def get_client_data(self):
        conn = cg.connect_to_azure()
        qry = f"SELECT * FROM client WHERE cid={self.id}"
        self.df2 = pd.read_sql(qry,conn)
        df3 = self.df1.join(self.df2)
        # user_type = cursor.fetchone()[0]
        # cursor.execute(chk)
        # user_type = cursor.fetchone()
        json_user_data = df3.to_json(orient = "index")
        parsed_json = json.loads(json_user_data)
        return json.dumps(parsed_json)
    
    # def get_trader_data(self):
    #     conn = cg.connect_to_azure()
    #     qry = f"SELECT * FROM trader WHERE tid={self.id}"
    #     df = pd.read_sql(qry,conn)
    #     # user_type = cursor.fetchone()[0]
    #     # cursor.execute(chk)
    #     # user_type = cursor.fetchone()
    #     json_user_data = df.to_json(orient = "index")
    #     parsed_json = json.loads(json_user_data)
    #     return json.dumps(parsed_json)