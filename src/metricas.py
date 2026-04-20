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
        return {}
    tiempo_por_app={}
    for dato in datos:
        apps= dato["app"]
        tiempos= dato["tiempo_uso"]
        for i in range(len(apps)):
            app = apps [i]
            tiempo=tiempos [i]
            if app in tiempo_por_app:         #duda
                tiempo_por_app[app] += tiempo #duda
            else:                              
                tiempo_por_app[app]= tiempo
    return tiempo_por_app   
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
    tiempos=calcular_tiempo_total(datos)
    valores= tiempos.values()
    total= sum(valores)
    cantidad=0
    for dato in datos: #promedio total no promedio por app
        cantidad += len(dato["app"])
    promedio= total/cantidad
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
            
    
    
        
    
            
     
            
        
    
        