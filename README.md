# Chatbot Multi-Agente con Razonamiento
Este proyecto implementa un sistema de resolución de preguntas complejas mediante un enfoque multi-agente,
donde cada agente especializado realiza una parte del proceso de razonamiento.
El sistema mide y muestra el consumo de tokens en cada fase del proceso.

## Características principales
- Arquitectura multi-agente: 4 agentes especializados trabajan en conjunto:
  - **Investigador**: Recopila información relevante
  - **Analista**: Extrae patrones y detalles técnicos
  - **Crítico**: Identifica posibles errores o riesgos
  - **Coordinador**: Sintetiza la respuesta final

- Transparencia en el proceso:
  - Muestra el razonamiento intermedio de cada agente
  - Proporciona métricas detalladas del uso de tokens
  - Permite inspeccionar el historial completo de conversaciones

## Estructura del proyecto
El proyecto está dividido en<>

1. **`notebook.ipynb`**:
   - Notebook interactivo para realizar pruebas.

2. **`streamlit_app.py`**:
   - Archivo independiente que implementa la interfaz gráfica del chatbot usando Streamlit.
   - Permite al usuario interactuar con el sistema de manera sencilla.

3. **`agent.py`**:
   - Implementación central del sistema multi-agente.
   - Incluye la clase `Agent` y la función `solve_complex_question()` para orquestar el flujo de trabajo.


## Requisitos

### Software
- Python 3.8 o superior
- Jupyter Notebook
- Streamlit

### Bibliotecas
Instalar las bibliotecas listadas en `requirements.txt` usando `pip`:

```bash
pip install -r requirements.txt
```

### Variables de Entorno
- `GROQ_API_KEY`: clave API Groq Cloud
- `GROQ_MODEL`: modelo LLM a utilizar (por defecto `llama3-70b-8192`)

## Ejecución

1. Notebook interactivo
   - Abrir el archivo `notebook.ipynb` en Jupyter Notebook.
   - Ejecutar las celdas para probar el sistema.

2. Interfaz gráfica con Streamlit
   - Ejecutar el siguiente comando: `streamlit run streamlit_app.py`
   - Se abrirá una ventana en el navegador con la interfaz gráfica del chatbot.


## Ejemplo

![ejemplo.mp4](media/ejemplo.mp4)
