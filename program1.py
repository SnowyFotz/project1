import streamlit as st
import numpy as np
 
st.title("Calculadora Estadística con Pestañas")

# =============================
# 💠 TEMA FUTURISTA ESTILO 2000 💠
# =============================
st.markdown("""
<!-- Fuente futurista geométrica -->
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@300;400;600&display=swap" rel="stylesheet">

<style>

/* ======= FUENTE GLOBAL ======= */
html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
    color: #e6f7ff;
    letter-spacing: 0.5px;
}

/* ======= FONDO GENERAL ======= */
.main {
    background: radial-gradient(circle at 20% 20%, #0a1a24, #000000 80%);
    background-attachment: fixed;
}

/* ======= TITULOS ======= */
h1, h2, h3 {
    color: #4dcfff;
    font-weight: 600;
    text-shadow: 0 0 8px rgba(77, 207, 255, 0.7);
}

/* ======= TEXTOS ======= */
p, label {
    color: #cfeaff !important;
}

/* ======= ÁREA DE TEXTO ======= */
textarea {
    background-color: #07131a !important;
    border: 2px solid #144e66 !important;
    color: #aee6ff !important;
    border-radius: 8px !important;
    padding: 12px !important;
    box-shadow: 0 0 6px rgba(0, 204, 255, 0.25);
}

/* ======= BOTONES ======= */
.stButton>button {
    background: linear-gradient(90deg, #0da2c8, #14c7ff);
    color: #001821;
    border-radius: 6px;
    font-weight: bold;
    border: none;
    padding: 12px 24px;
    text-shadow: 0 0 4px rgba(255,255,255,0.5);
    box-shadow: 0 0 10px rgba(20, 199, 255, 0.4);
}

.stButton>button:hover {
    background: linear-gradient(90deg, #14c7ff, #0da2c8);
    transform: scale(1.03);
    box-shadow: 0 0 14px rgba(20, 199, 255, 0.7);
}

/* ======= PESTAÑAS ======= */
.stTabs [data-baseweb="tab"] {
    font-size: 16px;
    font-weight: bold;
    color: #8bd8ff;
    background-color: #041017;
    border-radius: 6px 6px 0 0;
    border: 1px solid #0f3c52;
    margin-right: 4px;
    padding: 8px 18px;
}

.stTabs [data-baseweb="tab"]:hover {
    color: #d4f4ff;
    background-color: #07202c;
}

.stTabs [aria-selected="true"] {
    background-color: #0a2b3d !important;
    border-bottom: 3px solid #14c7ff !important;
    color: #ffffff !important;
}

/* ======= CAJAS DE RESULTADOS ======= */
div[data-testid="stMetricValue"], .stAlert>div {
    background-color: #04151f;
    border: 1px solid #0e4a63;
    border-radius: 8px;
    padding: 8px 12px;
    color: #c7f2ff !important;
    box-shadow: 0 0 8px rgba(20,199,255,0.3);
}

/* ======= TABLAS ======= */
table {
    background-color: #051a24cc !important;
    border-radius: 8px;
    color: #e1f7ff;
}

/* ======= SCROLLBAR FUTURISTA ======= */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: #0da2c8;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #14c7ff;
}

</style>
""", unsafe_allow_html=True)


# Creamos las pestañas
tab1, tab2, tab3 = st.tabs(["Calculadora", "Estadísticos", "Acerca de"])
 
# --------------------
# PESTAÑA 1: CALCULADORA
# --------------------
with tab1:
    st.header("Calculadora de Datos")
 
    st.write("Ingresa una lista de números separados por comas. Ejemplo:")
    st.code("10, 20, 15, 30, 25")
 
    data_input = st.text_area("Datos:")
 
    if st.button("Cargar datos"):
        try:
            # Convertir texto a lista numérica
            data = [float(x.strip()) for x in data_input.split(",")]
 
            st.success("Datos cargados correctamente.")
            st.write("Tamaño de la muestra:", len(data))
            st.write("Primeros valores:", data[:5])
 
            # Guardamos los datos para usarlos en otras pestañas
            st.session_state["datos"] = data
 
        except:
            st.error("Error: revisa que los datos estén escritos correctamente.")
 
# --------------------
# PESTAÑA 2: ESTADÍSTICOS
# --------------------
with tab2:
    st.header("Resultados Estadísticos")
 
    if "datos" in st.session_state:
        data = st.session_state["datos"]
 
        media = np.mean(data)
        mediana = np.median(data)
        desviacion = np.std(data, ddof=1)
        varianza = np.var(data, ddof=1)
        minimo = np.min(data)
        maximo = np.max(data)
        rango = maximo - minimo
 
        st.write(f"**Media:** {media:.4f}")
        st.write(f"**Mediana:** {mediana:.4f}")
        st.write(f"**Desviación estándar (muestral):** {desviacion:.4f}")
        st.write(f"**Varianza (muestral):** {varianza:.4f}")
        st.write(f"**Mínimo:** {minimo:.4f}")
        st.write(f"**Máximo:** {maximo:.4f}")
        st.write(f"**Rango:** {rango:.4f}")
 
    else:
        st.warning("Primero ingresa los datos en la pestaña 'Calculadora'.")
 
# --------------------
# PESTAÑA 3: ACERCA DE
# --------------------
with tab3:
    st.header("Acerca de la App")
    st.write("""
    Esta app fue creada para practicar el análisis estadístico básico.
 
    **Funciones:**
    - Ingreso de datos numéricos
    - Cálculo de media, mediana, desviación estándar y varianza
    - Cálculo de mínimo, máximo y rango
    - Organización en pestañas (entrada de datos, resultados e información)
    """)
