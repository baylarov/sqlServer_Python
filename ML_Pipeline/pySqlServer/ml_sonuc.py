import pyodbc
import pandas as pd

# Bağlantı bilgileri
server = 'private/server'
db = 'private_db'
user = 'pr_user'
psw = '123456'
tcon = 'No'

# Bağlantı havuzu
cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=db,trusted_connection=tcon, user=user, password=psw,autocommit=True)

alanlar=['HK_ADI','RR_ID','HH_ADI','HH_SOYADI','HH_TEL_NO','HH_ADRES','BB','DD_ISIM_SOYISIM',
         "RR_BASLANGIC_AY_GUN", "RR_BASLANGIC_SAATI","RR_BASLANGIC_GUNU", "ML_OLASILIK"]

cursor_2=cnxn.cursor()
cursor_2.fast_executemany = True
cnxn.execute("TRUNCATE TABLE dbo.ML_Sonuc")

# iPython tarafta işlenen df
return_data["ML_SONUC"] = 1 - model_39.predict(x_test)

cursor_2.executemany(
    '''
    INSERT INTO dbo.ML_Sonuc (
    'HK_ADI','RR_ID','HH_ADI','HH_SOYADI','HH_TEL_NO','HH_ADRES','BB','DD_ISIM_SOYISIM',
    "RR_BASLANGIC_AY_GUN", "RR_BASLANGIC_SAATI","RR_BASLANGIC_GUNU_TR", "ML_OLASILIGI_SONUC")
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    list(return_data.loc[:,alanlar].itertuples(index=False, name=None))
)

cursor_2.close()
del cursor_2

cnxn.close()
del cnxn