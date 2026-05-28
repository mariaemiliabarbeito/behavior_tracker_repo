#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:38:23 2026

@author: mariaemiliabarbeito
"""
import pandas as pd
def validar_id_participante (df):
    """
    Que hace la funcion: Valida que la columna id_partcipante no este vacía, que sus valores sean mayores a cero y que sea el tipo de dato correcto 
    
    Parametro
    ----------
    df: Dataframe
        columna "id participante" sin validar

    Raises
    ------
    ValueError
        Verifica que el ID no sea invalido ni este vacío

    Returns
    -------
    df :Dataframe
        la columna id participante validada

    """
    
    if df["id_participante"].isna().any(): 
        raise ValueError (" El ID está vacío")
            
    try:
        df["id_participante"]=df["id_participante"].astype(int)
    except ValueError:
       raise ValueError("El ID es invalido")
       
    if (df["id_participante"] <= 0).any():
       raise ValueError (" El ID  es invalido")
    return df 
          

def validar_fecha (df):
    """
    Que hace la funcion: valida que la columna fecha tenga el formato correcto  y que no esté vacía

    Parametro
    ----------
    df: dataframe
         Dataframe con la columna fecha sin validar

    Raises
    ------
    ValueError
        Verifica que la fecha no sea invalida ni este vacia

    Returns
    -------
    df: dataframe
        Dataframe con la columna fecha validada

    """
    if df["fecha"].isna().any(): 
        raise ValueError ("La fecha esta vacia")

    try:
        pd.to_datetime(df["fecha"], format="%Y/%m/%d") 
    except ValueError:
        raise ValueError ("La fecha no tiene formato valido")
    return df

def validar_app (df):
    """
    Que hace la funcion: valida que la columna app app sea el tipo de dato correcto y que no esté vacía

    Parameteros
    ----------
    df: Dataframe
        Dataframe con la columna "app" sin validar

    Raises
    ------
    ValueError
        Verifica que la app no este vacia
    TypeError
        Verifica que la app no seadel tipo de dato invalido

    Returns
    -------
    df: Dataframe
       Dataframe con la columna app validada

    """
    if df["app"].isna().any(): 
        raise ValueError ("La app esta vacia")
   
    if ["app"].dtype != str:
        raise TypeError ("La app debe ser un string")
    return df

def validar_cantidad_uso (df):
    """
    Que hace la funcion: Valida que la  columna cantidad de uso sea del tipo de dato y tenga el valor correcto y que no este vacia.

    Parametros
    ----------
    df: dataframe
        Dataframe con la columna cantidad uso sin validar
    Raises
    ------   
    ValueError
        Verifica que la cantidad de uso no este vacia ni sea invalida

    Returns
    -------
    df: dataframe
         Dataframe con la  columna cantidad uso validada

    """
    if df["cantidad_uso"].isna().any():
       raise ValueError ("La cantidad de uso está vacía")
    try:
        df["cantidad_uso"]=df["cantidad_uso"].astype(int)
    except ValueError:
       raise ValueError("Cantidad uso invalida")
    if (df["cantidad_uso"]<=0).any():
       raise ValueError ("Cantidad de uso invalida")
    return df

def validar_tiempo_uso (df):
    """
    Que hace la función: valida que la columna" tiempo de uso" sea el tipo de dato correcto, que contenga el valor esperado y que no este vacio

    Parameters
    ----------
    df: dataframe
        Dataframe con la columna tiempo sin validar

    Raises
    ------
    ValueError
        Verifica que el tiempo de uso no este vacío ni sea invalido

    Returns
    -------
    df: dataframe
        dataframe con la columna tiempo validada 

    """
    if df["tiempo"].isna().any():
         raise ValueError ("El tiempo de uso está vacio")
    try:
        df["tiempo"]=df["tiempo"].astype(int)
    except ValueError:
       raise ValueError("Tiempo de uso invalido")
       
    if(df["tiempo"]<=0).any():
       raise ValueError ("Tiempo de uso invalido")

 
def validar_datos(df):
    """
    Que hace la funcion: valida el dataframe

    Parameters
    ----------
    df : dataframe
        Dataframe sin validar. Columnas de id_participante, fecha, app, cantidad_uso, tiempo

    Returns
    -------
    df : dataframe
        Dataframe validado

    """
    df=validar_id_participante(df)
    df= validar_fecha (df)
    df= validar_app (df)
    df= validar_cantidad_uso (df)
    df= validar_tiempo_uso(df)
    
    return df
    
        
              
        
            
  
            
      
            
            
                
                
            