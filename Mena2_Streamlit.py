import streamlit as st
import pandas as pd
import numpy as np
import math
import warnings
import random

warnings.filterwarnings('ignore')

def calculate_entropy(data: pd.DataFrame, target_col: str = None) -> float:
    if target_col is None:
        target_col = data.columns[-1]
    if len(data) == 0:
        return 0
    value_counts = data[target_col].value_counts()
    total = len(data)
    entropy = 0
    for count in value_counts:
        probability = count / total
        if probability > 0:
            entropy -= probability * math.log2(probability)
    return entropy

def calculate_information_gain(data: pd.DataFrame, attribute: str, target_col: str = None) -> float:
    if target_col is None:
        target_col = data.columns[-1]
    total_entropy = calculate_entropy(data, target_col)
    total_instances = len(data)
    weighted_entropy = 0
    for value in data[attribute].unique():
        subset = data[data[attribute] == value]
        probability = len(subset) / total_instances
        weighted_entropy += probability * calculate_entropy(subset, target_col)
    return total_entropy - weighted_entropy

def configure_attributes_auto(data):
    columns = list(data.columns)
    class_column = columns[-1]
    attribute_columns = columns[:-1]
    processed_data = data.copy()
    attribute_types = {}
    nominal_values = {}
    numeric_ranges = {}
    for attr in attribute_columns:
        unique_values = data[attr].unique()
        if data[attr].dtype in ['object', 'string'] or len(unique_values) <= 5:
            attribute_types[attr] = "nominal"
            value_mapping = {}
            available_labels = [1, 2, 3]
            for i, val in enumerate(unique_values):
                if i < 3:
                    value_mapping[val] = available_labels[i]
            nominal_values[attr] = value_mapping
            processed_data[attr] = processed_data[attr].map(value_mapping)
        else:
            attribute_types[attr] = "numeric"
            q1 = data[attr].quantile(0.33)
            q2 = data[attr].quantile(0.67)
            numeric_ranges[attr] = (q1, q2)
            processed_data[attr] = processed_data[attr].apply(
                lambda x: 1 if x < q1 else (2 if q1 <= x <= q2 else 3)
            )
    attribute_types[class_column] = "clase"
    unique_classes = data[class_column].unique()
    if len(unique_classes) == 2:
        class_mapping = {unique_classes[0]: 0, unique_classes[1]: 1}
        processed_data[class_column] = processed_data[class_column].map(class_mapping)
    return processed_data, attribute_types, nominal_values, numeric_ranges

def main():
    st.set_page_config(
        page_title="\U0001F333 Analizador de Entropía y Árboles de Decisión",
        page_icon="\U0001F333",
        layout="wide"
    )

    st.markdown("""
        <style>
            html, body, [class*="css"] {
                font-family: 'Segoe UI', sans-serif;
                background-color: #f9f9f9;
            }
            h1, h2, h3, h4 {
                color: #2c3e50;
            }
            .block-container {
                padding: 2rem 2rem;
            }
            .stButton > button {
                background-color: #2c3e50;
                color: white;
                border-radius: 0.5rem;
                padding: 0.6rem 1.2rem;
                border: none;
            }
            .stButton > button:hover {
                background-color: #34495e;
            }
            .stRadio > div, .stSelectbox > div, .stNumberInput > div {
                padding: 0.5rem;
            }
            .stDataFrame, .stTable {
                border-radius: 0.5rem;
                overflow: hidden;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("\U0001F333 Analizador de Entropía y Árboles de Decisión")
    st.markdown("---")

    st.subheader("📥 Selecciona el modo de entrada de datos")
    input_mode = st.radio(
        "¿Cómo quieres ingresar los datos?",
        ["📁 Cargar archivo (CSV/Excel)", "✏️ Crear datos manualmente"],
        index=0
    )

    data = None

    if input_mode == "📁 Cargar archivo (CSV/Excel)":
        uploaded_file = st.file_uploader(
            "📁 Selecciona tu archivo de datos (CSV o Excel)",
            type=['csv', 'xlsx', 'xls']
        )
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    data = pd.read_csv(uploaded_file)
                else:
                    data = pd.read_excel(uploaded_file)
                st.success(f"✅ Datos cargados exitosamente: {data.shape[0]} instancias, {data.shape[1]} columnas")
            except Exception as e:
                st.error(f"❌ Error al cargar el archivo: {str(e)}")
    else:
        st.subheader("✏️ Creación Manual de Datos")
        st.info("⚠️ Por simplicidad, esta versión simplificada solo soporta carga desde archivo. Agrega manualmente en tu CSV.")

    if data is not None:
        st.subheader("📋 Datos Originales")
        st.dataframe(data.head(10), use_container_width=True, height=300)

        processed_data, attribute_types, nominal_values, numeric_ranges = configure_attributes_auto(data)

        st.subheader("🔧 Datos Procesados")
        st.dataframe(processed_data.head(10), use_container_width=True, height=300)

        target_col = processed_data.columns[-1]
        general_entropy = calculate_entropy(processed_data, target_col)
        all_columns = list(processed_data.columns)
        gains = {attr: calculate_information_gain(processed_data, attr, target_col) for attr in all_columns}
        sorted_gains = sorted(gains.items(), key=lambda x: x[1], reverse=True)

        st.subheader("🌳 Selección del Nodo Raíz")
        options = [f"{attr} (Ganancia: {gain:.4f})" + (" 🎯 [CLASE]" if attr == target_col else "") for attr, gain in sorted_gains]
        selected_option = st.selectbox("Selecciona el atributo que será el nodo raíz:", options, index=0)
        selected_attr = selected_option.split(" (Ganancia:")[0]
        selected_gain = gains[selected_attr]

        st.success(f"✅ Nodo raíz seleccionado: **{selected_attr}** con ganancia de **{selected_gain:.4f}**")

        st.markdown("---")
        st.subheader("📊 RESULTADOS COMPLETOS DEL ANÁLISIS")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Entropía General", f"{general_entropy:.4f}")
        with col2:
            st.metric("Ganancia Seleccionada", f"{selected_gain:.4f}")
        with col3:
            st.metric("Instancias", len(processed_data))
        with col4:
            st.metric("Atributos", len(all_columns) - 1)

        st.subheader("🏆 Ranking de Atributos por Ganancia de Información")
        ranking_data = [{
            "Posición": "⭐" if attr == selected_attr else f"{i+1}.",
            "Atributo": attr,
            "Ganancia": f"{gain:.4f}",
            "Tipo": "🎯 Clase" if attr == target_col else f"📊 {attribute_types.get(attr, 'Desconocido').title()}"
        } for i, (attr, gain) in enumerate(sorted_gains)]
        st.dataframe(pd.DataFrame(ranking_data), use_container_width=True)

        st.markdown("---")
        st.subheader("🎯 RESUMEN FINAL")
        summary_text = f"""
            **🌳 Nodo Raíz Seleccionado:** {selected_attr} ({'🎯 CLASE' if selected_attr == target_col else '📊 ATRIBUTO'})

            **📊 Métricas Principales:**
            - Entropía General: {general_entropy:.4f}
            - Ganancia del Nodo Raíz: {selected_gain:.4f}
            - Total de Instancias: {len(processed_data)}
            - Total de Atributos: {len(all_columns) - 1}

            **🏆 Ranking de Atributos:**
        """
        for i, (attr, gain) in enumerate(sorted_gains[:4], 1):
            marker = "⭐" if attr == selected_attr else f"{i}."
            type_indicator = " 🎯" if attr == target_col else ""
            summary_text += f"\n{marker} {attr}{type_indicator}: {gain:.4f}"
        st.markdown(summary_text)

        if selected_attr == target_col:
            st.warning("""
                **⚠️ NOTA IMPORTANTE:**
                Has seleccionado la variable objetivo (clase) como nodo raíz. 
                Esto puede resultar en interpretaciones especiales del árbol de decisión.
                En la práctica, normalmente se usan los atributos predictores como nodos raíz.
            """)

if __name__ == "__main__":
    main()
