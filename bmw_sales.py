# %%
import kagglehub
import pandas as pd
import os

# 1. Descargamos el dataset (Kaggle lo guardará en una carpeta temporal en tu PC)
ruta_descarga = kagglehub.dataset_download("dmahajanbe23/bmw-global-automotive-sales")

# 2. Como se descarga una carpeta, buscamos cuál es el archivo CSV adentro
archivos = os.listdir(ruta_descarga)
archivo_csv = [f for f in archivos if f.endswith('.csv')][0]

# 3. Unimos la ruta y lo leemos con Pandas
ruta_completa = os.path.join(ruta_descarga, archivo_csv)
df_bmw = pd.read_csv(ruta_completa)

# 4. ¡Listo! Vemos las primeras filas
df_bmw.head()

# %%
# 1. Búsqueda de valores nulos (celdas vacías)
print("--- VALORES NULOS POR COLUMNA ---")
print(df_bmw.isnull().sum())
print("\n" + "="*30 + "\n")

# 2. Búsqueda de registros duplicados
print("--- FILAS DUPLICADAS ---")
print(f"Cantidad de duplicados exactos: {df_bmw.duplicated().sum()}")
print("\n" + "="*30 + "\n")

# 3. Auditoría estadística de las variables numéricas
print("--- RESUMEN ESTADÍSTICO (Atención a mínimos y máximos) ---")
# Usamos round(2) para leer los valores financieros como euros reales
df_bmw.describe().round(2)
# %%
import matplotlib.pyplot as plt
# %%
plt.figure(figsize=(10, 6))
# %%
# regplot crea el gráfico de puntos y además traza una línea de tendencia matemática
sns.regplot(data=df_bmw, x='Fuel_Price_Index', y='BEV_Share', 
            scatter_kws={'alpha':0.3, 'color':'gray'}, 
            line_kws={'color':'red', 'linewidth':2})

plt.title('Relación: Precio del Combustible vs Adopción de Autos Eléctricos', fontsize=14)
plt.xlabel('Índice de Precio del Combustible', fontsize=12)
plt.ylabel('Adopción de Eléctricos (BEV_Share)', fontsize=12)
plt.show()

# %%
import matplotlib.pyplot as plt
import seaborn as sns  # <-- ¡Esta es la llave maestra que faltaba!

plt.figure(figsize=(10, 6))

# regplot crea el gráfico de puntos y además traza una línea de tendencia matemática
sns.regplot(data=df_bmw, x='Fuel_Price_Index', y='BEV_Share', 
            scatter_kws={'alpha':0.3, 'color':'gray'}, 
            line_kws={'color':'red', 'linewidth':2})

plt.title('Relación: Precio del Combustible vs Adopción de Autos Eléctricos', fontsize=14)
plt.xlabel('Índice de Precio del Combustible', fontsize=12)
plt.ylabel('Adopción de Eléctricos (BEV_Share)', fontsize=12)
plt.show()

# %%
# Agrupamos, sumamos las unidades y ordenamos de mayor a menor
ventas_region = df_bmw.groupby('Region')['Units_Sold'].sum().sort_values(ascending=False)

print("--- VENTAS TOTALES POR REGIÓN ---")
print(ventas_region)

plt.figure(figsize=(8, 4))
sns.barplot(x=ventas_region.index, y=ventas_region.values, palette='Blues_r')
plt.title('Unidades Vendidas por Región (2018-2025)', fontsize=14)
plt.ylabel('Unidades Vendidas')
plt.show()

# %%
# Agrupamos por modelo, ordenamos y nos quedamos solo con los 10 primeros
ventas_modelo = df_bmw.groupby('Model')['Units_Sold'].sum().sort_values(ascending=False).head(10)

print("\n--- TOP 10 MODELOS MÁS VENDIDOS ---")
print(ventas_modelo)

plt.figure(figsize=(10, 5))
# Gráfico de barras horizontales para leer mejor los nombres de los autos
sns.barplot(x=ventas_modelo.values, y=ventas_modelo.index, palette='crest')
plt.title('Top 10 Modelos de BMW Más Vendidos', fontsize=14)
plt.xlabel('Unidades Vendidas')
plt.ylabel('Modelo')
plt.show()

# %%
# Agrupamos solo por año sin alterar el orden
ventas_anio = df_bmw.groupby('Year')['Units_Sold'].sum()

print("\n--- EVOLUCIÓN DE VENTAS POR AÑO ---")
print(ventas_anio)

plt.figure(figsize=(10, 4))
sns.lineplot(x=ventas_anio.index, y=ventas_anio.values, marker='o', color='black', linewidth=2)

plt.title('Evolución de Unidades Vendidas por Año', fontsize=14)
plt.xlabel('Año')
plt.ylabel('Unidades Vendidas')
# Obligamos al gráfico a mostrar solo números enteros en los años
plt.xticks(ventas_anio.index) 
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# %%
# Agrupamos por modelo, sumamos las unidades y ordenamos de menor a mayor
menos_vendidos = df_bmw.groupby('Model')['Units_Sold'].sum().sort_values(ascending=True).head(10)

print("\n--- TOP 10 MODELOS MENOS VENDIDOS ---")
print(menos_vendidos)

plt.figure(figsize=(10, 5))
# Gráfico de barras horizontales usando una paleta de colores rojos para denotar "bajas ventas"
sns.barplot(x=menos_vendidos.values, y=menos_vendidos.index, palette='Reds_r')
plt.title('Top 10 Modelos de BMW Menos Vendidos (2018-2025)', fontsize=14)
plt.xlabel('Unidades Vendidas')
plt.ylabel('Modelo')
plt.show()

# %%
# 1. Contamos cuántos modelos diferentes existen en la columna 'Model'
cantidad_modelos = df_bmw['Model'].nunique()

print(f"BMW vende un total de {cantidad_modelos} modelos diferentes en este dataset.\n")

# 2. Si quieres ver cuáles son exactamente esos modelos, usamos unique()
nombres_modelos = df_bmw['Model'].unique()

print("--- LISTA COMPLETA DE MODELOS ---")
print(nombres_modelos)

# %%
# 1. Agrupamos por modelo y usamos agg() para pedir el mínimo ('min') y el máximo ('max') del precio
precios_por_modelo = df_bmw.groupby('Model')['Avg_Price_EUR'].agg(['min', 'max']).round(2)

# 2. Le cambiamos el nombre a las columnas para que el reporte quede más profesional
precios_por_modelo.columns = ['Precio Mínimo (€)', 'Precio Máximo (€)']

# 3. Ordenamos la tabla desde el auto con el precio máximo más alto, hasta el más barato
precios_por_modelo = precios_por_modelo.sort_values(by='Precio Máximo (€)', ascending=False)

print("--- RANGO DE PRECIOS POR MODELO ---")
print(precios_por_modelo)

# %%
# 1. Filtramos para quedarnos solo con las columnas que tienen números
datos_numericos = df_bmw.select_dtypes(include=['number'])

# 2. Calculamos la matriz de correlación de Pearson
correlaciones = datos_numericos.corr()

# 3. Configuramos el tamaño del gráfico
plt.figure(figsize=(12, 8))

# 4. Creamos el Heatmap
# annot=True pone los números dentro de los cuadritos
# cmap='coolwarm' usa rojo para correlaciones positivas y azul para negativas
# fmt=".2f" redondea a dos decimales
sns.heatmap(correlaciones, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

# 5. Títulos
plt.title('Mapa de Calor de Correlaciones - BMW Global Sales', fontsize=16)
plt.show()

# %%
# 1. Agrupamos por modelo y sumamos los ingresos
ingresos_modelo = df_bmw.groupby('Model')['Revenue_EUR'].sum().sort_values(ascending=False)

# 2. Dividimos por mil millones (1e9) para que los números sean legibles
ingresos_modelo_billones = ingresos_modelo / 1e9

print("--- FACTURACIÓN TOTAL POR MODELO (En Miles de Millones de €) ---")
print(ingresos_modelo_billones.round(2))

# 3. Graficamos
plt.figure(figsize=(10, 5))
# Usamos una paleta verde, clásica para representar dinero/ingresos
sns.barplot(x=ingresos_modelo_billones.values, y=ingresos_modelo_billones.index, palette='Greens_r')

plt.title('Ingresos Totales por Modelo de BMW (2018-2025)', fontsize=14)
plt.xlabel('Ingresos (Miles de Millones de Euros)', fontsize=12)
plt.ylabel('Modelo', fontsize=12)
plt.show()

# %%
# 1. Agrupamos por región y sumamos los ingresos
ingresos_region = df_bmw.groupby('Region')['Revenue_EUR'].sum()

# 2. Creamos el gráfico de torta
plt.figure(figsize=(8, 8))

# autopct='%1.1f%%' calcula e imprime los porcentajes automáticamente en el gráfico
plt.pie(ingresos_region, 
        labels=ingresos_region.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=sns.color_palette('Set2'),
        explode=[0.05]*len(ingresos_region)) # Esto separa un poquito las porciones

plt.title('Distribución Global de Ingresos por Región', fontsize=15, fontweight='bold')
plt.show()

