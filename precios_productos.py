import pandas as pd 
df = pd.read_excel('precios_productos.xlsx')
#print(df.isnull().sum())

# Aquí reemplazo los nulos en la columna "NOMBRE_VENDEDOR"
# por "--" ya que no puedo imputar nombres que desconozco
df['NOMBRE_VENDEDOR'] = df['NOMBRE_VENDEDOR'].fillna("--")
#print(df.isnull().sum())

# Convertir DataFrame a CSV 
df.to_csv('precios_productos_limpio.csv')