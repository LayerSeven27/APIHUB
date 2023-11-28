import shutil

nombre_archivo = "index.html"

# Hacemos una copia del archivo en la carpeta temporal
ruta_original = nombre_archivo
ruta_temporal = "tmp/index.html"
shutil.copyfile(ruta_original, ruta_temporal)

# Le preguntamos al usuario qué cadena desea sustituir
cadena_a_sustituir = "ByLayerSeven"

# Le preguntamos al usuario por la nueva cadena con la que desea reemplazarla
nueva_cadena = input("Enter the Google Maps API key: ")

# Leemos el contenido del archivo temporal
with open(ruta_temporal, 'r') as archivo:
    contenido = archivo.read()

# Realizamos la sustitución
contenido_modificado = contenido.replace(cadena_a_sustituir, nueva_cadena)

# Escribimos el contenido modificado de vuelta al archivo temporal
with open(ruta_temporal, 'w') as archivo_modificado:
    archivo_modificado.write(contenido_modificado)
