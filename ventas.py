import pandas as pd
import numpy as np

df = pd.read_csv('ventas_totales.csv')
#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

# quitar nulos en columna salon_ventas
df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))
valores_nulos = df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna tarjetas_debito
df['tarjetas_debito'] = df['tarjetas_debito'].fillna(round(df['tarjetas_debito'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna tarjetas_credito
df['tarjetas_credito'] = df['tarjetas_credito'].fillna(round(df['tarjetas_credito'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna otros_medios
#print(df['otros_medios'].describe())
df['otros_medios']=df['otros_medios'].fillna(6922148.759)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna subtotal_ventas_alimentos_bebidas
df['subtotal_ventas_alimentos_bebidas'] =df['subtotal_ventas_alimentos_bebidas'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna bebidas
df['bebidas'] =df['bebidas'].fillna(round(df['bebidas'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna almacen
df['almacen'] =df['almacen'].fillna(method='bfill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna panaderia
df['panaderia'] =df['panaderia'].fillna(0)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna lacteos
df['lacteos'] =df['lacteos'].fillna(0)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna carnes
df['carnes'] =df['carnes'].fillna(round(df['carnes'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna verduleria_fruteria
df['verduleria_fruteria'] =df['verduleria_fruteria'].fillna(method='bfill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna alimentos_preparados_rotiseria
df['alimentos_preparados_rotiseria'] =df['alimentos_preparados_rotiseria'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna indumentaria_calzado_textiles_hogar
df['indumentaria_calzado_textiles_hogar'] =df['indumentaria_calzado_textiles_hogar'].fillna(round(df['indumentaria_calzado_textiles_hogar'].mean(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna electronicos_articulos_hogar
df['electronicos_articulos_hogar'] =df['electronicos_articulos_hogar'].fillna(round(df['electronicos_articulos_hogar'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# quitar nulos de columna otros
df['otros'] =df['otros'].fillna(round(df['otros'].mean(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# Convertir DataFrame a CSV 
df.to_csv('ventas_totales_limpio.csv')