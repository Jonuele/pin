import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Configuración inicial
st.title("Aplicación de Numerología")
st.subheader("Ingresa tu fecha de nacimiento para calcular tus números.")

# Entrada del usuario
fecha_nacimiento = st.date_input("Fecha de nacimiento", value=pd.Timestamp("2000-01-01"))

# Si se selecciona una fecha
if fecha_nacimiento:
    # Extraer día, mes y año
    dia_nacimiento = fecha_nacimiento.day
    mes_nacimiento = fecha_nacimiento.month
    año_nacimiento = fecha_nacimiento.year

    # Función para reducir número
    def reducir_numero(numero):
        while numero > 9 and numero not in (11, 22, 33):
            numero = sum(int(digit) for digit in str(numero))
        return numero

    def reducir_numeronomaestro(numero):
        while numero > 9:
            numero = sum(int(digit) for digit in str(numero))
        return numero

    # Cálculos principales
    suma_año = sum(int(digit) for digit in str(año_nacimiento))
    numero_karma = reducir_numero(mes_nacimiento)
    numero_personal = reducir_numero(dia_nacimiento)
    numero_vida_pasada = reducir_numero(año_nacimiento)
    numero_personalidad = reducir_numero(numero_karma + numero_personal + numero_vida_pasada)
    numero_primera_realizacion = reducir_numero(numero_karma + numero_personal)
    numero_segunda_realizacion = reducir_numero(numero_personal + numero_vida_pasada)
    numero_tercera_realizacion = reducir_numero(numero_primera_realizacion + numero_segunda_realizacion)
    numero_cuarta_realizacion = reducir_numero(numero_karma + numero_vida_pasada)
    numero_subconsciente = reducir_numero(numero_primera_realizacion + numero_segunda_realizacion + numero_tercera_realizacion)
    numero_inconsciente = reducir_numero(numero_personalidad + numero_cuarta_realizacion)
    numero_meta1 = abs(reducir_numeronomaestro(mes_nacimiento - dia_nacimiento))
    numero_meta2 = abs(reducir_numeronomaestro(dia_nacimiento - año_nacimiento))
    numero_meta3 = abs(reducir_numeronomaestro(numero_meta1 - numero_meta2))
    numero_meta4 = abs(reducir_numeronomaestro(mes_nacimiento - año_nacimiento))
    numero_inconsciente_negativo = reducir_numeronomaestro(numero_meta3 + numero_meta1 + numero_meta2)
    numero_sombra = reducir_numero(numero_personalidad + numero_inconsciente_negativo)
    ser_inferior_heredado = reducir_numeronomaestro(numero_meta1 + numero_meta3)
    ser_inferior_consciente = reducir_numeronomaestro(numero_meta2 + numero_meta3)
    ser_inferior_latente = reducir_numeronomaestro(ser_inferior_heredado + ser_inferior_consciente)

    # Mostrar resultados
    st.markdown("### Resultados:")
    resultados = {
        "Número Karma": numero_karma,
        "Número Personal": numero_personal,
        "Número Vida Pasada": numero_vida_pasada,
        "Número Personalidad": numero_personalidad,
        "Número Primera Realización": numero_primera_realizacion,
        "Número Segunda Realización": numero_segunda_realizacion,
        "Número Tercera Realización": numero_tercera_realizacion,
        "Número Cuarta Realización": numero_cuarta_realizacion,
        "Número Subconsciente": numero_subconsciente,
        "Número Inconsciente": numero_inconsciente,
        "Número Meta 1": numero_meta1,
        "Número Meta 2": numero_meta2,
        "Número Meta 3": numero_meta3,
        "Número Meta 4": numero_meta4,
        "Número Inconsciente Negativo": numero_inconsciente_negativo,
        "Número Sombra": numero_sombra,
        "Ser Inferior Heredado": ser_inferior_heredado,
        "Ser Inferior Consciente": ser_inferior_consciente,
        "Ser Inferior Latente": ser_inferior_latente,
    }

    for key, value in resultados.items():
        st.write(f"{key}: {value}")

    # Crear gráfico
    st.markdown("### Visualización de Estructura:")
    nodos = {
        'H': numero_cuarta_realizacion,
        'G': numero_tercera_realizacion,
        'E': numero_primera_realizacion,
        'I': numero_subconsciente,
        'F': numero_segunda_realizacion,
        'A': numero_karma,
        'B': numero_personal,
        'C': numero_vida_pasada,
        'D': numero_personalidad,
        'K': abs(numero_meta1),
        'O': numero_inconsciente_negativo,
        'L': abs(numero_meta2),
        'M': abs(numero_meta3),
        'P': numero_sombra,
        'N': abs(numero_meta4),
        'Q': ser_inferior_heredado,
        'R': ser_inferior_consciente,
        'S': ser_inferior_latente,
        'J': numero_inconsciente
    }
    G = nx.DiGraph()
    for nodo, valor in nodos.items():
        G.add_node(nodo, value=valor)
    edges = [('H', 'A'), ('H', 'C'), ('H', 'J'), ('J', 'D'), ('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'E'),
             ('E', 'B'), ('B', 'F'), ('F', 'C'), ('A', 'K'), ('K', 'B'), ('B', 'L'), ('L', 'C'), ('K', 'M'),
             ('L', 'M')]
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 8))
    node_labels = {nodo: f"{nodo}\n{valor}" for nodo, valor in nodos.items()}
    nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=2000, node_color='lightblue', font_size=10,
            font_weight='bold', arrows=True)
    st.pyplot(plt)
