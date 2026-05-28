# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:56:28 2026

@author: Usuario
"""
import matplotlib.pyplot as plt
metricas_agrupadas = df.groupby('columna_categoria')['metrica_numerica'].mean()
plt.figure(figsize=(9, 5))
metricas_agrupadas.plot(kind='bar', color='#1e3a8a', edgecolor='black', alpha=0.8)
# 3. Personalización del estándar científico
plt.title('Comparación de Métricas por Condición Experimental', fontsize=13, fontweight='bold',
pad=15)
plt.xlabel('Condición / Fase', fontsize=11)