import pyshorteners
import streamlit as st

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

#Creamos una app simple con Streamlit
st.set_page_config(page_title="Acortador de URL", page_icon=":link:")
st.title("Acortador de URL")
url = st.text_input("Introduce la URL que deseas acortar")
if st.button("Acortar"):
    shortened_url = shorten_url(url)
    st.success("URL acortada: {}".format(shortened_url))