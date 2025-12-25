import streamlit as st
from config.settings import Settings
from jarvis.gemini_engine import GeminiEngine
from jarvis.prompt_controller import PromptController
from jarvis.memory import Memory
from jarvis.assistant import JarvisAssistant

st.set_page_config(page_title="JARVIS", page_icon="🧠")

settings = Settings()
engine = GeminiEngine(settings.load_api_key())
memory = Memory()
prompt_controller = PromptController()
assistant = JarvisAssistant(engine, prompt_controller, memory)

st.title("🧠 JARVIS – Your AI Assistant")

with st.sidebar:
    role = st.selectbox("Select Assistant Role", ["Tutor", "Coder", "Mentor"])
    if st.button("Clear Memory"):
        memory.clear()
        st.success("Memory cleared")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask JARVIS...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("assistant"):
        response = assistant.respond(user_input, role)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
