import pandas as pd
import pymysql

host="di-test.cluster-cuaie290qfbf.eu-west-1.rds.amazonaws.com"
port=3306
dbname="di-test"
user="diadmin"
password="diadmin613!"

conn = pymysql.connect(host, user=user,port=port,
                           passwd=password, db=dbname)
pd.read_sql('select * from person;', con=conn)