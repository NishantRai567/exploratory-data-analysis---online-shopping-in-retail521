import yaml
from sqlalchemy import create_engine
import pandas as pd

def get_credentials():
    with open('credentials.yaml') as f:
        data=yaml.safe_load(f)
        return data

class RDSDataBaseConnector:
    def __init__(self,data):
        self.data=data
    
    def extract_from_database(self,data):
        self.DATABASE_TYPE = 'postgresql'
        self.DBAPI = 'psycopg2'
        self.RDS_USER=data['RDS_USER']
        self.RDS_PASSWORD=data['RDS_PASSWORD']
        self.RDS_HOST=data['RDS_HOST']
        self.RDS_PORT=data['RDS_PORT']
        self.RDS_DATABASE=data['RDS_DATABASE']
        self.engine = create_engine(f"{self.DATABASE_TYPE}+{self.DBAPI}://{self.RDS_USER}:{self.RDS_PASSWORD}@{self.RDS_HOST}:{self.RDS_PORT}/{self.RDS_DATABASE}")
        
    def create_dataframe(self):
        df = pd.read_sql_table('customer_activity', self.engine)
        return df

def save_as_csv(df):
    df.to_csv('file.csv', index=False)

def load_to_dataframe():
    dataframe=pd.read_csv('file.csv')
    return dataframe

credentials_dict=get_credentials()
db_connector=RDSDataBaseConnector(credentials_dict)
db_connector.extract_from_database(credentials_dict)
customer_activity=db_connector.create_dataframe()
save_as_csv(customer_activity)
dataframe=load_to_dataframe()
print(dataframe.shape)
print(dataframe.head())

