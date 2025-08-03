# 🌳 Analizador de Entropía y Árboles de Decisión - Versión Gráfica

## 📋 Descripción

Esta es la versión gráfica del analizador de entropía y árboles de decisión que incluye visualizaciones interactivas y gráficos informativos para analizar datos de clasificación.

## 🚀 Características

### 📊 Tipos de Gráficos Disponibles

1. **📈 Distribución de Clases**
   - Gráfico de barras y gráfico de pastel
   - Muestra la distribución entre clases positivas y negativas

2. **📊 Distribución de Atributos**
   - Gráficos de barras para cada atributo
   - Muestra la frecuencia de valores (Bajo, Normal, Alto)

3. **🎯 Ganancia de Información**
   - Gráfico de barras horizontal
   - Ranking de atributos por ganancia de información
   - Marca el nodo raíz seleccionado con ⭐

4. **🔗 Matriz de Correlación**
   - Heatmap de correlaciones entre atributos
   - Ayuda a identificar relaciones entre variables

5. **🌳 Distribución del Nodo Raíz**
   - Gráficos de barras apiladas por clase
   - Gráfico de líneas de tendencia
   - Matriz de contingencia
   - Gráfico de pastel de distribución general

6. **📉 Entropía por Valor**
   - Gráfico de barras de entropía para cada valor del nodo raíz
   - Ayuda a entender la pureza de cada rama

7. **📋 Datos Originales**
   - Visualización de los datos antes de la transformación
   - Útil para entender la distribución original

8. **🎨 Resumen Completo**
   - Dashboard con 12 gráficos diferentes
   - Vista general de todo el análisis

## 🛠️ Instalación

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **O instalar manualmente:**
   ```bash
   pip install pandas numpy matplotlib seaborn openpyxl xlrd
   ```

## 📖 Uso

### Ejecutar el Programa

```bash
python Mena2_Graficos.py
```

### Flujo de Trabajo

1. **Cargar Datos**
   - Selecciona "1. 📁 Cargar datos desde archivo"
   - El programa detectará automáticamente archivos CSV/Excel en el directorio
   - O introduce manualmente el nombre del archivo

2. **Configurar Atributos**
   - El programa detectará automáticamente el tipo de cada atributo
   - Para atributos nominales: mapeará valores a Bajo(1), Normal(2), Alto(3)
   - Para atributos numéricos: pedirá rangos X1 y X2 para categorización

3. **Seleccionar Nodo Raíz**
   - Selecciona "2. 🌳 Seleccionar nodo raíz"
   - El programa mostrará las ganancias de información de cada atributo
   - Puedes elegir manualmente o usar el de mayor ganancia automáticamente

4. **Ver Gráficos**
   - Selecciona "3. 📊 Ver Gráficos"
   - Elige entre 8 tipos diferentes de visualizaciones

## 📁 Formato de Datos

### Estructura del Archivo
- **Columnas de atributos**: Todas excepto la última
- **Columna de clase**: Última columna (debe ser binaria: 0/1)

### Ejemplo de Datos (tenis.csv)
```csv
Temperatura,Humedad,Viento,Jugar
> 32,3,1,0
> 32,3,3,0
> 32,3,1,1
25 - 32,3,1,1
< 25,2,1,1
...
```

## 🎨 Tipos de Visualizaciones

### Gráficos de Distribución
- **Barras**: Para mostrar frecuencias y conteos
- **Pastel**: Para mostrar proporciones y porcentajes
- **Líneas**: Para mostrar tendencias

### Gráficos de Análisis
- **Heatmaps**: Para matrices de correlación y contingencia
- **Barras horizontales**: Para rankings y comparaciones
- **Barras apiladas**: Para mostrar composición por categorías

### Dashboard Completo
- **12 subplots**: Vista general de todo el análisis
- **Información resumida**: Métricas principales y ranking

## 🔧 Configuración de Atributos

### Atributos Nominales
- Se mapean automáticamente a valores numéricos
- **1 = Bajo**, **2 = Normal**, **3 = Alto**

### Atributos Numéricos
- Se categorizan en rangos:
  - **< X1 = Bajo (1)**
  - **X1 - X2 = Normal (2)**
  - **> X2 = Alto (3)**

## 📊 Métricas Calculadas

### Entropía
- **Entropía General**: Medida de impureza del conjunto completo
- **Entropía por Valor**: Entropía de cada rama del nodo raíz

### Ganancia de Información
- **Cálculo**: Entropía General - Entropía Ponderada
- **Ranking**: Ordenamiento de atributos por ganancia

## 🎯 Consejos de Uso

1. **Para datos pequeños**: Usa todos los tipos de gráficos para explorar completamente
2. **Para presentaciones**: El "Resumen Completo" es ideal
3. **Para análisis detallado**: Usa gráficos específicos según tu interés
4. **Para comparar atributos**: El gráfico de "Ganancia de Información" es clave

## 🐛 Solución de Problemas

### Error: "No module named 'matplotlib'"
```bash
pip install matplotlib
```

### Error: "No module named 'seaborn'"
```bash
pip install seaborn
```

### Los gráficos no se muestran
- Asegúrate de ejecutar en un entorno con soporte gráfico
- En servidores remotos, usa `plt.savefig()` en lugar de `plt.show()`

### Error al cargar archivos
- Verifica que el archivo esté en el directorio correcto
- Asegúrate de que el formato sea CSV o Excel
- Revisa que la última columna sea la clase (binaria)

## 📈 Ejemplo de Salida

El programa generará gráficos como:
- Distribución de clases con porcentajes
- Ranking de atributos por ganancia de información
- Matrices de correlación con valores numéricos
- Distribuciones detalladas del nodo raíz
- Dashboard completo con múltiples visualizaciones

## 🤝 Contribuciones

Para mejorar el programa:
1. Agregar nuevos tipos de gráficos
2. Mejorar la estética de las visualizaciones
3. Agregar opciones de exportación de gráficos
4. Implementar análisis de árboles de decisión completos

## 📝 Licencia

Este proyecto es de uso educativo y puede ser modificado libremente. 