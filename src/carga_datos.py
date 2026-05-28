#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:36:07 2026

@author: mariaemiliabarbeito
"""
import pandas as pd
import os

def cargar_datos(ruta_csv):
    """
    Que hace la funcion: 
        Lee un archivo CSV con Pandas y devuelve un DataFrame.

    Parametros: 
    ruta_csv : str
        Ruta del archivo que se quiere leer

    Retorna:
    DataFrame 
    tabla con los datos de cada participante.
    
    Excepciones:
        FileNotFoundError: si el archivo no existe.

    """
    if not os.path.exists(ruta_csv):
        raise FileNotFoundError(f'No se encontró el archivo en la ruta: {ruta_csv}')
    df = pd.read_csv(ruta_csv)
    
    return df

    
