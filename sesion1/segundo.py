import streamlit as st
import matplotlib.pyplot as plt


st.title("📊 Graficas con matplotlib")

# Datos
categorias = ["a", "b", "c"]
valores = [105, 89, 90]

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(8, 4))

# Crear la gráfica
ax.bar(categorias, valores, color=["green", "red", "yellow"])

# Título
ax.set_title("Ventas")

# Nombre de los ejes
ax.set_xlabel("Productos")
ax.set_ylabel("Cantidad")

# Mostrar la gráfica
st.pyplot(fig)