import pyodbc
import pandas as pd

# Bağlantı bilgileri
server = 'private/server'
db = 'private_db'
user = 'pr_user'
psw = '123456'
tcon = 'No'
start_date='20190201'
end_date='20200310'
tckn='9999999999999'

# Sorgular
exec_sp_hasta="EXEC [dbo].[sp_TrainFullDataset_Each] '{}','{}','{}'".format(start_date,end_date,tckn)
select_query_hasta="SELECT * FROM dbo.TrainFullDataset_Each"

# Bağlantı havuzu
cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=db,trusted_connection=tcon, user=user, password=psw,autocommit=True)

# Cursor ve sorgular
cursor_1=cnxn.cursor()
print("Aşağıdaki sorgu çalışıyor: \n{}".format(exec_sp_hasta))
print('\n')
cursor_1.execute(exec_sp_hasta)
cursor_1.close()
del cursor_1
print("SP çalıştırıldı, sorgu sonucu Pandas dataframe`e yansıtılıyor...")
print('\n')

veri_2 = pd.read_sql_query(select_query_hasta,cnxn)

print(veri_2.head())