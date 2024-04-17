import pandas as pd
df = pd.read_excel('devoluciones.xlsx')
#print(df.head())
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "CVE_VEND" con un espacio en
# blanco " " ya que no puedo crear una clave de vendedor o realizar 
# una imputación que podría llevar a futuros errores. 
df['CVE_VEND']=df['CVE_VEND'].fillna(' ')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "CVE_PED" con un espacio en 
# blanco " " ya que no puedo realizar una imputación con claves de pedidos
# que podrían ser erróneas
df['CVE_PEDI']=df['CVE_PEDI'].fillna(' ')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "FECHA_CANCELA" con un espacio en
# blanco " " ya que no puedo realizar una imputación de fechas dado que 
# podrían imputarse fechas erróneas 
df['FECHA_CANCELA'] = df['FECHA_CANCELA'].fillna(' ')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "DOC_ANT" con un espacio en blanco 
# " " ya que realizar una imputación para esta columna podría causar más 
# errores dado que no puedo crear una clave de documento imaginaria
df['DOC_ANT'] = df['DOC_ANT'].fillna(' ')
print(df.isnull().sum())

# Convertir DataFrame a CSV 
df.to_csv('devoluciones_limpio.csv')