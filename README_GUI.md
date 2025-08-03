# 🌳 Analizador de Entropía y Árboles de Decisión - Versión GUI

## 📋 Descripción

Esta es la versión con interfaz gráfica de usuario (GUI) del analizador de entropía y árboles de decisión. Proporciona una experiencia de usuario intuitiva y visual para analizar datos de clasificación sin necesidad de usar la línea de comandos.

## 🚀 Características de la GUI

### 🖥️ Interfaz Principal
- **Ventana principal** de 1200x800 píxeles
- **Controles intuitivos** con botones y campos de texto
- **Área de visualización** integrada para gráficos
- **Mensajes de estado** en tiempo real
- **Diálogos de selección** para archivos y opciones

### 📁 Gestión de Datos
- **Selector de archivos** con diálogo nativo del sistema
- **Soporte para CSV y Excel** (.csv, .xlsx, .xls)
- **Configuración automática** de atributos
- **Detección inteligente** de tipos de datos
- **Validación de archivos** con mensajes de error

### 🌳 Selección de Nodo Raíz
- **Ventana modal** para selección
- **Radio buttons** con ganancias de información
- **Ranking automático** de atributos
- **Indicador visual** del mejor atributo (🏆)
- **Confirmación** con botones de acción

### 📊 Visualizaciones Integradas
- **Canvas integrado** para gráficos matplotlib
- **8 tipos de gráficos** diferentes
- **Actualización dinámica** de visualizaciones
- **Gráficos interactivos** dentro de la GUI
- **Mensaje de bienvenida** informativo

## 🛠️ Instalación

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Sistema operativo con soporte gráfico

### Pasos de Instalación

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **O instalar manualmente:**
   ```bash
   pip install pandas numpy matplotlib seaborn openpyxl xlrd
   ```

**Nota:** `tkinter` viene incluido con Python, no necesita instalación adicional.

## 📖 Uso de la GUI

### Ejecutar el Programa

```bash
python Mena2_GUI.py
```

### Flujo de Trabajo con GUI

1. **Cargar Datos**
   - Haz clic en "📁 Buscar" para abrir el selector de archivos
   - Navega hasta tu archivo CSV o Excel
   - Haz clic en "📂 Cargar" para procesar los datos
   - El estado mostrará la confirmación

2. **Seleccionar Nodo Raíz**
   - Haz clic en "🌳 Seleccionar" para abrir la ventana de selección
   - Revisa las ganancias de información de cada atributo
   - Selecciona el atributo deseado con los radio buttons
   - Haz clic en "✅ Confirmar" para establecer el nodo raíz

3. **Explorar Gráficos**
   - Usa los 8 botones de gráficos disponibles
   - Cada gráfico se mostrará en el área de visualización
   - Los gráficos se actualizan dinámicamente
   - Puedes cambiar entre diferentes visualizaciones

## 🎨 Tipos de Gráficos Disponibles

### 📈 Distribución de Clases
- **Gráfico de barras** y **gráfico de pastel**
- Muestra la distribución entre clases positivas y negativas
- Porcentajes y conteos exactos

### 📊 Distribución de Atributos
- **Gráficos de barras** para cada atributo
- Muestra la frecuencia de valores (Bajo, Normal, Alto)
- Layout automático según número de atributos

### 🎯 Ganancia de Información
- **Gráfico de barras horizontal**
- Ranking de atributos por ganancia de información
- Marca el nodo raíz seleccionado con ⭐

### 🔗 Matriz de Correlación
- **Heatmap** de correlaciones entre atributos
- Valores numéricos en cada celda
- Escala de colores para interpretación

### 🌳 Distribución del Nodo Raíz
- **4 gráficos en uno**: barras apiladas, líneas, matriz de contingencia, pastel
- Análisis completo del nodo raíz seleccionado
- Relación con las clases objetivo

### 📉 Entropía por Valor
- **Gráfico de barras** de entropía para cada valor del nodo raíz
- Ayuda a entender la pureza de cada rama
- Valores numéricos en las barras

### 📋 Datos Originales
- **Visualización** de los datos antes de la transformación
- Útil para entender la distribución original
- Comparación con datos procesados

### 🎨 Resumen Completo
- **Dashboard** con 12 gráficos diferentes
- Vista general de todo el análisis
- Información resumida y métricas principales

## 🔧 Características Técnicas

### Configuración Automática
- **Detección automática** de tipos de atributos
- **Mapeo inteligente** de valores nominales
- **Categorización automática** de valores numéricos usando percentiles
- **Configuración de clases** binarias (0/1)

### Manejo de Errores
- **Validación de archivos** antes de cargar
- **Mensajes de error** descriptivos
- **Verificación de datos** en cada paso
- **Recuperación** de errores comunes

### Interfaz Responsiva
- **Grid layout** adaptable
- **Redimensionamiento** automático
- **Scroll** en áreas de texto largas
- **Ventanas modales** para selecciones

## 📁 Formato de Datos Soportado

### Estructura del Archivo
- **Columnas de atributos**: Todas excepto la última
- **Columna de clase**: Última columna (debe ser binaria: 0/1)
- **Formato**: CSV o Excel (.xlsx, .xls)

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

## 🎯 Ventajas de la GUI

### Fácil de Usar
- **Sin comandos** de terminal
- **Interfaz intuitiva** con botones y menús
- **Flujo visual** del proceso
- **Feedback inmediato** de acciones

### Visualización Integrada
- **Gráficos dentro de la aplicación**
- **No ventanas separadas** para gráficos
- **Navegación fácil** entre visualizaciones
- **Contexto visual** completo

### Gestión de Datos Simplificada
- **Selector de archivos** nativo
- **Configuración automática** de atributos
- **Validación visual** de datos
- **Estado visible** del proceso

## 🐛 Solución de Problemas

### Error: "No module named 'tkinter'"
- En Linux: `sudo apt-get install python3-tk`
- En macOS: `brew install python-tk`
- En Windows: Reinstalar Python con tkinter incluido

### Los gráficos no se muestran
- Verifica que matplotlib esté instalado: `pip install matplotlib`
- Asegúrate de ejecutar en un entorno con soporte gráfico
- En servidores remotos, usa la versión de línea de comandos

### Error al cargar archivos
- Verifica el formato del archivo (CSV o Excel)
- Asegúrate de que la última columna sea la clase
- Revisa que no haya caracteres especiales en los nombres de columnas

### La GUI no responde
- Verifica que no haya procesos bloqueando
- Reinicia la aplicación
- Comprueba la memoria disponible del sistema

## 📈 Comparación con Versiones

| Característica | Versión CLI | Versión Gráficos | Versión GUI |
|----------------|-------------|------------------|-------------|
| Facilidad de uso | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Visualización | ❌ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Interactividad | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Configuración | Manual | Manual | Automática |
| Experiencia | Técnica | Técnica | Intuitiva |

## 🤝 Contribuciones

Para mejorar la GUI:
1. Agregar más opciones de personalización
2. Implementar guardado de configuraciones
3. Agregar exportación de gráficos
4. Mejorar la accesibilidad
5. Agregar temas visuales

## 📝 Licencia

Este proyecto es de uso educativo y puede ser modificado libremente.

## 🎉 ¡Disfruta usando la GUI!

La versión GUI hace que el análisis de entropía y árboles de decisión sea accesible para todos, sin necesidad de conocimientos técnicos avanzados. 