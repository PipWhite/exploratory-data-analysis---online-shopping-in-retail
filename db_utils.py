import yaml
import psycopg2
from sqlalchemy import create_engine, inspect, text
import pandas as pd


def get_credentials():
    with open('credentials.yaml', 'r') as file:
            credentials = yaml.safe_load(file)
    print(credentials)
    return credentials

RDS_credentials = get_credentials()





class RDSDatabaseConnector():
    def __init__(self):
        self.credentials = RDS_credentials

    def init_engine(self, credentials):
        HOST = credentials.get('RDS_HOST')
        PASSWORD = credentials.get('RDS_PASSWORD')
        USER = credentials.get('RDS_USER')
        DATABASE = credentials.get('RDS_DATABASE')
        PORT = credentials.get('RDS_PORT')
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        
        with psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DATABASE, port=PORT) as conn:
            with conn.cursor() as cur:
                cur.execute(''' SELECT * FROM customer_activity ''')
                print(type(cur))
                records = cur.fetchall()

        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

        engine.execution_options(isolation_level='AUTOCOMMIT').connect()
        return engine

    def extract_data(self):
        inspector = inspect(engine)
        inspector.get_table_names
        
        customer_activity = pd.read_sql_table('customer_activity', engine)
        return customer_activity


connector = RDSDatabaseConnector()
engine = connector.init_engine(RDS_credentials)
customer_activity = connector.extract_data()
print(type(customer_activity))

customer_activity.to_csv('customer_activity.csv')

