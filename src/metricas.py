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
        DESCRIPTION.

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
            if app in tiempo_por_app:         #duda
                tiempo_por_app[app] += tiempo  
            else:                              
                tiempo_por_app[app]= tiempo
    tiempo_total=sum(tiempo_por_app.values())            
    return tiempo_por_app,tiempo_total   
def calcular_promedio_uso(datos): 
    """
    

    Parameters
    ----------
    datos : TYPE
        DESCRIPTION.

    Returns
    -------
    promedio : TYPE
        DESCRIPTION.

    """
    resultado= calcular_tiempo_total(datos)
    tiempo_por_app= resultado[0]
    tiempo_total= resultado[1]
    
    promedio= tiempo_total/ len(tiempo_por_app)
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
            
    
    
        
    
            
     
            
        
    
        