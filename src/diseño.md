\#!/usr/bin/env python3

# \-*- coding: utf-8 -*-

"""
Created on Wed Jun  3 11:38:45 2026

@author: mariaemiliabarbeito
"""



Diseño del sistema — BehaviorTracker

Objetivo del programa

El programa analiza el comportamiento de usuarios en el uso de aplicaciones móviles. Lee un archivo CSV con registros de uso, valida los datos, filtra por participante y calcula métricas de uso.



Inputs

El archivo CSV no tiene encabezado. Las columnas son:

\- id\_participante: número entero positivo 

\- fecha: formato DD/MM/YYYY

\- app: puede ser instagram, whatsapp, youtube o tiktok

\- cantidad\_uso: número entero positivo, cuántas veces se abrió la app

\- tiempo\_uso: número entero positivo, minutos de uso.



Outputs

\- Tiempo total de uso por app

\- Tiempo total de uso por fecha

\- Promedio de cantidad de uso por app

\- Total de aperturas por app

\- Gráfico de barras con el tiempo por app

\- Gráfico de líneas con el tiempo por fecha



Procesos principales



1\. Se lee el CSV con pandas y se asignan los nombres de columna

2\. Se validan todos los datos

3\. El usuario elige un participante

4\. Se filtran los datos de ese participante

5\. Se calculan las métricas

6\. Se muestran los resultados y gráficos



en src/



\- cargar\_datos.py → función cargar\_datos(ruta\_csv): lee el CSV y devuelve un DataFrame

\- validacion\_datos.py → función validar\_datos(df): valida todas las columnas

\- procesamiento\_datos.py → función filtrar\_por\_participante(df, id\_participante): filtra por participante, recibe el id como string y lo convierte a int internamente

\- metricas.py → funciones calcular\_tiempo\_total(df, condicion), calcular\_promedio\_uso(df, condicion), calcular\_uso\_por\_app(df, condicion)

\- graficos.py → funciones tiempo\_por\_app\_grafico(serie) y grafico\_tiempo\_uso\_por\_fecha(serie)



Errores posibles

\- Archivo no encontrado → FileNotFoundError en cargar\_datos

\- ID negativo o vacío → ValueError en validar\_id\_participante

\- Fecha con formato incorrecto → ValueError en validar\_fecha

\- App que no está en la lista → ValueError en validar\_app

\- cantidad\_uso o tiempo\_uso negativos o vacíos → ValueError

\- tiempo\_uso mayor a 1440 → ValueError

\- Campo vacío → ValueError en cualquier validación

\- Fila con datos corruptos → ValueError

\- Participante no encontrado → ValueError en filtrar\_por\_participante

\- Sin datos para calcular promedio → ZeroDivisionError



Criterios de calidad



\- Ningún error debe cortar el programa sin mensaje claro

\- Las validaciones no usan for, usan operaciones de pandas

\- Cada función hace una sola cosa

\- app.py no repite lógica de src/, solo la usa

\- Los gráficos se guardan en graficos/ 







se espera que la interfaz sea:

La aplicación debe desarrollarse con Streamlit.

Debe reutilizar solo las funciones existentes en src/.

La interfaz debe permitir:



1\. Cargar un archivo CSV.

2\. Mostrar una vista previa de los datos.

3\. Seleccionar un participante desde un desplegable.

4\. Mostrar métricas calculadas para ese participante.

5\. Mostrar gráficos.

6\. Mostrar mensajes de error claros.

