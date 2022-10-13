import pandas as pd
# Leer un Excel
ex = pd.read_excel("carga-bip.xlsx")

# Mostrar un resumen
# con las 15 primeras filas
print(ex.head(15))


# Leer Excel, desde la fila que corresponde
bip = pd.read_excel("carga-bip.xlsx", header=9)
print("bip: ",bip)

## Filtrar datos
# Obtener solo los datos de las columnas: CODIGO, NOMBRE FANTASIA
cod_nom = bip.loc[ : , ["CODIGO","NOMBRE FANTASIA"]]
print("cod_nom", cod_nom)

# Podemos crear columnas dinámicamente
# asignando los valores de otra columna o filtro
cod_nom["COMUNA"] = bip.loc[ : , ["MAIPU"]]
print("cod_nom con COMUNA: ",cod_nom)

# Podemos crear columnas con un dato predefinido, para modificar después
cod_nom["ESTACIONAMIENTO"] = "NO"
cod_nom["ES PAR"] = bip.loc[ : , ["CODIGO"]]
print("cod_nom con dos columnas mas", cod_nom)
# Aplicando la lógica si el valor registrado en "ES PAR", 
# que se asignó desde CODIGO, es un número par, entonces "ES PAR" será SI
cod_nom["ES PAR"] = cod_nom["ES PAR"].apply(lambda x: "SI" if (int(x) % 2 == 0) else "NO")
print("cod_nom con ES PAR modificado", cod_nom)

# Además me permite guardar como distintos tipos de archivos
cod_nom.to_csv("codigo-bip.csv", encoding="utf-8")
cod_nom.to_json("codigo-bip.json")
cod_nom.to_excel("codigo-bip.xlsx")

# Crear un DataFrame solo para PROVIDENCIA
cod_provi=cod_nom[cod_nom["COMUNA"]=="PROVIDENCIA"]
cod_provi.to_excel("codigo-bip-provi.xlsx")

