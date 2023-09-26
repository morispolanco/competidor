import openai
import streamlit as st

def assistant():
    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        
    st.title("💬 Análisis de la competencia")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key

    prompt = "Analizar el sitio web de mi competidor, observando sus productos o servicios, ventajas y beneficios. Con base en su análisis, sugiera estrategias y acciones para superar a mi competencia. Considere factores como el diseño del sitio web, la usabilidad, la calidad del producto / servicio, los precios, las ofertas especiales, el servicio al cliente y otros factores relevantes. Proporcionar una respuesta detallada con recomendaciones prácticas y viables para mejorar mi posición competitiva. Tómese su tiempo. "
  
    if prompt:
        st.session_state.messages.append({"role": "assistant", "content": prompt})

    user_input = st.text_input("Igrese URL")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)

    if st.button("Generate Optimized Prompt"):
        optimized_prompt = generate_optimized_prompt(prompt)
        st.session_state.messages.append({"role": "assistant", "content": optimized_prompt})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)

def generate_optimized_prompt(prompt):
    # Aquí puedes agregar tu lógica para generar el prompt optimizado
    optimized_prompt = prompt + " [Optimized]"
    return optimized_prompt

assistant()
