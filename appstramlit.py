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

fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
fecha_nacimiento = pd.to_datetime(fecha_nacimiento)
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
    
    # Aquí calculas los números según la fecha de nacimiento
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
    numero_meta1 = abs(reducir_numeronomaestro(reducir_numeronomaestro(mes_nacimiento) - reducir_numeronomaestro(dia_nacimiento)))
    numero_meta2 = abs(reducir_numeronomaestro(reducir_numeronomaestro(dia_nacimiento) - reducir_numeronomaestro(año_nacimiento)))
    numero_meta3 = abs(reducir_numeronomaestro(reducir_numeronomaestro(numero_meta1) - reducir_numeronomaestro(numero_meta2)))
    numero_meta4 = abs(reducir_numeronomaestro(reducir_numeronomaestro(mes_nacimiento) - reducir_numeronomaestro(año_nacimiento)))
    numero_inconsciente_negativo = reducir_numeronomaestro(reducir_numeronomaestro(numero_meta3) + reducir_numeronomaestro(numero_meta1) + reducir_numeronomaestro(numero_meta2))
    numero_sombra = reducir_numero(reducir_numero(numero_personalidad) + reducir_numero(numero_inconsciente_negativo))
    ser_inferior_heredado = reducir_numeronomaestro(reducir_numeronomaestro(numero_meta1) + reducir_numeronomaestro(numero_meta3))
    ser_inferior_consciente = reducir_numeronomaestro(reducir_numeronomaestro(numero_meta2) + reducir_numeronomaestro(numero_meta3))
    ser_inferior_latente = reducir_numeronomaestro(reducir_numeronomaestro(ser_inferior_heredado) + reducir_numeronomaestro(ser_inferior_consciente))

    # Aquí va la visualización del gráfico
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

    # Crear la posición de los nodos en el gráfico
    pos = nx.spring_layout(G)

    # Ajustar posiciones manualmente para A, B, C y D
    pos['A'] = (0, 1)
    pos['B'] = (1, 1)
    pos['C'] = (2, 1)
    pos['D'] = (3, 1)

    # Asignar posiciones para los otros nodos
    pos['H'] = (1, 2)  # H arriba del centro
    pos['G'] = (1, 1.7)  # G a la izquierda de H
    pos['E'] = (0.5, 1.2)  # E justo a la izquierda de B
    pos['I'] = (1, 1.3)  # I abajo de E
    pos['F'] = (1.5, 1.2)  # F abajo de I
    pos['K'] = (0.5, 0.8)  # K abajo de A
    pos['O'] = (1, 0.8)  # O abajo de B
    pos['L'] = (1.5, 0.8)  # L abajo de C
    pos['M'] = (1, 0.55)  # M abajo de O
    pos['P'] = (0.1, 0.4)  # P abajo de K
    pos['N'] = (1, 0.4)  # N abajo de M
    pos['Q'] = (0.5, 0.2)  # Q abajo de L
    pos['R'] = (1, 0.2)  # R a la derecha de M
    pos['S'] = (1.5, 0.2)  # S abajo de R
    pos['J'] = (2.2, 1.4)  # J a la derecha de D
    pos = nx.spring_layout(G)

    plt.figure(figsize=(8, 8))
    node_labels = {nodo: f"{nodo}\n{valor}" for nodo, valor in nodos.items()}
    nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=2000, node_color='lightblue', font_size=10,
            font_weight='bold', arrows=True)
    st.pyplot(plt)
