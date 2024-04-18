import pandas as pd 
df = pd.read_excel('notas_credito.xlsx')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "CVE_VEND"
# por "--" dado que no puedo imputar claves de vendedor 
# que desconozco 
df['CVE_VEND'] = df['CVE_VEND'].fillna('--')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "CVE_PEDI"
# por "--" ya que no puedo imputar claves de pedidos que
# desconozco 
df['CVE_PEDI'] = df['CVE_PEDI'].fillna('--')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "FECHA_CANCELA"
# por "--" ya que no puedo imputar fechas 
# que desconozco 
df['FECHA_CANCELA'] = df['FECHA_CANCELA'].fillna('--')
#print(df.isnull().sum())

# Convertir DataFrame a CSV 
df.to_csv('notas_credito_limpio.csv')