#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:39:04 2026

@author: mariaemiliabarbeito
"""

def filtrar_por_participante(datos, id_participante):
    
    '''
    Que hace la funcion: La función obtiene y devuelve los datos de un participante especifico, ignorando los demás.
    
    Parametros:
        datos (list): lista con la informacion de todos los participantes
        id_participante (int): numero que identifica al participante cuyos datos se quiere obtener 
    Retorna:
        datos_participante (list): datos del participante filtrado

    '''
    datos_participante = []
    for registro in datos:     
       if id_participante == registro["id_participante"]:
            datos_participante.append(registro)
    return datos_participante