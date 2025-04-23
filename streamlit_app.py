import streamlit as st
from agent import *

# Configuracion de la interfaz de Streamlit
st.title("Chatbot Multi-Agente con Razonamiento")
st.write("Resuelve preguntas complejas usando agentes especializados y midiendo el uso de tokens.")

# Entrada del usuario
pregunta = st.text_area("Escribe tu pregunta compleja:")

if st.button("Enviar"):
    with st.spinner("Procesando con agentes..."):
        result = solve_complex_question(pregunta)

        st.subheader("Respuesta Final")
        st.write(result["answer"])

        st.subheader("Tokens Utilizados")
        col1, col2, col3 = st.columns(3)
        col1.metric("Entrada", result["tokens"]["input"])
        col2.metric("Salida", result["tokens"]["output"])
        col3.metric("Razonamiento", result["tokens"]["reasoning"])
        st.metric("Total de Tokens", result["tokens"]["total"])

        # Mostrar historial de cada agente
        st.subheader("📜 Proceso de Razonamiento (Detalle por Agente)")
        for agent_name, agent_obj in result["agents"].items():
            with st.expander(f"⚙️ {agent_name} (Tokens: {agent_obj.token_counter['total']})"):
                for msg in agent_obj.messages:
                    emoji = "👤" if msg["role"] == "user" else "🤖"
                    content = str(msg.get("content", "")).replace("`", "'")
                    st.markdown(f"{emoji} **{msg['role']}:** {content}")