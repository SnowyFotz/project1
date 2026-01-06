import streamlit as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Configuración de página
st.set_page_config(page_title="Calculadora Estadística", layout="wide")

# =============================
# 💠 ESTILOS FUTURISTAS B&W NYA 💠
# Inyección de CSS para el tema Dark Future
# =============================
st.markdown("""
<style>
    /* --- FONDO GLOBAL Y FUENTE --- */
    .stApp {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Courier New', Courier, monospace; /* Fuente tipo terminal */
    }

    /* --- ENCABEZADOS --- */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 1px solid #333;
        padding-bottom: 10px;
    }

    /* --- BOTONES CON GLOW (La parte importante nya) --- */
    div.stButton > button {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #ffffff !important;
        border-radius: 0px !important; /* Bordes cuadrados futuristas */
        padding: 0.5rem 1rem;
        font-family: 'Courier New', monospace;
        text-transform: uppercase;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.1);
    }

    /* Efecto Hover (Brillo Blanco) */
    div.stButton > button:hover {
        box-shadow: 0 0 15px #ffffff, 0 0 5px #ffffff inset !important;
        text-shadow: 0 0 8px #ffffff;
        border-color: #ffffff !important;
        background-color: #000000 !important;
        font-weight: bold;
        transform: scale(1.02);
    }

    /* Efecto Click */
    div.stButton > button:active {
        background-color: #ffffff !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #ffffff !important;
    }

    /* --- INPUTS Y CAJAS DE TEXTO --- */
    /* Hacemos que los inputs sean negros con borde gris */
    .stTextInput input, .stTextArea textarea, .stNumberInput input, .stSelectbox div[data-baseweb="select"] div {
        background-color: #0a0a0a !important;
        color: #ffffff !important;
        border: 1px solid #444 !important;
        border-radius: 0px !important;
    }
    
    /* Focus en los inputs */
    .stTextInput input:focus, .stTextArea textarea:focus, .stNumberInput input:focus {
        border-color: #ffffff !important;
        box-shadow: 0 0 8px rgba(255, 255, 255, 0.3) !important;
    }

    /* --- PESTAÑAS (TABS) --- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #000000;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #000000;
        border: 1px solid #333;
        border-radius: 0px;
        color: #888;
    }
    .stTabs [aria-selected="true"] {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #ffffff !important;
        border-bottom: none !important;
        box-shadow: 0 -5px 10px rgba(255,255,255,0.1);
    }

    /* --- MENSAJES DE ALERTA (Success, Info, Error) --- */
    /* Ajustamos los colores para que no sean tan brillantes, más estilo "consola" */
    .stAlert {
        background-color: #111 !important;
        color: #fff !important;
        border: 1px solid #fff !important;
    }

</style>
""", unsafe_allow_html=True)

st.title("Calculadora Estadística // SYSTEM_READY")

# =============================
# MENÚ CON PESTAÑAS (Funcionalidad Original)
# =============================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Tendencia Central",
    "IC Media Pob.",
    "IC Proporción",
    "Dos Poblaciones",
    "Cálculo Z / T",
    "Tamaño Muestra"
])

# Script de scroll original (se mantiene igual para funcionalidad)
st.markdown("""
<script>
(function(){
  function scrollActiveTabIntoView(){
    try{
      const active = document.querySelector('.stTabs [aria-selected="true"]');
      if(active && active.scrollIntoView){
        active.scrollIntoView({behavior:'smooth', inline:'center', block:'nearest'});
      }
    }catch(e){console.error('scrollActiveTabIntoView error',e)}
  }
  setTimeout(scrollActiveTabIntoView, 50);
  document.addEventListener('click', function(e){
    const t = e.target.closest('[data-baseweb="tab"]');
    if(t) setTimeout(scrollActiveTabIntoView, 50);
  }, true);
  function observeTabs(){
    const tabsContainer = document.querySelector('.stTabs');
    if(!tabsContainer) return;
    const mo = new MutationObserver(function(){
      scrollActiveTabIntoView();
    });
    mo.observe(tabsContainer, {childList:true, subtree:true, attributes:true});
  }
  const app = document.querySelector('[data-testid="stApp"]');
  if(app){
    const mo2 = new MutationObserver(function(){
      observeTabs(); scrollActiveTabIntoView();
    });
    mo2.observe(app, {childList:true, subtree:true});
  }
  observeTabs();
})();
</script>
""", unsafe_allow_html=True)

# =============================
# PESTAÑA 1
# =============================
with tab1:
    st.header(">> Medidas de Tendencia Central")

    datos = st.text_area(
        "INPUT DE DATOS (Separados por comas)",
        placeholder="Ej: 10, 12, 15, 18, 20"
    )

    if st.button("EJECUTAR CÁLCULO [TC]"):
        if datos:
            try:
                lista = [float(x) for x in datos.split(",")]
                media = np.mean(lista)
                mediana = np.median(lista)
                moda = max(set(lista), key=lista.count)

                c1, c2, c3 = st.columns(3)
                c1.metric("Media", f"{media:.4f}")
                c2.metric("Mediana", f"{mediana:.4f}")
                c3.metric("Moda", f"{moda:.4f}")
            except:
                st.error("Error de sintaxis en los datos.")
        else:
            st.warning("Ingrese datos para procesar.")

    st.markdown("---")
    st.subheader(">> Error Estándar")

    c_desv, c_n = st.columns(2)
    desviacion_tc = c_desv.number_input("Desv. Estándar (s)", min_value=0.0, key="tc_desviacion")
    n_tc = c_n.number_input("Muestra (n)", min_value=1, key="tc_n")

    if st.button("CALCULAR ERROR [SE]"):
        error_estandar = desviacion_tc / np.sqrt(n_tc)
        st.success(f"Error estándar = {error_estandar:.4f}")

    st.markdown("---")
    st.subheader(">> Teorema del Límite Central (TLC)")

    if datos:
        try:
            datos_tlc = [float(x) for x in datos.split(",")]
            if len(datos_tlc) >= 2:
                col_tlc1, col_tlc2 = st.columns(2)
                n_muestra = col_tlc1.slider("Tamaño sub-muestra (n)", 2, 50, 5, key="tlc_n")
                num_muestras = col_tlc2.slider("Iteraciones", 50, 1000, 200, key="tlc_num")

                medias = []
                for _ in range(num_muestras):
                    muestra = np.random.choice(datos_tlc, n_muestra, replace=True)
                    medias.append(np.mean(muestra))

                # Gráficos con estilo oscuro
                plt.style.use('dark_background')
                
                fig, ax = plt.subplots()
                ax.hist(medias, bins=30, color='white', edgecolor='black')
                ax.set_title("Distribución de Medias Muestrales", color='white')
                ax.grid(color='#333', linestyle='--')
                st.pyplot(fig)
                plt.close(fig)

                st.write("Histograma Original:")
                fig3, ax3 = plt.subplots()
                ax3.hist(datos_tlc, bins=20, color='#444', edgecolor='white')
                ax3.set_title("Distribución Original", color='white')
                ax3.grid(color='#333', linestyle='--')
                st.pyplot(fig3)
                plt.close(fig3)
            else:
                st.warning("Datos insuficientes para simulación.")
        except ValueError:
            st.error("Formato de datos inválido.")

# =============================
# PESTAÑA 2
# =============================
with tab2:
    st.header(">> Inferencia: Media Poblacional")

    col1, col2 = st.columns(2)
    with col1:
        media_muestral = st.number_input("Media (x̄)", key="infer_media_muestral")
        desviacion = st.number_input("Desviación (σ/s)", min_value=0.0, key="infer_desviacion")
        n = st.number_input("Muestra (n)", min_value=1, key="infer_n")
    with col2:
        nivel_confianza = st.selectbox("Confianza", [0.90, 0.95, 0.99])

    if st.button("CALCULAR INTERVALO [IC]"):
        z = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}[nivel_confianza]
        error = z * (desviacion / np.sqrt(n))
        st.info(f"IC: ({media_muestral - error:.4f}, {media_muestral + error:.4f})")

# =============================
# PESTAÑA 3
# =============================
with tab3:
    st.header(">> Inferencia: Proporción")

    col1, col2 = st.columns(2)
    with col1:
        p = st.number_input("Proporción (p̂)", 0.0, 1.0, key="prop_p")
        n_prop = st.number_input("Muestra (n)", min_value=1, key="prop_n")
    with col2:
        confianza_p = st.selectbox("Confianza", [0.90, 0.95, 0.99], key="prop")

    if st.button("CALCULAR INTERVALO [PROP]"):
        z = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}[confianza_p]
        error = z * np.sqrt((p * (1 - p)) / n_prop)
        st.success(f"IC: ({p - error:.4f}, {p + error:.4f})")

# =============================
# PESTAÑA 4
# =============================
with tab4:
    st.header(">> Dos Poblaciones")
    
    st.markdown("### Diferencia de Medias")
    c1, c2 = st.columns(2)
    with c1:
        x1 = st.number_input("Media 1", key="dosp_x1")
        s1 = st.number_input("Desviación 1", min_value=0.0, key="dosp_s1")
        n1 = st.number_input("n₁", min_value=1, key="dosp_n1")
    with c2:
        x2 = st.number_input("Media 2", key="dosp_x2")
        s2 = st.number_input("Desviación 2", min_value=0.0, key="dosp_s2")
        n2 = st.number_input("n₂", min_value=1, key="dosp_n2")

    if st.button("CALCULAR DIFERENCIA [MEDIAS]"):
        diff = x1 - x2
        st.info(f"Dif: {diff:.4f}")
        # Cálculo del error estándar de la diferencia
        if n1 > 0 and n2 > 0:
            se_diff = np.sqrt((s1**2 / n1) + (s2**2 / n2))
            if se_diff == 0:
                st.warning("Error estándar = 0. Revisa desviaciones y tamaños de muestra.")
            else:
                st.success(f"Error estándar = {se_diff:.4f}")
        else:
            st.warning("Revisa los tamaños de muestra para calcular error estándar.")

    st.markdown("---")
    st.markdown("### Diferencia de Proporciones")
    colp1, colp2 = st.columns(2)
    with colp1:
        p1 = st.number_input("Prop 1 (p̂₁)", 0.0, 1.0, key="p1")
        n1p = st.number_input("n₁ (prop)", min_value=1, key="n1p")
    with colp2:
        p2 = st.number_input("Prop 2 (p̂₂)", 0.0, 1.0, key="p2")
        n2p = st.number_input("n₂ (prop)", min_value=1, key="n2p")

    if st.button("CALCULAR DIFERENCIA [PROP]"):
        st.info(f"Dif: {p1 - p2:.4f}")

    st.markdown("---")
    st.markdown("### Hipótesis: Medias")
    mu0 = st.number_input("H₀ (μ₁ − μ₂)", key="mu0_medias")
    alpha = st.selectbox("Alpha (α)", [0.01, 0.05, 0.10], key="alpha_medias")

    if st.button("TEST HIPÓTESIS [MEDIAS]"):
        if n1 > 0 and n2 > 0:
            se = np.sqrt((s1**2 / n1) + (s2**2 / n2))
            if se == 0:
                st.error("Error estándar es 0.")
            else:
                z = ((x1 - x2) - mu0) / se
                z_crit = stats.norm.ppf(1 - alpha/2)
                st.write(f"Z calc: {z:.4f} | Z crit: ±{z_crit:.4f}")
                if abs(z) > z_crit: st.error("RECHAZAR H₀")
                else: st.success("NO RECHAZAR H₀")
        else:
            st.warning("Revisa los tamaños de muestra.")

    st.markdown("---")
    st.markdown("### Hipótesis: Proporciones")
    p0 = st.number_input("H₀ (p₁ − p₂)", key="p0_prop")
    alpha_p = st.selectbox("Alpha (α)", [0.01, 0.05, 0.10], key="alpha_prop")

    if st.button("TEST HIPÓTESIS [PROP]"):
        if n1p > 0 and n2p > 0:
            p_pool = (p1*n1p + p2*n2p) / (n1p + n2p)
            se_p = np.sqrt(p_pool*(1-p_pool)*(1/n1p + 1/n2p))
            if se_p == 0:
                st.error("Error estándar es 0.")
            else:
                z_p = ((p1 - p2) - p0) / se_p
                z_crit_p = stats.norm.ppf(1 - alpha_p/2)
                st.write(f"Z calc: {z_p:.4f} | Z crit: ±{z_crit_p:.4f}")
                if abs(z_p) > z_crit_p: st.error("RECHAZAR H₀")
                else: st.success("NO RECHAZAR H₀")

# =============================
# PESTAÑA 5
# =============================
with tab5:
    st.header(">> Estadísticos Z / t")

    tipo = st.radio("Selector", ["Z (Normal)", "t (Student)"], horizontal=True)

    col1, col2 = st.columns(2)
    with col1:
        x_barra = st.number_input("Media Muestral", key="xbar_z")
        mu = st.number_input("Media Pob.", key="z_mu")
        s = st.number_input("Desviación", min_value=0.0, key="z_s")
    with col2:
        n = st.number_input("n", min_value=1, key="z_n")
        alpha = st.selectbox("Alpha", [0.01, 0.05, 0.10], index=1, key="alpha_z_t")

    if st.button("CALCULAR ESTADÍSTICO"):
        if tipo.startswith("Z"):
            if s > 0:
                z_stat = (x_barra - mu) / (s / np.sqrt(n))
                p_val = 2 * (1 - stats.norm.cdf(abs(z_stat)))
                z_crit = stats.norm.ppf(1 - alpha/2)
                st.write(f"Z: {z_stat:.4f} | P-val: {p_val:.4f}")
                if abs(z_stat) > z_crit: st.error("RECHAZAR H₀")
                else: st.success("NO RECHAZAR H₀")
            else: st.error("Desviación debe ser > 0")
        else:
            if n > 1 and s > 0:
                t_stat = (x_barra - mu) / (s / np.sqrt(n))
                df = int(n) - 1
                p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df))
                t_crit = stats.t.ppf(1 - alpha/2, df)
                st.write(f"t: {t_stat:.4f} | P-val: {p_val:.4f}")
                if abs(t_stat) > t_crit: st.error("RECHAZAR H₀")
                else: st.success("NO RECHAZAR H₀")
            else: st.error("Verifica n > 1 y s > 0")

# =============================
# PESTAÑA 6
# =============================
with tab6:
    st.header(">> Tamaño de Muestra")

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Para la Media")
        s = st.number_input("Desviación Est.", min_value=0.0, key="s_media")
        E = st.number_input("Error Máx.", min_value=0.0001, key="e_media")
        conf = st.selectbox("Confianza", [0.90,0.95,0.99], key="conf_tm_media")
        if st.button("CALCULAR N [MEDIA]", key="btn_tm_media"):
            z = {0.90:1.645,0.95:1.96,0.99:2.576}[conf]
            n_res = (z*s/E)**2
            st.metric("n Requerida", f"{np.ceil(n_res):.0f}")

    with c2:
        st.subheader("Para la Proporción")
        p = st.number_input("Proporción Est.", 0.0, 1.0, 0.5, key="p_tm")
        E_p = st.number_input("Error Máx.", min_value=0.0001, key="e_prop")
        conf_p = st.selectbox("Confianza", [0.90,0.95,0.99], key="conf_tm_prop")
        if st.button("CALCULAR N [PROP]", key="btn_tm_prop"):
            z = {0.90:1.645,0.95:1.96,0.99:2.576}[conf_p]
            n_res = (z**2 * p*(1-p)) / (E_p**2)
            st.metric("n Requerida", f"{np.ceil(n_res):.0f}")
