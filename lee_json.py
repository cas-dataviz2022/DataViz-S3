import json
mi_json = open("datos.json","r", encoding="utf-8")
print(mi_json)
json_datos = mi_json.read()
datos = json.loads(json_datos)
print("json_datos: ", json_datos)
print("datos: ", datos)
print("temperaturas: ", datos["temperaturas"])


# Deseo generar una lista solo con los días y sus temperaturas
# Luego guardar esa lista como un archivo CSV

# Genero una variable de tipo List
dias_temps = ["Día;Temperatura en la Mañana"]

# Usando un ciclo, extraigo los datos uno a uno
# y los voy agregando a mi lista
for temps in datos["temperaturas"]:
    t_dia = temps["dia"]
    t_temp = temps["t"]
    dias_temps.append(f"{t_dia};{t_temp}")

print(dias_temps)

# creo un archivo CSV
mi_csv = open("datos.csv","w", encoding="utf-8")
# se recorre cada elemento de la lista
for dia_temp in dias_temps:
    # se escribe una linea de datos por cada elemento de la lista
    mi_csv.write(dia_temp + "\n")
# finalmente se cierra el archivo
mi_csv.close()
