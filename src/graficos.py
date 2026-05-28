# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:56:28 2026

@author: Usuario
"""

import matplotlib.pyplot as plt
def tiempo_por_app_grafico(df):
    '''
    Que hace: crea un grafico de barras del tiempo total de cada aplicacion.

    Parametros
    ----------
    df : Dataframe

    Retorna
    -------
    None porque solo se muestra el grafico y lo guarda

    '''
    metricas_agrupadas = df.groupby('app')['tiempo_uso'].sum()
    plt.figure(figsize=(9, 5))
    metricas_agrupadas.plot(kind='bar', color='#1e3a8a', edgecolor='black', alpha=0.8)

    plt.title('Comparacion del Tiempo total de uso por aplicacion', fontsize=13, fontweight='bold',
    pad=15)
    plt.xlabel('Aplicaciones', fontsize=11)
    plt.ylabel('tiempo de uso', fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5, axis='y')
    plt.tight_layout()
    plt.savefig('graficos/tiempo_por_app.png', dpi=300)
    plt.show()
    plt.close()

    




