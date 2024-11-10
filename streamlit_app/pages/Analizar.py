import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
###########################################################################
from common.downloader import downloader_data
from common.analyse_data import (
    add_performance, descriptive, get_fig_plot_line_series, get_fig_plot_box_plot
)
from common.calculate_weight import calculate_mu_sigma, calculate_weight
from common.to_generate_word import generar_informe
from common.to_generate_excel import generar_excel
#####################################################################
import streamlit as st
import pandas as pd
import io

# Título e introducción
st.title("Análisis de Inversión Bursátil")
st.write("""
    Puede consultar los símbolos de las acciones en:
    [Yahoo Finance](https://finance.yahoo.com/lookup/) o 
    [Nasdaq Symbol Directory](https://www.nasdaq.com/market-activity/stocks/screener)
""")

# Configuración inicial de sesión
for key in ["data", "tickers_list", "weights"]:
    if key not in st.session_state:
        st.session_state[key] = None

# Entrada de datos del usuario
tickers = st.text_input("Ingrese los símbolos (tickers) separados por comas (ejemplo: MSFT, TSLA, NVDA)")
date_start = st.date_input("Fecha de inicio")
date_end = st.date_input("Fecha de fin")
tickers_list = [ticker.strip().upper() for ticker in tickers.split(",") if ticker]

# Botón de análisis
if st.button("Analizar"):
    # Validación para asegurar que hay al menos dos tickers
    if len(tickers_list) < 2:
        st.warning("Por favor, ingrese al menos dos símbolos de ticker para realizar el análisis.")
    else:
        st.write("Descargando datos...")
        try:
            data = downloader_data(tickers_list, date_start, date_end)
            data = add_performance(data, tickers_list)

            if data.empty:
                st.error("No se pudieron descargar datos para los tickers especificados.")
            else:
                st.session_state.update({"data": data, "tickers_list": tickers_list})
                mu, sigma = calculate_mu_sigma(data, tickers_list)
                st.session_state["weights"] = calculate_weight(mu, sigma)

                # Mostrar estadísticas descriptivas
                st.subheader("Estadísticas Descriptivas")
                st.table(descriptive(data))

        except Exception as e:
            st.error(f"Error al descargar o procesar los datos: {e}")

# Visualización de gráficos y tablas
data, tickers_list = st.session_state["data"], st.session_state["tickers_list"]
if data is not None and tickers_list:
    st.subheader("Generar Gráficos")
    grafico = st.selectbox("Escoja el tipo de gráfico que desea visualizar", ["Series Temporales", "Box Plot"])

    # Mostrar gráficos según selección
    if grafico == "Series Temporales":
        st.write("Gráfico de Series Temporales")
        st.pyplot(get_fig_plot_line_series(data, tickers_list))
    elif grafico == "Box Plot":
        st.write("Gráfico de Box Plot")
        st.pyplot(get_fig_plot_box_plot(data, tickers_list))

    # Mostrar peso óptimo
    if st.session_state["weights"] is not None:
        st.subheader("Peso Óptimo")
        weights_df = pd.DataFrame(st.session_state["weights"].items(), columns=["Ticker", "Peso Óptimo"])
        st.table(weights_df)
    else:
        st.warning("Por favor, realice el análisis primero para calcular los pesos óptimos.")

    # Descarga de informes
    st.subheader("Generar y Descargar Informe en Word")
    if st.button("Generar Word"):
        with io.BytesIO() as word_buffer:
            generar_informe(data, tickers_list, st.session_state["weights"], output=word_buffer)
            word_buffer.seek(0)
            st.download_button(
                label="Descargar",
                data=word_buffer,
                file_name="informe_analisis_inversion.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

    st.subheader("Generar y Descargar Datos en Excel")
    if st.button("Generar Excel"):
        with io.BytesIO() as excel_buffer:
            generar_excel(data, output=excel_buffer)
            excel_buffer.seek(0)
            st.download_button(
                label="Descargar",
                data=excel_buffer,
                file_name="data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

