#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:36:07 2026

@author: mariaemiliabarbeito
"""
from validar_datos.py import validar_datos

def parsear_linea(linea):
    """
    Que hace la funcion: separa una linea, verifica que tenga el formato correcto y devuelve una lista parseada./

    Parametros:
    linea : string
         linea con informacion del participante separado por comas.

    Retorna:
       lista- devuelve una lista con los valores separados pero sin validarlos.
      
    Excepciones:
        ValueError: si la linea esta vacia o no tiene la cantidad de columnas necesarias.
       
    """
    linea_str= linea.strip()
    if linea_str == "":
        raise ValueError("La línea del archivo está vacía")
    registro = linea_str.split(",")
    
    if len(registro) != 5:
        raise ValueError("La linea del archivo no tiene la cantidad de columnas necesarias")
   
    return registro
        
    
def cargar_datos(ruta):
    """
    Que hace la funcion: 
        Lee un archivo CSV y devuelve una lista de registros.

    Parametros
    ruta : str
        Ruta del archivo

    Retorna:
    datos: list
    lista de diccionarios con los datos de cada participante.
    
    Excepciones:
        FileNotFoundError: si el archivo no existe.
        Exception: si no se logra abrir el archivo.
        ValueError: si el archivo esta vacío.

    """
    try: 
        with open (ruta, "r") as archivo: 
            lineas = archivo.readlines()
    except FileNotFoundError:
        raise FileNotFoundError("El archivo no existe")
    except Exception: 
        raise Exception("No se pudo abrir el archivo")
    if len(lineas) == 0:
        raise ValueError("El archivo esta vacio.")
        
    datos=[]
    for linea in lineas:
        registro = parsear_linea(linea)
        registro = validar_datos(registro) ##% se pisa registro porque se reemplaza por uno validado y con valores convertidos
        
        id_participante = registro[0]
        fecha =  registro[1]
        app = registro[2]
        cantidad_uso = registro[3]
        tiempo_uso = registro[4]
        
        encontrado = False
        
        for registro_participante in datos:
            if registro_participante["id_participante"] == id_participante:
                registro_participante["fecha"].append(fecha)
                registro_participante["app"].append(app)
                registro_participante["cantidad_uso"].append(cantidad_uso)
                registro_participante["tiempo_uso"].append(tiempo_uso)
                encontrado = True
               
        if encontrado == False:
            registro_participante_nuevo= {"id_participante": id_participante, "fecha": [fecha], "app": [app], "cantidad_uso": [cantidad_uso], "tiempo_uso": [tiempo_uso] }
            datos.append(registro_participante_nuevo)
            
    return datos

             
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
  