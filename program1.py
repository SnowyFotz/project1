import streamlit as st
import numpy as np
 
st.title("Calculadora Estadística con Pestañas")

# =============================
# 🎀 TEMA PASTEL KAWAII STREAMLIT 🎀
# =============================
st.markdown("""
<!-- Google Font kawaii -->
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;600&display=swap" rel="stylesheet">

<style>

/* ======= FUENTE GLOBAL ======= */
html, body, [class*="css"]  {
    font-family: 'Quicksand', sans-serif;
    font-size: 17px;
    color: #555;
}

/* ======= FONDO GENERAL ======= */
.main {
    background: linear-gradient(135deg, #ffe8f0, #e5f6ff, #fff7d9);
    background-size: 400% 400%;
    animation: pastelFlow 12s ease infinite;
}

@keyframes pastelFlow {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ======= TITULOS ======= */
h1, h2, h3 {
    color: #ff8ac7;
    text-shadow: 0px 0px 4px rgba(255, 182, 219, 0.6);
    font-weight: 600;
}

/* ======= TEXTOS ======= */
p, label {
    color: #6b6b6b !important;
}

/* ======= AREA DE TEXTO ======= */
textarea {
    background-color: #ffffffcc !important;
    border: 2px solid #ffd2e8 !important;
    border-radius: 12px !important;
    padding: 10px !important;
}

/* ======= BOTONES ======= */
.stButton>button {
    background: linear-gradient(90deg, #ffb3d9, #ffcce7);
    color: #ffffff;
    border-radius: 12px;
    padding: 12px 22px;
    font-size: 16px;
    border: none;
    box-shadow: 0px 4px 8px rgba(255, 170, 200, 0.4);
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #ffa3cf, #ffbde0);
    transform: scale(1.02);
}

/* ======= PESTAÑAS ======= */
.stTabs [data-baseweb="tab"] {
    font-size: 17px;
    font-weight: bold;
    color: #ff8ac7;
    background-color: #ffeaf4;
    border-radius: 12px 12px 0 0;
    padding: 10px 20px;
    margin-right: 5px;
    border: 2px solid #ffd6e9;
}

.stTabs [data-baseweb="tab"]:hover {
    background-color: #ffd6ee;
    color: #ff6db9;
}

.stTabs [aria-selected="true"] {
    background-color: #ffcde6 !important;
    border-bottom: 3px solid #ff8ac7 !important;
}

/* ======= CAJAS DE RESULTADOS ======= */
div[data-testid="stMetricValue"], .stAlert>div {
    background-color: #fff3fa;
    padding: 10px 14px;
    border-radius: 12px;
    border: 2px solid #ffd7ef;
}

/* ======= TABLAS ======= */
table {
    background-color: #ffffffdd !important;
    border-radius: 10px;
}

/* ======= SCROLLBAR KAWAII ======= */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: #ffbde0;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #ff9fd1;
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
