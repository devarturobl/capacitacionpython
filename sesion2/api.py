import requests #libreria para llamar a las api
import streamlit as st

#url del api
URL = "https://pokeapi.co/api/v2/pokemon/"

# Usamos los metodos de peticion de api
# Métodos HTTP Principales
# GET: Pide y busca datos del servidor sin cambiarlos.
# POST: Envía datos nuevos para crear un recurso.
# PUT: Cambia o actualiza por completo un dato que ya existe.
# DELETE: Borra un recurso del servidor.

respuesta = requests.get(URL)

# HTTP response status codes indicate whether a specific HTTP request
# has been successfully completed. Responses are grouped in five classes:
# Informational responses (100 – 199)
# Successful responses (200 – 299)
# Redirection messages (300 – 399)
# Client error responses (400 – 499)
# Server error responses (500 – 599)


st.title("Consumo de APi")

st.header("Ejemplo de consumo de datos api pokemon")

st.text(f"Status code API {respuesta}")


#cambiar respuesta a formato json
datos = respuesta.json()

st.text(f"Datos JSON {datos}")

# Intension consultar mediante entrada los datos de un pokemon

