import json
import pandas as pd
import matplotlib.pyplot as plt

# Leer Excel, desde la fila que corresponde
bip = pd.read_excel("carga-bip.xlsx", header=9, index_col=0)
print("bip: ", bip)

# Corregir nombre de la columna de comunas
# el Excel la tiene como "MAIPU", pero debe indicar "COMUNA"
bip.rename(columns={"MAIPU": "COMUNA"}, inplace=True)
print("acá se despliega la información: ", bip, "Ya mostré el contenido")

########################################
### Generar Total de Puntos de Carga ###

# Filtrar datos de una sola comuna
provi = bip[ bip["COMUNA"]=="PROVIDENCIA" ]

# Obtener Filas y Columnas de los datos
# Para esto primero se genera como Numpy 
# y de ahí su forma, con la función "shape".
provi_filas, provi_columnas = provi.to_numpy().shape

# Ya podemos pasar el contador de filas a nuestro Diccionario
puntos_de_carga = {
    "PROVIDENCIA": provi_filas
}

# Luego guardamos usando la librería json.
# Además indicamos su codificación en UTF-8
# y que mantenga una identación de 2 caracteres 
with open("puntos-carga.json", "w", encoding="utf-8") as j:
    j.write( json.dumps(puntos_de_carga, indent=2) )

######################################################
### Generar CSV con Puntos de Carga para 3 comunas ###
# Filtrar datos de 3 comunas
puntos_comunas = [
    bip[ bip["COMUNA"] == "RENCA" ] ,
    bip[ bip["COMUNA"] == "LA FLORIDA" ]
]
puntos_comunas.append( bip[ bip["COMUNA"] == "ÑUÑOA" ] )

# Unir los elementos de la lista 
# Corregir el nombre de la columna de dirección, en este caso no se usa "inplace" ya que lo hacemos en memoria
# y luego escribir el archivo CSV
pd.concat(puntos_comunas).rename( columns={"CERRO BLANCO 625": "DIRECCION"} ).to_csv("puntos-comunas.csv", encoding="UTF-8")

##########################################################
### Generar valores ficticios para Horario Referencial ###
# Se obtiene la lista de indice de los datos, que corresponde a la columna CODIGO
horario = bip.index
horarios = []
for h in horario:
    # Se evalúa una condición, en este caso que el CODIGO sea par
    if (h % 2 == 0):
        horarios.append("09:00 - 13:00, 14:00 - 19:00")
    else:
        horarios.append("08:30 - 12:30, 13:30 - 18:30")

# Otra forma de escribir el bloque anterior:
# horarios=["09:00 - 13:00, 14:00 - 19:00" if (h % 2 == 0) else "08:00 - 12:00, 13:00 - 18:00" for h in horario]

# Con la lista de horarios completa, se asigna a la columna de datos
bip["HORARIO REFERENCIAL"] = horarios
print(bip)

########################################################################################
### Crear un gráfico de la cantidad de puntos de carga para cada Horario Referencial ###

# Agrupar por la columna requerida
horario_ref = bip.groupby(["HORARIO REFERENCIAL"])
# Crear la referencia al conteo por la columnda requerida
horario_agrupado = horario_ref["HORARIO REFERENCIAL"].count()
# Cerrar todo gráfico previo
plt.close("all")
# Generar el espacio donde se graficará
plt.figure()
# Generar el "ploteo" de los datos agrupados y contados
horario_agrupado.plot()
# Mostrar el gráfico
plt.show()
# Mostrar los datos que se graficaron
print(horario_agrupado)