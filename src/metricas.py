   #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:39:37 2026

@author: mariaemiliabarbeito
"""

def calcular_tiempo_total(datos):
    """
    Que hace la funcion: calcula el tiempo total de uso de las aplicaciones
    
    Parameters
    ----------
    datos : lista
         lista, donde cada elemento es un diccionario que contiene un participante

    Returns  
    -------
    type :  float
           teimpo total en el que se usaron todas las aplicaciones

    """
    tiempo_total=0
    for participante in datos: 
       tiempos= participante["tiempo_uso"]
       tiempo_total += sum(tiempos)
    return tiempo_total

def calcular_promedio_uso(datos): 
    """
    Que hace: calcula el tiempo promedio en el que se usan las aplicaciones.

    Parametros: 
    ----------
    datos : lista
        lista, donde cada elemento es un diccionario que contiene un participante

    Returns
    -------
    promedio : float
        promedio de tiempo de uso.
    Raises:
        zerodivisionerror
        si los usos totales son iguales a 0

    """
    tiempo_total= calcular_tiempo_total(datos)
    
    total_usos = 0
    for participante in datos:
        total_usos += sum(participante["cantidad_uso"])
    
    if total_usos == 0:
        raise ZeroDivisionError ("No se puede calcular el promedio")
    promedio= tiempo_total / total_usos
    
    return promedio

def calcular_uso_por_app(datos):
    """
    Que hace la funcion: calcula cuantas veces se utilizo cada app.

    Parametro
    ----------
    datos : lista
        lista , donde cada elemento es un diccionario que contiene un  participante

    Returns
    -------
    TYPE: dict
        Diccionario con la cantidad de usos por aplicación. La clave es la app, el valor la cantidad de usos
    """
    uso_por_app={}
    for participante in datos:
        apps= participante["app"]
        usos= participante["cantidad_uso"]
        for i in range(len(apps)):
            app = apps [i]
            uso=usos [i]
            if app in uso_por_app:        
               uso_por_app[app]  += uso 
            else:
               uso_por_app [app] =uso
    return uso_por_app
            
    
    
        
    
            
     
            
        
    
        