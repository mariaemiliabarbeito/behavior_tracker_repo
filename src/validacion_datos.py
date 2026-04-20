#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:38:23 2026

@author: mariaemiliabarbeito
"""

def validar_id_participante (id_participante):
    """
    Que hace la funcion: Valida que el id sea del tipo de dato y tenga el valor correcto. Tambien valida que no esté vacía
    
    Parametro
    ----------
    id_participante : str
        Id del participante sin validar en formato string

    Raises
    ------
    ValueError
        Verifica que el ID no sea invalido ni este vacío

    Returns
    -------
    id_participante : int
        Id del participante validado en formato int

    """
    
    if id_participante == "":
        raise ValueError (" El ID está vacío")
            
    try:
         id_participante=int(id_participante)
    except ValueError:
       raise ValueError("El ID es invalido")
       
    if id_participante <= 0:
       raise ValueError (" El ID  es invalido")
       
    return id_participante
          
from datetime import datetime
def validar_fecha (fecha):
    """
    Que hace la funcion: valida que la fecha tenga el formato correcto  y que no esté vacía

    Parametro
    ----------
    fecha : str
        La fecha del participante sin validar en formato string

    Raises
    ------
    ValueError
        Verifica que la fecha no sea invalida ni este vacia

    Returns
    -------
    fecha : str
        Fecha validada en formato string

    """
    if fecha == "":
       raise ValueError ("La fecha está vacía")
    #try:
   #     fecha=str(fecha)
   # except ValueError:
   #     raise ValueError("Fecha invalida")
    try:
        datetime.strptime(fecha,"%Y-%m-%d")
    except ValueError:
        raise ValueError ("La fecha no tiene formato valido")
    return fecha

def validar_app (app):
    """
    Que hace la funcion: valida que la app sea el tipo de dato correcto y que no esté vacía

    Parameteros
    ----------
    app : str
        La app sin validar en formato string

    Raises
    ------
    ValueError
        Verifica que la app no este vacia
    TypeError
        Verifica que la app no seadel tipo de dato invalido

    Returns
    -------
    app : str
       App validada en formato string

    """
    
    if app == "" :
      raise ValueError("La app está vacía")
      
    if not isinstance (app, str):
        raise TypeError ("La app debe ser un string")
    return app

def validar_cantidad_uso (cantidad_uso):
    """
    Que hace la funcion: Valida que la cantidad de uso sea del tipo de dato y tenga el valor correcto y que no este vacia.

    Parametros
    ----------
    cantidad_uso: str
        La cantidad de uso sin validar en formato string

    Raises
    ------   
    ValueError
        Verifica que la cantidad de uso no este vacia ni sea invalida

    Returns
    -------
    uso : int
        Cantidad de uso validada en formato int

    """
    if cantidad_uso  == "":
       return ValueError ("La cantidad de uso está vacía")
    try:
         cantidad_uso=int(cantidad_uso)
    except ValueError:
       raise ValueError("Cantidad uso invalida")
    if cantidad_uso <= 0:
       raise ValueError ("Cantidad de uso invalida")
    return cantidad_uso

def validar_tiempo_uso (tiempo):
    """
    Que hace la función: valida que el tiempo de uso sea el tipo de dato correcto, que contenga el valor esperado y que no este vacio

    Parameters
    ----------
    tiempo : str
        El tiempo de uso sin validar en formato string

    Raises
    ------
    ValueError
        Verifica que el tiempo de uso no este vacío ni sea invalido

    Returns
    -------
    tiempo : int
        Tiempo uso en formato int

    """
    if  tiempo == "":
         raise ValueError ("El tiempo de uso está vacio")
    try:
         tiempo=int(tiempo)
    except ValueError:
       raise ValueError("Tiempo de uso invalido")
    if tiempo<= 0:
       raise ValueError ("Tiempo de uso invalido")
    return tiempo
 
def validar_datos(registro):
    id_participante=validar_id_participante(registro[0])
    fecha= validar_fecha (registro[1])
    app= validar_app (registro[2])
    cantidad_uso= validar_cantidad_uso (registro[3])
    tiempo= validar_tiempo_uso(registro[4])
    
    return [id_participante, fecha, app, cantidad_uso, tiempo]
    
        
              
        
            
  
            
      
            
            
                
                
            