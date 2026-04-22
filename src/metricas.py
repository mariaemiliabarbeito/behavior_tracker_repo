   #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:39:37 2026

@author: mariaemiliabarbeito
"""

def calcular_tiempo_total(datos):
    """
    Que hace la funcion:
    
    Parameters
    ----------
    datos : TYPE
        DESCRIPTIO

    Returns  
    -------
    TYPE
        DESCRIPTION.

    """
    if datos==[]:
        raise ValueError ("La lista se encuentra vacía por lo tanto el tiempo total no se encuentra")
    tiempo_por_app={}
    for dato in datos:
        lista_apps= dato["app"]
        tiempos= dato["tiempo_uso"]
        for i in range(len(lista_apps)):
            app =lista_apps [i]
            tiempo=tiempos [i]
            if app in tiempo_por_app:         
                tiempo_por_app[app] += tiempo  
            else:                              
                tiempo_por_app[app]= tiempo
    tiempo_total = sum(tiempo_por_app.values())            
    return tiempo_por_app,tiempo_total   
def calcular_promedio_uso(datos): 
    """
    Que hace: calcula el promedio del tiempo que se usan las aplicaciones.

    Parametros: 
    ----------
    datos : lista
        lista, donde cada elemento es un diccionario que contiene el registro de un participante.

    Returns
    -------
    promedio : float
        promedio de tiempo de uso.

    """
    resultado= calcular_tiempo_total(datos)
    
    tiempo_total= resultado[1]
    
    total_usos = 0
    for dato in datos:
        total_usos += sum(dato["cantidad_uso"])
    
    promedio= tiempo_total / total_usos
    return promedio

def calcular_uso_por_app(datos):
    """
    

    Parameters
    ----------
    datos : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if datos==[]:
        return {}
    uso_por_app={}
    for dato in datos:
        apps= dato["app"]
        usos= dato["cantidad_uso"]
        for i in range(len(apps)):
            app = apps [i]
            uso=usos [i]
            if app in uso_por_app:        #duda
               uso_por_app[app]  += uso #duda
            else:
               uso_por_app [app] =uso
    return uso_por_app
            
    
    
        
    
            
     
            
        
    
        