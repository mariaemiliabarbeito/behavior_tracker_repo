#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:38:23 2026

@author: mariaemiliabarbeito
"""

def validar_registro (registro):
    for datos in registro:
        try:
            id_participante = int(datos["id_participante"]): 
        except:
          raise TypeError("ID invalido")
        if id_participante <0:
          raise ValueError ("ID invalido")
              
        
            
  
            
      
            
            
                
                
            