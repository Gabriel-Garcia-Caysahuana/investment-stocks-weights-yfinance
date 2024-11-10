import streamlit as st

st.title("Plataforma de Análisis de Inversiones Bursátiles")
st.write("Bienvenido a la página principal. Utiliza el menú en la barra lateral para navegar por la aplicación.")

st.write("""
Esta aplicación está diseñada para proporcionar un análisis profundo de acciones bursátiles, permitiendo a los inversionistas evaluar el rendimiento histórico, medir el riesgo y optimizar la distribución de activos en su portafolio. A continuación, se explican las principales funcionalidades de la plataforma y los conceptos en los que se basa:
""")

st.subheader("Funcionalidades Principales")

st.markdown("### Descarga de Datos Históricos de Precios de Acciones")
st.write("""
La plataforma permite descargar datos históricos de precios ajustados de múltiples acciones en un rango de fechas definido por el usuario. Estos datos son la base para el análisis del rendimiento y la optimización del portafolio.
""")

st.markdown("### Cálculo de Rendimiento Diario")
st.write("""
Se calcula el rendimiento logarítmico diario de cada acción, que representa la variación porcentual de un día al siguiente. Este cálculo ayuda a visualizar el desempeño de las acciones en el corto plazo, capturando sus ganancias y pérdidas diarias.
""")

st.markdown("### Análisis Estadístico Descriptivo")
st.write("""
La plataforma genera estadísticas descriptivas clave, como la media, desviación estándar, valores máximos y mínimos, para ayudar al usuario a comprender la distribución y el comportamiento histórico de los precios y retornos. Esto es esencial para evaluar el riesgo y la estabilidad de cada acción.
""")

st.markdown("### Visualización de Series Temporales y Análisis de Volatilidad")
st.write("""
- **Gráfico de Series Temporales**: Muestra la evolución del precio ajustado de las acciones a lo largo del tiempo, permitiendo identificar tendencias, patrones de crecimiento o declive, y periodos de alta volatilidad.
- **Gráfico de Caja (Box Plot)**: Visualiza la variabilidad y dispersión de los retornos de cada acción. Este tipo de gráfico es útil para evaluar la volatilidad y comparar el riesgo entre diferentes activos.
""")

st.markdown("### Optimización de Portafolio")
st.write("""
La plataforma permite calcular una distribución óptima de inversión entre las acciones seleccionadas, con el objetivo de maximizar la rentabilidad ajustada al riesgo. Esto se logra mediante la optimización de la relación de Sharpe, un indicador financiero que mide el rendimiento del portafolio en función de su riesgo. Esta funcionalidad ayuda a los inversionistas a decidir cómo distribuir su capital para obtener el mejor rendimiento posible con un nivel de riesgo controlado.
""")

st.subheader("¿Por qué usar esta aplicación?")
st.write("""
Esta herramienta de análisis es ideal para inversionistas interesados en evaluar y optimizar su portafolio de una manera visual e intuitiva. Con sus capacidades de descarga de datos, análisis estadístico, visualización de tendencias y optimización, la plataforma ofrece una solución integral para tomar decisiones informadas en el mercado bursátil.
""")

st.write("""
**Nota**: Esta herramienta es educativa y no constituye asesoramiento financiero. Recomendamos consultar a un asesor financiero antes de tomar decisiones de inversión.
""")

st.sidebar.title("Acerca de")
st.sidebar.info("""
👨‍💻 **Desarrollado por:** Gabriel García Caysahuana 
                
📧 **Contacto:** Proximamente
                
🌐 **GitHub:** [GabrielGarcía](https://github.com/Gabriel-Garcia-Caysahuana)  
                
🔗 **LinkedIn:** [Gabriel García Caysahuana](https://www.linkedin.com/in/gabriel-garcia-caysahuana/)

Esta aplicación fue desarrollada para ayudar a los inversionistas a analizar 
y optimizar su portafolio de acciones. Si tienes alguna pregunta o sugerencia,
¡no dudes en ponerte en contacto!
""")

# streamlit run streamlit_app/Introducción.py
# investment-stocks-weights-yfinance-dvmcrmspcqjqg7r2sblyhh

