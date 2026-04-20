#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:38:23 2026

@author: mariaemiliabarbeito
"""

def validar_id_participante (registro):
    id_participante = registro["id_participante"]
    if id_participante not in registro:
        raise KeyError("Falta la clave id_participante")
        if id_participante == []:
            return None
    try:
         id_participante=int(id_participante)
    except ValueError:
       raise ValueError("ID invalido")
    if id_participante <= 0:
       raise ValueError ("ID invalido")
    return id_participante
          
from datetime import datetime
def validar_fecha (registro):
    fecha = registro["fecha"]
    if "fecha" not in registro:
        raise KeyError("Falta la fecha")
        if fecha == []:
            return None  
    try:
        fecha=str(fecha)
    except ValueError:
        raise ValueError("Fecha invalida")
    try:
        datetime.strptime(fecha,"%Y-%m-%d")
    except ValueError:
        raise ValueError ("La fecha no tiene formato valido")
    return fecha

def validar_app (registro):
    app = registro["app"]
    if app not in registro:
        raise KeyError("Falta la app")
        if app == []:
            return None
    try:
         app =str(app)
    except ValueError:
       raise ValueError("App invalida")
    return app

def cantidad_uso (registro):
    uso = registro["cantidad_uso"]
    if uso not in registro:
        raise KeyError("No esta la cantidad de uso de la app")
        if uso  == []:
            return None
    try:
         uso=int(uso)
    except ValueError:
       raise ValueError("Cantidad uso invalida")
    if uso <= 0:
       raise ValueError ("Cantidad de uso invalida")
    return uso

def tiempo_uso (registro):
    tiempos= registro["tiempo_uso"]
    if  tiempos not in registro:
        raise KeyError("Falta el tiempo de uso de la app")
        if  tiempos == []:
            return None
    try:
         tiempos=int(tiempos)
    except ValueError:
       raise ValueError("Tiempo de uso invalido")
    if tiempos <= 0:
       raise ValueError ("tiempo de uso invalido")
    return tiempos
 
    
    
        
              
        
            
  
            
      
            
            
                
                
            