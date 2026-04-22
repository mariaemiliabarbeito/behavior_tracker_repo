#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:40:35 2026

@author: mariaemiliabarbeito
"""

from src.carga_datos import cargar_datos
## no importo validar_datos porque se importa dentro de cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app)
ruta = "datos/BehaviorTracker_mock_data.csv"

try:
    datos = cargar_datos (ruta)
except FileNotFoundError as e:
    print(f"Error en el archivo: {e}")
    exit()
except ValueError as e:
    print(f"Error en los valores de los datos: {e}")
    exit()
except Exception as e:
   print (f"Error inesperado: {e}")
   exit()
   

try:
    id_participante = input("ingrese el id del participante que desea filtrar: ")
    registro_participante = [filtrar_por_participante(datos, id_participante)] ##lo pongo dentro de una lista para poder usarlo en metricas
except ValueError as e:
    print(f"Error con el id o con el participante: {e} ")
    exit()
except KeyError as e:
    print(f" error con datos: {e}")
    exit()
except Exception as e:
   print (f"Error inesperado: {e}")
   exit()
   
###metricas
try:
    tiempo_total= calcular_tiempo_total(registro_participante)
    promedio_uso= calcular_promedio_uso (registro_participante)
    uso_por_app = calcular_uso_por_app(registro_participante)
except ZeroDivisionError as e: 
    print(f"Error cuando se calcula el promedio: {e}")
except KeyError as e:
     print(f" error con datos: {e}")
     exit()
except Exception as e:
    print (f"Error inesperado: {e}")
    exit()

print(f"Los resultados para el participante {id_participante} son: ")
print("El Tiempo total fue: {tiempo_total}")
print("El promedio de uso fue: {promedio_uso}")
print(f"el uso por app fue: {uso_por_app}")
