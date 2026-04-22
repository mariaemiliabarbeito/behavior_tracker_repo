#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:40:35 2026

@author: mariaemiliabarbeito
"""

from src.carga_datos import cargar_datos
<<<<<<< HEAD
from src.validacion_datos import validar_registro
from src.metricas import (calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app)
=======
from src.validacion_datos import validar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso
>>>>>>> 24b270ee1f965bc154baa4701a7031d5862f581d
from src.procesamiento_datos import filtrar_por_participante
try:
    datos = cargar_datos ("datos/datos_proyecto.csv")
except FileNotFoundError as e:
    print(f"Error en el archivo: {e}")
    exit()
except ValueError as e:
    print(f"Error en los valores de los datos: {e}")
    exit()
except Exception as e:
   print (f"Error inesperado: {e}")
   exit()

<<<<<<< HEAD
try:
    id_participante = input("ingrese el id del participante que desea filtrar: ")
    datos_filtrados = [filtrar_por_participante(datos, id_participante)]
except ValueError as e:
    print(f"Error con el id o con el participante: {e} ")
    exit()
except KeyError as e:
    print(f" error con datos: {e}")
    exit()
except Exception as e:
   print (f"Error inesperado: {e}")
   exit()
    
##%%%%%%%%la parte de metricas nose como hacerla
datos_validos= []
for registro in datos: 
    if validar_registro(registro):
=======
def main ():
    datos = cargar_datos("datos/datos_proyecto.csv")
    datos_validos= []

    for registro in datos: 
    if validar_datos(registro):
>>>>>>> 24b270ee1f965bc154baa4701a7031d5862f581d
        datos_validos.append(registro)
id_participante= int(input("Ingrese id del participante: "))
datos_participante = filtrar_por_participante(datos_validos,id_participante)
tiempo_total= calcular_tiempo_total(datos_validos)
promedio_uso= calcular_promedio_uso (datos_validos)

print("Tiempo total: {tiempo_total}")
print("El promedio de uso es: {promedio_uso")
