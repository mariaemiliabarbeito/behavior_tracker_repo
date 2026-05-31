# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:56:28 2026

@author: Usuario
"""

import matplotlib.pyplot as plt
def tiempo_por_app_grafico(df_tiempo_total):
    '''
    Que hace: crea un grafico de barras del tiempo total de cada aplicacion.

    Parametros
    ----------
    df : Dataframe

    Retorna
    -------
    None porque solo se muestra el grafico y lo guarda

    '''
    
    plt.figure(figsize=(9, 5))
    df_tiempo_total.plot(kind='bar', color='#1e3a8a', edgecolor='black', alpha=0.8)

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

def grafico_tiempo_uso_por_fecha(df_tiempo_total):
    """
    que hace la funcion: Crea un grafico de lineas en el que mustra el tiempo de uso segun las fechas, a lo largo del tiempo.
    Parameters
    ----------
    df :Dataframe
       Dataframe validado 

    Returns
    -------
    None.
        Muestra el grafico y lo guarda

    """
    plt.figure(figsize=(11, 5))

    df_tiempo_total.plot(kind='line', x='fecha', y='tiempo_uso', color='#b45309', linewidth=1.5, ax=plt.gca())

    plt.title('Tiempo de uso a lo largo del tiempo', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Fecha', fontsize=11)
    plt.ylabel('Tiempo uso (min)', fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()

    plt.savefig('graficos/tiempo_uso_por_fecha.png', dpi=300)
    plt.show()
    plt.close()

    




