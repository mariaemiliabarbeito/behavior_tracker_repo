#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:40:35 2026

@author: mariaemiliabarbeito
"""

from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.metricas import calcular_tiempo_total, calcular_promedio_uso
from src.procesamiento_datos import filtrar_por_participante

datos = cargar_datos ("datos/datos_proyecto.csv")
datos_validos= []
for registro in datos: 
    if validar_registro(registro):
        datos_validos.append(registro)
id_participante= int(input("Ingrese id del participante: "))
datos_participante = filtrar_por_participante(datos_validos,id_participante)
tiempo_total= calcular_tiempo_total(datos_validos)
promedio_uso= calcular_promedio_uso (datos_validos)

print("Tiempo total: {tiempo_total}")
print("El promedio de uso es: {promedio_uso")
