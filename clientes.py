import pandas as pd 
df = pd.read_excel('clientes.xlsx')
#print(df.head())
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "RFC" con el RFC generico XAXX010101000
df['RFC']=df['RFC'].fillna('XAXX010101000')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "NOMBRE" com un espacio en blanco,
#  pues no se puede inventar un nombre   
df['NOMBRE']=df['NOMBRE'].fillna('')
#print(df.isnull().sum())

# Convertir DataFrame a CSV 
df.to_csv('clientes_limpio.csv')