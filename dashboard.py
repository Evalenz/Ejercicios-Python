import pandas as pd 
import streamlit as st
import plotly.express as px 
import plotly.graph_objects as go   

@st.cache_data
def load_data ():
    ventas = pd.read_csv("ventas.csv", parse_dates= ["fecha"])
    empleados = pd.read_csv("empleados.csv")
    clientes = pd.read_csv("clientes.csv")
    calificaciones = pd.read_csv("calificaciones.csv")
    return ventas, empleados, clientes, calificaciones

ventas, empleados, clientes, calificaciones = load_data()

st.title ("Dashboard Interactivo - Ventas, Empleados, Clientes y Calificaciones")  

# sidebar global
st.sidebar.header ("Filtros Globales")
datasets = ["Ventas", "Empleados", "Clientes", "Calificaciones"]
view = st.sidebar.selectbox ("Vista", datasets)

# ---- Ventas ----
if view == "Saldo":
    st.subheader ("Análisis de Ventas")
    # Filtros
    productos = [ "Todos"] + sorted (ventas["producto"].dropna().unique().tolist())
    prod_sel = st.sidebar.selectbox ("Producto", productos)
    fecha_min, fecha_max = ventas["fecha"].min(), ventas["fecha"].max()
    rango = st.sidebar.date_input ("Rango de Fecha", [fecha_min, fecha_max])
    start, end = rango if isinstance (rango, list) else (fecha_min, fecha_max)

    



 