import pyodbc
import pandas as pd

#Bağlantı bilgileri
server = 'private/server'
db = 'private_db'
user = 'pr_user'
psw = '123456'
tcon = 'No'
start_date='20200201'
end_date='20200313'

#SQL Server sorguları
exec_sp="EXEC [dbo].[sp_TrainFullDataset] '{}','{}'".format(start_date,end_date)
sql_query="SELECT * FROM dbo.TrainFullDataset"

cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=db,
                      trusted_connection=tcon, user=user, password=psw,autocommit=True)

cursor=cnxn.cursor()

print("Aşağıdaki sorgu çalışıyor: \n{}".format(exec_sp))
print('\n')
cursor.execute(exec_sp)

print("SP çalıştırıldı, sorgu sonucu Pandas dataframe`e yansıtılıyor...")
print('\n')

cursor.execute(sql_query)
cursor.close()
del cursor

df = pd.read_sql_query(sql_query, cnxn)
cnxn.close()
del cnxn