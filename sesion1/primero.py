import streamlit as st
import numpy as np

st.title("📊 Contador y Analizador con NumPy")

# 1. Memoria de la sesión 🧠
if 'lista_numeros' not in st.session_state:
    st.session_state.lista_numeros = []

# 2. Formulario de captura 📝
with st.form("Formulario de numeros", clear_on_submit=True):
    numero = st.number_input("Ingresa un número", value=0)
    boton = st.form_submit_button("Guardar número")

    if boton:
        st.session_state.lista_numeros.append(numero)

# 3. Procesamiento de datos con NumPy ⚡
if len(st.session_state.lista_numeros) > 0:
# Convertimos la lista de Python a un array de NumPy
    arr = np.array(st.session_state.lista_numeros)

    # Métrica 1: Cantidad de números registrados
    total_registros = len(arr)

    # Métrica 2 y 3: Suma y Promedio
    suma_total = np.sum(arr)
    promedio = np.mean(arr)

    # Filtro vectorizado
    cantidad_pares = np.sum(arr % 2 == 0)
    cantidad_multiplos_3 = np.sum(arr % 3 == 0)

    st.subheader("😊 Resultados del Analisis")

    #tabla de datos
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Números", total_registros)
    col2.metric("Suma Total", f"{suma_total:.2f}")
    col3.metric("Promedio", f"{promedio:.2f}")

    col4, col5 = st.columns(2)
    col4.metric("Cantidad de Pares", f"{cantidad_pares}")
    col5.metric("Múltiplos de 3", f"{cantidad_multiplos_3}")

    # Muestra los datos tal como han sido ingresados
    with st.expander("Ver lista de números registrados"):
        st.write(arr)

    if st.button("Limpiar todos los datos"):
        st.session_state.lista_numeros = []
        st.rerun()