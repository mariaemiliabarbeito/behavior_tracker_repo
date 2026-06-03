#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:41:30 2026

@author: mariaemiliabarbeito
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# =============================================================================
# from src.validacion_datos import validar_datos
# =============================================================================
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app

# Configuracion de la pagina 
st.set_page_config(
    page_title="BehaviorTracker",
    page_icon="📱",
    layout="wide"
)

# Asegurar que exista la carpeta de graficos
os.makedirs("graficos", exist_ok=True)

# Titulo principal
st.title("📱 BehaviorTracker — Análisis de Uso Digital")
st.markdown("Sistema de análisis de patrones de comportamiento digital a lo largo del tiempo.")
st.divider()

# ── 1. CARGA DINAMICA DE DATOS ─────────────────────────────────────────────────
st.header("1. Carga de datos")
archivo = st.file_uploader(
    "Arrastrá y soltá el archivo CSV de BehaviorTracker",
    type="csv",
    help="Columnas esperadas: id_participante, fecha, app, cantidad_uso, tiempo_uso"
)

if archivo is None:
    st.info("👆 Subí un archivo CSV para comenzar el análisis.")
    st.stop()

try:
    # El CSV no tiene encabezado: se asignan los nombres de columna manualmente
    df = pd.read_csv(
        archivo,
        header=None,
        names=["id_participante", "fecha", "app", "cantidad_uso", "tiempo_uso"]
    )
except Exception as e:
    st.error(f"❌ No se pudo leer el archivo: {e}")
    st.stop()

# ── 2. VALIDACION DEFENSIVA ────────────────────────────────────────────────────
st.header("2. Validación de datos")

try:
    df = validar_datos(df)
    st.success("✅ Archivo válido. Todos los datos pasaron las validaciones.")
except (ValueError, TypeError) as e:
    st.error(f"❌ Error en los datos: {e}")
    st.stop()
except Exception as e:
    st.error(f"❌ Error inesperado durante la validación: {e}")
    st.stop()

with st.expander("📋 Vista previa de los datos cargados"):
    st.dataframe(df.head(10), use_container_width=True)
    st.caption(f"Total de registros: {len(df)} | Participantes: {df['id_participante'].nunique()}")

st.divider()

# ── 3. SELECTOR DE PARTICIPANTE ────────────────────────────────────────────────
st.header("3. Selección de participante")

# Los valores del selectbox son int (vienen directo del DataFrame ya validado)
# filtrar_por_participante recibe str o int y convierte internamente a int
participantes_disponibles = sorted(df["id_participante"].unique().tolist())
id_seleccionado = st.selectbox(
    "Seleccioná el ID del participante a analizar:",
    options=participantes_disponibles,
    format_func=lambda x: f"Participante {x}"
)

try:
    df_filtrado = filtrar_por_participante(df, id_seleccionado)
except ValueError as e:
    st.error(f"❌ {e}")
    st.stop()

st.success(f"Mostrando análisis para el **Participante {id_seleccionado}** — {len(df_filtrado)} registros encontrados.")
st.divider()

# ── 4. KPIs ────────────────────────────────────────────────────────────────────
st.header("4. Indicadores clave (KPIs)")

try:
    tiempo_total_general   = int(df_filtrado["tiempo_uso"].sum())
    cantidad_total_general = int(df_filtrado["cantidad_uso"].sum())
    apps_usadas            = df_filtrado["app"].nunique()
    dias_registrados       = df_filtrado["fecha"].nunique()
    promedio_tiempo_dia    = round(tiempo_total_general / dias_registrados, 1) if dias_registrados > 0 else 0

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("⏱️ Tiempo total (min)", tiempo_total_general)
    col2.metric("📲 Aperturas totales", cantidad_total_general)
    col3.metric("📱 Apps distintas", apps_usadas)
    col4.metric("📅 Días registrados", dias_registrados)
    col5.metric("⏱️ Prom. por día (min)", promedio_tiempo_dia)

except Exception as e:
    st.error(f"❌ Error al calcular KPIs: {e}")

st.divider()

# ── 5. METRICAS DETALLADAS ─────────────────────────────────────────────────────
st.header("5. Métricas detalladas")

try:
    tiempo_por_app   = calcular_tiempo_total(df_filtrado, "app")
    tiempo_por_fecha = calcular_tiempo_total(df_filtrado, "fecha")
    promedio_por_app = calcular_promedio_uso(df_filtrado, "app")
    uso_por_app      = calcular_uso_por_app(df_filtrado, "app")

    col_izq, col_der = st.columns(2)

    with col_izq:
        st.subheader("Tiempo total por app (min)")
        st.dataframe(
            tiempo_por_app.reset_index().rename(
                columns={"tiempo_uso": "Tiempo total (min)", "app": "App"}
            ),
            use_container_width=True, hide_index=True
        )
        st.subheader("Promedio de aperturas por app")
        st.dataframe(
            promedio_por_app.reset_index().rename(
                columns={"cantidad_uso": "Promedio aperturas", "app": "App"}
            ),
            use_container_width=True, hide_index=True
        )

    with col_der:
        st.subheader("Tiempo de uso por fecha (min)")
        st.dataframe(
            tiempo_por_fecha.reset_index().rename(
                columns={"tiempo_uso": "Tiempo total (min)", "fecha": "Fecha"}
            ),
            use_container_width=True, hide_index=True
        )
        st.subheader("Aperturas totales por app")
        st.dataframe(
            uso_por_app.reset_index().rename(
                columns={"cantidad_uso": "Total aperturas", "app": "App"}
            ),
            use_container_width=True, hide_index=True
        )

except ZeroDivisionError as e:
    st.error(f"❌ Sin datos suficientes para calcular métricas: {e}")
    st.stop()
except Exception as e:
    st.error(f"❌ Error al calcular métricas: {e}")
    st.stop()

st.divider()

# ── 6. VISUALIZACIONES ─────────────────────────────────────────────────────────
st.header("6. Visualizaciones")

col_g1, col_g2 = st.columns(2)

# Grafico 1: Barras — Tiempo total por app
with col_g1:
    st.subheader("⏱️ Tiempo total por app")
    try:
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        tiempo_por_app.plot(kind="bar", ax=ax1, color="#1e3a8a", edgecolor="black", alpha=0.85)
        ax1.set_title(
            f"Tiempo total por app — Participante {id_seleccionado}",
            fontsize=11, fontweight="bold", pad=10
        )
        ax1.set_xlabel("Aplicación", fontsize=10)
        ax1.set_ylabel("Tiempo (minutos)", fontsize=10)
        ax1.tick_params(axis="x", rotation=30)
        ax1.grid(True, linestyle="--", alpha=0.5, axis="y")
        plt.tight_layout()
        fig1.savefig(f"graficos/tiempo_por_app_p{id_seleccionado}.png", dpi=300)
        st.pyplot(fig1)
        plt.close(fig1)
    except Exception as e:
        st.error(f"❌ Error al generar gráfico de barras: {e}")

# Grafico 2: Lineas — Tiempo por fecha
with col_g2:
    st.subheader("📅 Tiempo de uso por fecha")
    try:
        df_tf = tiempo_por_fecha.reset_index()
        # Convertir a datetime para ordenar correctamente las fechas
        df_tf["fecha_dt"] = pd.to_datetime(df_tf["fecha"], format="%d/%m/%Y")
        df_tf = df_tf.sort_values("fecha_dt")

        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.plot(
            df_tf["fecha_dt"],
            df_tf["tiempo_uso"],
            color="#b45309", linewidth=2, marker="o", markersize=5
        )
        ax2.set_title(
            f"Tiempo de uso por fecha — Participante {id_seleccionado}",
            fontsize=11, fontweight="bold", pad=10
        )
        ax2.set_xlabel("Fecha", fontsize=10)
        ax2.set_ylabel("Tiempo (minutos)", fontsize=10)
        ax2.tick_params(axis="x", rotation=30)
        ax2.grid(True, linestyle=":", alpha=0.6)
        plt.tight_layout()
        fig2.savefig(f"graficos/tiempo_por_fecha_p{id_seleccionado}.png", dpi=300)
        st.pyplot(fig2)
        plt.close(fig2)
    except Exception as e:
        st.error(f"❌ Error al generar gráfico de líneas: {e}")

# Grafico 3 (ancho completo): Boxplot de aperturas por app
st.subheader("📊 Distribución de aperturas por app")
try:
    apps_presentes = df_filtrado["app"].unique().tolist()
    data_boxplot = [
        df_filtrado[df_filtrado["app"] == app]["cantidad_uso"].values
        for app in apps_presentes
    ]

    fig3, ax3 = plt.subplots(figsize=(9, 4))
    ax3.boxplot(
        data_boxplot,
        labels=apps_presentes,
        patch_artist=True,
        boxprops=dict(facecolor="#cbd5e1", color="#0f172a"),
        medianprops=dict(color="#1e3a8a", linewidth=2)
    )
    ax3.set_title(
        f"Distribución de aperturas por app — Participante {id_seleccionado}",
        fontsize=11, fontweight="bold", pad=10
    )
    ax3.set_ylabel("Cantidad de aperturas", fontsize=10)
    ax3.grid(True, linestyle="--", alpha=0.4, axis="y")
    plt.tight_layout()
    fig3.savefig(f"graficos/distribucion_p{id_seleccionado}.png", dpi=300)
    st.pyplot(fig3)
    plt.close(fig3)
except Exception as e:
    st.error(f"❌ Error al generar boxplot: {e}")

st.caption("Los gráficos se guardan automáticamente en la carpeta `graficos/`.")