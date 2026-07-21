import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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

    st.divider()

    st.subheader("📊 Gráfica de Barras por Posición")

    # Creamos las posiciones para el eje X
    posiciones = np.arange(len(arr))

    # Construcción de la figura
    fig, ax = plt.subplots(figsize=(6,4))
    barras = ax.bar(posiciones, arr, color='#4CAF50', edgecolor='black', alpha=0.85)

    ax.set_title("Valores Registrados en el Arreglo", fontsize=14, fontweight='bold')
    ax.set_xlabel("Posición en el Arreglo (Índice)", fontsize=11)
    ax.set_ylabel("Valor Ingresado", fontsize=11)
    ax.set_xticks(posiciones)  # Muestra solo posiciones enteras (0, 1, 2, ...)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Etiquetar cada barra con su valor numérico
    for barra in barras:
        yval = barra.get_height()
        # Coloca el texto ligeramente arriba de la barra si es positivo, o abajo si es negativo
        va = 'bottom' if yval >= 0 else 'top'
        ax.text(barra.get_x() + barra.get_width()/2.0, yval, f'{yval}', ha='center', va=va, fontsize=9)

    # Renderizamos el gráfico en Streamlit
    st.pyplot(fig)

    # Muestra los datos tal como han sido ingresados
    with st.expander("Ver lista de números registrados"):
        st.write(arr)

    if st.button("Limpiar todos los datos"):
        st.session_state.lista_numeros = []
        st.rerun()