import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Graficas con matplotlib")

# Datos
categorias = ["a", "b", "c"]
valores = [105, 89, 90]

fig, ax = plt.subplots(figsize=(6, 6))

# Crear la gráfica circular
ax.pie(valores, labels=categorias)

# Título
ax.set_title("Distribución de Valores")

# Mostrar en Streamlit
st.pyplot(fig)