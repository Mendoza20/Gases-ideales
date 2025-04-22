import streamlit as st
st.imagen("imagen1.jpg")
# Constante R (L·atm/mol·K)
R = 0.0821

st.title("🧪 Cálculo de Número de Moles (n)")
st.markdown("Usando la ecuación: **n = PV / RT**")

# Entradas del usuario
P = st.number_input("Presión (P) en atm", min_value=0.001, format="%.4f")
V = st.number_input("Volumen (V) en litros", min_value=0.001, format="%.4f")
T = st.number_input("Temperatura (T) en Kelvin", min_value=0.001, format="%.4f")

# Cálculo de n
if st.button("Calcular n (mol)"):
    n = (P * V) / (R * T)
    st.success(f"n = {n:.4f} mol")
