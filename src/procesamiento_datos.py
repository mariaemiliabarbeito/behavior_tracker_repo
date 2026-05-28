#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:39:04 2026

@author: mariaemiliabarbeito
"""

def filtrar_por_participante(df, id_participante):
    
    '''
    Que hace la funcion: La función obtiene y devuelve los datos de un participante especifico, ignorando los demás.
    
    Parametros:
        df: DataFrame con la informacion de todos los participantes
        id_participante: int
        numero que identifica al participante cuyos datos se quiere obtener 
    
    Retorna:
        df_filtrado: DataFrame
        DataFrame que contiene unicamente los datos del participante filtrado.
        
    Excepciones:
        ValueError si ningun participante coincide con el id ingresado por el usuario.
        ValueError si el id ingresado por el usuario no es un numero mayor a 0.

    '''
    try:
        id_participante = int(id_participante)
    except ValueError:
        raise ValueError("El id ingresado debe ser un numero entero")
    if id_participante <= 0:
        raise ValueError("El id ingresado debe ser un numero mayor a 0")
     
    df_filtrado= df[df["id_participante"]== id_participante]    
    if df_filtrado.empty:
         raise ValueError("No se pudo encontrar al participante")
    return df_filtrado
    
    