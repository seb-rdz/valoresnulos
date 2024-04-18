import pandas as pd 
df = pd.read_excel('clientes.xlsx')
#print(df.head())
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "RFC" con el RFC generico XAXX010101000
df['RFC']=df['RFC'].fillna('XAXX010101000')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "NOMBRE" con "--",
#  pues no se puede inventar e imputar un nombre que desconocemos  
df['NOMBRE']=df['NOMBRE'].fillna('--')
#print(df.isnull().sum())

# Convertir DataFrame a CSV 
df.to_csv('clientes_limpio.csv')