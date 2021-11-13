#CONNECTION CONFIGURATIONS FOR AWS/ADLS
import os, uuid, sys
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings
import pandas as pd

ADLS = {
    "ADLS_name" : '',
    "ADLS_key" : ''
}

def initialize_storage_account(self):

        try:  
            self.service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
                "https", ADLS["ADLS_name"]), credential=ADLS["ADLS_key"])
        
        except Exception as e:
            print(e)

def list_directory_contents(self):
        try:
            
            file_system_client = self.service_client.get_file_system_client(file_system="snowflake-synapse-dm")

            paths = file_system_client.get_paths(path="data")

            for path in paths:
                print(path.name + '\n')

        except Exception as e:
            print("111 Error = ", e)


def download_file_from_directory(self):


    try:
        file_system_client = self.service_client.get_file_system_client(file_system=self.container)

        directory_client = file_system_client.get_directory_client(self.directory)
        
        file_client = directory_client.get_file_client(self.filename)

        #print("file_client = ", type(file_client))

        download = file_client.download_file()    

        #print("download = ", dir(download))
        downloaded_bytes = download.readall()    

        # To convert Bytes to pandas Dataframe -----------------
        df = pd.read_csv(BytesIO(downloaded_bytes), encoding='unicode_escape')
        #print("df =, "df.head())

    # To convert Bytes to pandas Dataframe -----------------
        #s=str(downloaded_bytes, 'ISO-8859-1')
        #data = StringIO(s) 
        #df = pd.read_csv(data)

    # To download the file locally ----------
        # local_file = open("orders.csv",'wb')
        # local_file.write(downloaded_bytes)
        # local_file.close()

        return df

    except Exception as e:
        print("Error = ", e)
