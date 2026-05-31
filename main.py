#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:40:35 2026

@author: mariaemiliabarbeito
"""

from src.carga_datos import cargar_datos
from src.validacion_datos import validar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app)
from src.graficos import (tiempo_por_app_grafico, grafico_tiempo_uso_por_fecha)

ruta_csv = "datos/BehaviorTracker_mock_data.csv"
try:
    df = cargar_datos(ruta_csv)
    df=validar_datos(df)
    id_participante=input("Ingrese el Id del participante")
    df_filtrado = filtrar_por_participante(df,id_participante)

except FileNotFoundError as e:
    print(f"Error en el archivo: {e}")
except ValueError as e:
    print(f"Error en los datos: {e}")
except TypeError as e :
    print(f"Error en el tipo de dato: {e}")

try:  
    tiempo_total_app= calcular_tiempo_total(df_filtrado, "app")
    print(f"El Tiempo total fue: {tiempo_total_app}")
    tiempo_total_fecha= calcular_tiempo_total(df_filtrado, "fecha")
    print(f"El Tiempo total fue: {tiempo_total_fecha}")
    promedio_uso= calcular_promedio_uso (df_filtrado, "app")
    print(f"El promedio de uso fue: {promedio_uso}")
    uso_por_app = calcular_uso_por_app(df_filtrado, "app")
    print(f"el uso por app fue: {uso_por_app}")
    tiempo_por_app_grafico(tiempo_total_app)
    grafico_tiempo_uso_por_fecha(tiempo_total_fecha)
except ZeroDivisionError as e: 
    print(f"Error cuando se calcula el promedio: {e}")
except KeyError as e:
     print(f" error con datos: {e}")     
except Exception as e:
    print (f"Error inesperado: {e}")
   


   





 
   
   


