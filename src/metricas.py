   #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:39:37 2026

@author: mariaemiliabarbeito
"""

def calcular_tiempo_total(df):
    """
    Que hace la funcion: calcula el tiempo total de uso de las aplicaciones
    
    Parameters
    ----------
    df: Dataframe
         Dataframe validado 

    Returns  
    -------
    tiempo_total :  int
           suma tiempo total en el que se usaron todas las aplicaciones

    """
    tiempo_total= df["tiempo_uso"].sum()
    return tiempo_total

def calcular_promedio_uso(df): 
    """
    Que hace: calcula el tiempo promedio en el que se usan las aplicaciones.

    Parametros: 
    ----------
    df:dataframe
        Dataframe validado 
    Returns
    -------
    promedio : float
        promedio de tiempo de uso.
    Raises:
        zerodivisionerror
        si los usos totales son iguales a 0

    """
    if df["cantidad_uso"].sum()==0:
        raise ZeroDivisionError ("No hay datos, no se puede calcular el promedio")
    promedio_uso= df["cantidad_uso"].mean()
    return promedio_uso


def calcular_uso_por_app(df):
    """
    Que hace la funcion: calcula cuantas veces se utilizo cada app.

    Parametro
    ----------
    df: dataframe
        Dataframe validado 

    Returns
    -------
    uso_por_app: series
             Uso por app
    """
    uso_por_app = df.groupby("app")["cantidad_uso"].sum()
    return uso_por_app
    
            
    
    
        
    
            
     
            
        
    
        