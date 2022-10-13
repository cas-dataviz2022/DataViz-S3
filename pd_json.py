import pandas as pd
import json
mi_json = open("datos.json","r", encoding="utf-8")
print(mi_json)
json_datos = mi_json.read()
datos = json.loads(json_datos)

# Se normalizan los datos desde JSON hacia Pandas
temps = pd.json_normalize(datos, record_path= "temperaturas")

print(temps)
# Se genera el objeto DataFrame de Pandas
mi_csv = pd.DataFrame(temps)
# Se cambia el nombre de las columnas
mi_csv.rename(columns={"d":"Día", "t":"Temperatura en la Mañana"}, inplace=True)
# Se escribe el archivo CSV
mi_csv.to_csv("datos_pandas.csv", encoding="utf-8", index=0)
