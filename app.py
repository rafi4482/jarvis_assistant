import streamlit as st
import speech_recognition as sr
import pyttsx3
from config.settings import Settings
from jarvis.gemini_engine import GeminiEngine
from jarvis.prompt_controller import PromptController
from jarvis.memory import Memory
from jarvis.assistant import JarvisAssistant

st.set_page_config(page_title="JARVIS", page_icon="🧠")

engine_tts = pyttsx3.init()
engine_tts.setProperty("rate", 170)

def speak(text):
    engine_tts.say(text)
    engine_tts.runAndWait()

def listen_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        return ""

settings = Settings()
engine = GeminiEngine(settings.load_api_key())
memory = Memory()
prompt_controller = PromptController()
assistant = JarvisAssistant(engine, prompt_controller, memory)

st.title("🧠 JARVIS – Your AI Assistant")

with st.sidebar:
    role = st.selectbox("Select Assistant Role", ["Tutor", "Coder", "Mentor"])
    voice_enabled = st.toggle("🔊 Voice Output", value=True)
    if st.button("Clear Memory"):
        memory.clear()
        st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.chat_input("Ask JARVIS...")

with col2:
    if st.button("🎤 Speak"):
        with st.spinner("Listening..."):
            user_input = listen_voice()

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response = assistant.respond(user_input, role)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    if voice_enabled:
        speak(response)
