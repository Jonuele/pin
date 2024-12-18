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

    # Suma de los dígitos del año de nacimiento
    suma_año = sum(int(digit) for digit in str(año_nacimiento))

    # Calculamos cada número del esquema según la fecha de nacimiento:

    # A. Número de Karma: día de nacimiento reducido
    numero_karma = reducir_numero(mes_nacimiento)

    # B. Número Personal: suma de día y mes
    numero_personal = reducir_numero(dia_nacimiento)

    # C. Número de vida pasada: suma de mes y año
    numero_vida_pasada = reducir_numero(año_nacimiento)

    # D. Número de personalidad: día + mes + año completo
    numero_personalidad = reducir_numero(numero_karma + numero_personal + numero_vida_pasada)

    # E. Número de Primera realizacion:
    numero_primera_realizacion = reducir_numero(numero_karma + numero_personal)

    # F. Número de Segunda realizacion:
    numero_segunda_realizacion = reducir_numero(numero_personal + numero_vida_pasada)

    # G. Número de Tercera realizacion:
    numero_tercera_realizacion = reducir_numero(numero_primera_realizacion + numero_segunda_realizacion)

    # H. Número de Cuarta realizacion:
    numero_cuarta_realizacion = reducir_numero(numero_karma + numero_vida_pasada)

    # I. Número del subconsciente: suma de los dígitos del día y mes
    numero_subconsciente = reducir_numero(numero_primera_realizacion + numero_segunda_realizacion + numero_tercera_realizacion)

    # J. Número del inconsciente: suma de los dígitos del año
    numero_inconsciente = reducir_numero(numero_personalidad + numero_cuarta_realizacion)

    # NUMEROS NEGATIVOS
    # K. Número Meta 1
    numero_meta1 = abs(reducir_numeronomaestro(reducir_numeronomaestro(mes_nacimiento) - reducir_numeronomaestro(dia_nacimiento)))

    # L. Número Meta 2
    numero_meta2 = abs(reducir_numeronomaestro(reducir_numeronomaestro(dia_nacimiento) - reducir_numeronomaestro(año_nacimiento)))

    # M. Número Meta 3
    numero_meta3 = abs(reducir_numeronomaestro(reducir_numeronomaestro(numero_meta1) - reducir_numeronomaestro(numero_meta2)))

    # N. Número Meta 4
    numero_meta4 = abs(reducir_numeronomaestro(reducir_numeronomaestro(mes_nacimiento) - reducir_numeronomaestro(año_nacimiento)))

    # O. Número de inconsciente negativo: último dígito del día
    numero_inconsciente_negativo = reducir_numeronomaestro(reducir_numeronomaestro(numero_meta3) + reducir_numeronomaestro(numero_meta1) + reducir_numeronomaestro(numero_meta2))

    # P. Número de sombra: suma de día, mes y último dígito del año
    numero_sombra = reducir_numero(reducir_numero(numero_personalidad) + reducir_numero(numero_inconsciente_negativo))

    # Q, R, S: Ser inferior
    ser_inferior_heredado = reducir_numeronomaestro(reducir_numeronomaestro(numero_meta1) + reducir_numeronomaestro(numero_meta3))  # último dígito del año
    ser_inferior_consciente = reducir_numeronomaestro(reducir_numeronomaestro(numero_meta2) + reducir_numeronomaestro(numero_meta3))
    ser_inferior_latente = reducir_numeronomaestro(reducir_numeronomaestro(ser_inferior_heredado) + reducir_numeronomaestro(ser_inferior_consciente))

    # Mostrar los resultados
    st.write(f"Número Karma: {numero_karma}")
    st.write(f"Número Personal: {numero_personal}")
    st.write(f"Número Vida Pasada: {numero_vida_pasada}")
    st.write(f"Número Personalidad: {numero_personalidad}")
    st.write(f"Número Primera Realización: {numero_primera_realizacion}")
    st.write(f"Número Segunda Realización: {numero_segunda_realizacion}")
    st.write(f"Número Tercera Realización: {numero_tercera_realizacion}")
    st.write(f"Número Cuarta Realización: {numero_cuarta_realizacion}")
    st.write(f"Número Subconsciente: {numero_subconsciente}")
    st.write(f"Número Inconsciente: {numero_inconsciente}")
    st.write(f"Número Sombra: {numero_sombra}")
    st.write(f"Número Inconsciente Negativo: {numero_inconsciente_negativo}")
    st.write(f"Ser Inferior Heredado: {ser_inferior_heredado}")
    st.write(f"Ser Inferior Consciente: {ser_inferior_consciente}")
    st.write(f"Ser Inferior Latente: {ser_inferior_latente}")

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
        'J': numero_inconsciente}
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

    plt.figure(figsize=(8, 8))
    node_labels = {nodo: f"{nodo}\n{valor}" for nodo, valor in nodos.items()}
    nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=2000, node_color='lightblue', font_size=10,
            font_weight='bold', arrows=True)
    st.pyplot(plt)
     # Mostrar los resultados usando st.write en lugar de print
    # st.write(f"Tu Número Karma: {numero_karma}")
    # st.write(f"Tu Número Quien Soy: {numero_personal}")
    # st.write(f"Tu Número Vidas Pasadas: {numero_vida_pasada}")
    # st.write(f"Tu Número Camino De Vida: {numero_personalidad}")
    # st.write(f"Tu Número Primera Realizacion: {numero_primera_realizacion}")
    # st.write(f"Tu Número Segunda Realizacion: {numero_segunda_realizacion}")
    # st.write(f"Tu Número Tercera Realizacion: {numero_tercera_realizacion}")
    # st.write(f"Tu Número Cuarta Realizacion: {numero_cuarta_realizacion}")
    # st.write(f"Tu Número Sexto Sentido: {numero_subconsciente}")
    # st.write(f"Tu Número Numero Del Inconsciente o De La Pareja: {numero_inconsciente}")
    # st.write(f"Tu Número Meta 1: {numero_meta1}")
    # st.write(f"Tu Número Meta 2: {numero_meta2}")
    # st.write(f"Tu Número Meta 3: {numero_meta3}")
    # st.write(f"Tu Número Meta 4: {numero_meta4}")
    # st.write(f"Tu Número Subconsciente Negativo: {numero_inconsciente_negativo}")
    # st.write(f"Tu Número Sombra: {numero_sombra}")
    # st.write(f"Tu Número Ser Inferior Generado Por Herencia De Familia: {ser_inferior_heredado}")
    # st.write(f"Tu Número Ser Inferior Desarrollado Por Ti Mismo: {ser_inferior_consciente}")
    # st.write(f"Tu Número Ser Inferior Inconsciente: {ser_inferior_latente}")
