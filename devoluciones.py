import pandas as pd
df = pd.read_excel('devoluciones.xlsx')
#print(df.head())
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "CVE_VEND" con "--" 
# ya que no puedo imputar una clave de vendedor que desconozco
df['CVE_VEND']=df['CVE_VEND'].fillna('--')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "CVE_PED" con "--"
# ya que no puedo realizar una imputación con claves de pedidos
# que desconozco 
df['CVE_PEDI']=df['CVE_PEDI'].fillna('--')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "FECHA_CANCELA" con "--" 
# ya que no puedo imputar fechas que desconozco
df['FECHA_CANCELA'] = df['FECHA_CANCELA'].fillna('--')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "DOC_ANT" con "--" 
# ya que no puedo imputar una clave de documento que desconozco
df['DOC_ANT'] = df['DOC_ANT'].fillna('--')
#print(df.isnull().sum())

# Convertir DataFrame a CSV 
df.to_csv('devoluciones_limpio.csv')