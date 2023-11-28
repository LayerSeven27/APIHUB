#!/bin/bash

# Comando para buscar la cadena "Inst. Geogr. Nacional" en el archivo pagina.html
resultado=$(grep "gmnoprint gm-style-mtc-bbw" tmp/pagina.html)

# Verificar si la cadena fue encontrada o no
if [ -n "$resultado" ]; then
    echo "VULNERABILITY DETECTED"
    
    # Pregunta al usuario si desea ejecutar la solución
    read -p "Do you want to attack? (Y/N): " respuesta

    # Comprueba la respuesta del usuario
    if [ "$respuesta" == "Y" ] || [ "$respuesta" == "y" ]; then
        # Ejecutar ddos
        python3 dos.py
	pkill php
    else
        echo "The attack will not be executed"
	pkill php
    fi
else
    echo "TRY ANOTHER ONE!"
	pkill php
fi
