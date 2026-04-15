#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:36:07 2026

@author: mariaemiliabarbeito
"""
def parsear_linea(linea):
    """
    Que hace la funcion: separa una linea, convierte algunos valores a int y devuelve una lista parseada./
    Maneja errores.

    Parametros
    ----------
    linea : string
         linea con informacion del participante separado por comas.

    Retorna
    -------
       lista- devuelve una lista con los valores separados
       None- Ocurre si alguno de los valores no se puede convertir 
       
    """
    linea_str=linea.strip()
    linea_spl=linea_str.split(",")
    
    try:
        id_participante= int(linea_spl[0])
        fecha= linea_spl[1]
        app=linea_spl[2] 
        cantidad=int(linea_spl[3])
        tiempo=int(linea_spl[4])
    except:
        print("Hubo un error al parsear una de las lineas")
        return None
    return [id_participante, fecha, app, cantidad, tiempo]
        
    
def cargar_datos(ruta):
    """
    Que hace la funcion: Lee un archivo CSV y devuelve una lista de registros.

    Parametros
    ----------
    ruta : str
        Ruta del archivo

    Retorna
    -------
    lista: lista de diccionarios con los datos

    """
    with open (ruta, "r") as archivo:
    datos=[]
        for linea in archivo:
            valores= parsear_linea(linea)  
            if valores == None:
                continue
            for dato in datos:
               if linea_parseada[0] not in dato["id"]:
                   diccionario={}
                   diccionario["id"]= linea_parseada[0]
                   diccionario["valor"]= linea_parseada[1]
               else:
                   diccionario["valor"].append(linea_parseada[1])
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
  