import pandas as pd
from sqlalchemy import create_engine
import yaml

def get_credentials():
    ''' This function loads the credentials.yaml file and returns the data dictionary contained within'''
    with open('credentials.yaml') as f:
        data=yaml.safe_load(f)
        return data

class RDSDataBaseConnector:
    ''' This class is used to connect to the remote database'''
    def __init__(self,data):
        self.data=data
    
    def extract_from_database(self,data):
        '''This method initialises a SQLAlchemy engine from the credentials provided to the class.'''
        self.DATABASE_TYPE = 'postgresql'
        self.DBAPI = 'psycopg2'
        self.RDS_USER=data['RDS_USER']
        self.RDS_PASSWORD=data['RDS_PASSWORD']
        self.RDS_HOST=data['RDS_HOST']
        self.RDS_PORT=data['RDS_PORT']
        self.RDS_DATABASE=data['RDS_DATABASE']
        self.engine = create_engine(f"{self.DATABASE_TYPE}+{self.DBAPI}://{self.RDS_USER}:{self.RDS_PASSWORD}@{self.RDS_HOST}:{self.RDS_PORT}/{self.RDS_DATABASE}")
        
    def create_dataframe(self):
        '''This method extracts data from the RDS database and returns it as a Pandas DataFrame'''
        df = pd.read_sql_table('customer_activity', self.engine)
        return df

def save_as_csv(df):
    '''This function saves the data to an appropriate file format to your local machine.'''
    df.to_csv('file.csv', index=False)

def load_to_dataframe():
    '''This function loads the data from your local machine into a Pandas DataFrame.'''
    dataframe=pd.read_csv('file.csv')
    return dataframe

if __name__ == '__main__':
  credentials_dict=get_credentials()
  db_connector=RDSDataBaseConnector(credentials_dict)
  db_connector.extract_from_database(credentials_dict)
  customer_activity=db_connector.create_dataframe()
  save_as_csv(customer_activity)
  dataframe=load_to_dataframe()
  print(dataframe.head())

