import streamlit as st
import numpy as np
 
st.title("Calculadora Estadística con Pestañas")

# =============================
# 💠 ULTRA TEMA FUTURISTA 2000 💠
# Hologramas, vidrio, burbujas, HUD y animaciones
# =============================
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Audiowide&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Sarpanch:wght@700&display=swap" rel="stylesheet">



<style>

/* ============ FUENTE GLOBAL ============ */
html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
    color: #dff6ff;
    letter-spacing: 0.6px;
}

/* ============ FONDO ANIMADO FUTURISTA (Vidrio + burbujas Frutiger Aero 2000) ============ */
.main {
    background: linear-gradient(135deg, rgba(0,40,60,0.9), rgba(0,0,20,0.95)),
                url('https://i.imgur.com/rK8eX9Y.png'); /* textura burbujas vidrio */
    background-size: cover;
    animation: bgPulse 12s ease-in-out infinite;
}

@keyframes bgPulse {
    0% { filter: brightness(0.90); }
    50% { filter: brightness(1.06); }
    100% { filter: brightness(0.90); }
}

/* ============ EFECTO SCANNER HUD ========= */
.main:before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: repeating-linear-gradient(
        0deg,
        rgba(20,255,255,0.12) 0px,
        rgba(20,255,255,0.12) 2px,
        transparent 2px,
        transparent 4px
    );
    mix-blend-mode: screen;
    animation: hudScan 6s linear infinite;
    pointer-events: none;
}

@keyframes hudScan {
    0% { transform: translateY(-10%); }
    100% { transform: translateY(110%); }
}

/* ============ TITULOS HOLOGRÁFICOS ============ */
h1, h2, h3 {
    font-family: 'Audiowide', sans-serif !important;
    color: #66eaff;
    font-weight: 600;
    text-shadow:
        0 0 10px rgba(102,234,255,0.9),
        0 0 20px rgba(102,234,255,0.5);
    animation: holoGlow 3s ease-in-out infinite alternate;
}

@keyframes holoGlow {
    0% { text-shadow: 0 0 6px #00d9ff; }
    100% { text-shadow: 0 0 20px #66eaff; }
}

/* ============ TEXTO ============ */
p, span, li, input, label {
    font-family: 'Sarpanch', sans-serif;

    color: #c7f2ff !important;
}

/* ============ TEXTAREA - VIDRIO HOLOGRÁFICO ============ */
textarea {
    background: rgba(0,50,70,0.35) !important;
    backdrop-filter: blur(8px) saturate(1.5);
    border: 2px solid rgba(0,200,255,0.5) !important;
    border-radius: 12px !important;
    padding: 12px !important;
    color: #d6f9ff !important;
    box-shadow: 0 0 12px rgba(0,200,255,0.5);
}

/* ============ BOTONES HOLOGRÁFICOS ============ */
.stButton>button {
    background: rgba(0,180,255,0.25);
    border: 2px solid rgba(0,230,255,0.8);
    border-radius: 10px;
    padding: 14px 28px;
    color: #dffaff;
    font-weight: bold;
    text-shadow: 0 0 6px rgba(255,255,255,0.5);
    box-shadow:
        0 0 10px rgba(0,220,255,0.45),
        inset 0 0 12px rgba(0,220,255,0.35);
    backdrop-filter: blur(6px);
    transition: 0.25s ease;
}

.stButton>button:hover {
    background: rgba(0,220,255,0.45);
    border-color: #66f3ff;
    transform: scale(1.05);
    box-shadow:
        0 0 20px rgba(0,240,255,0.8),
        inset 0 0 25px rgba(255,255,255,0.5);
}

/* ============ PESTAÑAS - TARJETAS DE VIDRIO ============ */
.stTabs [data-baseweb="tab"] {
    font-size: 15px;
    font-weight: bold;
    color: #9eeaff;
    background: rgba(0,30,40,0.55);
    backdrop-filter: blur(10px) saturate(1.4);
    border-radius: 10px 10px 0 0;
    border: 1px solid rgba(0,180,255,0.4);
    margin-right: 6px;
    padding: 10px 20px;
    transition: 0.25s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    color: #dffaff;
    background: rgba(0,45,60,0.75);
    border-color: rgba(0,230,255,0.7);
}

.stTabs [aria-selected="true"] {
    background: rgba(0,80,110,0.75) !important;
    border-bottom: 3px solid #5fe6ff !important;
    color: #ffffff !important;
}

/* ============ RESULTADOS HOLOGRÁFICOS ============ */
div[data-testid="stMetricValue"], .stAlert>div {
    background: rgba(0,35,50,0.55);
    backdrop-filter: blur(6px);
    padding: 10px 14px;
    border-radius: 12px;
    border: 1px solid rgba(0,200,255,0.4);
    box-shadow: 0 0 10px rgba(0,220,255,0.4);
    color: #dffaff !important;
}

/* ============ TABLAS FUTURISTAS ============ */
table {
    background: rgba(0,25,35,0.6) !important;
    color: #c7f7ff;
    border-radius: 10px;
    backdrop-filter: blur(4px);
    border: 1px solid rgba(0,200,255,0.4);
}

/* ============ SCROLLBAR NEÓN ============ */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(#0dc6ff, #63f3ff);
    border-radius: 10px;
    box-shadow: 0 0 6px rgba(0,200,255,0.8);
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(#63f3ff, #a7ffff);
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
