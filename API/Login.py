import pandas
#import config as cg

class Login:
    
    def __init__(self,uid,username,password):
        self.uid = uid
        self.username = username
        self.password = password

    def testOutput(self): 
        str =  f"Welcome user: {self.username} Password: {self.password}"
        return str
    