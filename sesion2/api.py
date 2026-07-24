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



# HTTP response status codes indicate whether a specific HTTP request
# has been successfully completed. Responses are grouped in five classes:
# Informational responses (100 – 199)
# Successful responses (200 – 299)
# Redirection messages (300 – 399)
# Client error responses (400 – 499)
# Server error responses (500 – 599)

# definir funcion consulta
def consulta(pokemon):
    #USAMOS lower para convertir en minusculas el texto y strip para eliminar espacios en blanco
    respuesta = requests.get(URL + pokemon.lower().strip())

    #verificamos respuesta y en caso de ser error mandamos este mensaje
    if respuesta.status_code != 200:
        st.error(f"¡No se encontró el pokemon: '{pokemon}'! Intenta con otro nombre.", icon="🚨")
        return
    
    datos = respuesta.json()

    #Datos para la card
    nombre = datos["name"].capitalize()
    hp = datos["stats"][0]["base_stat"]  # El primer stat suele ser HP
    totalm = len(datos['moves'])
    st.header(f"{totalm} Movimientos de {pokemon}")
    url_imagen = datos["sprites"]["other"]["dream_world"]["front_default"]
    #url_imagen = url_imagen['forms']['url']
    st.image(url_imagen, width=400)
    for move in datos['moves']:
        st.text(f"Movimiento: {move["move"]["name"]}")



st.title("Consumo de APi")

st.header("Ejemplo de consumo de datos api pokemon")

#st.text(f"Status code API {respuesta}")

# Intension consultar mediante entrada los datos de un pokemon
with st.form("Formulario de busqueda Pokemon"):
    pokemon = st.text_input("Escribe el nombre de un pokemon: ")
    conpokemon = st.form_submit_button("Consultar")

    if conpokemon:
        consulta(pokemon)


    


