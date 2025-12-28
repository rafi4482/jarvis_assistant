# 🧠 JARVIS - AI Assistant

A conversational AI assistant powered by Google Gemini, built with Streamlit. JARVIS supports multiple roles (Tutor, Coder, Mentor) and features voice interaction capabilities with conversation memory.

## ✨ Features

- **Multi-Role Support**: Switch between Tutor, Coder, and Mentor personas
- **Voice Interaction**: Speak your queries and receive voice responses
- **Conversation Memory**: Maintains context across interactions using persistent memory
- **Modern UI**: Clean and intuitive Streamlit-based interface
- **Google Gemini Integration**: Powered by Gemini 2.5 Flash model for fast, accurate responses

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Engine**: Google Generative AI (Gemini 2.5 Flash)
- **Speech Recognition**: SpeechRecognition + PyAudio
- **Text-to-Speech**: pyttsx3
- **Memory**: JSON-based persistent storage

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- Microphone (for voice input)


## 📖 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Using JARVIS**
   - Select a role from the sidebar (Tutor, Coder, or Mentor)
   - Type your question in the chat input or click the microphone button for voice input
   - Toggle voice output on/off as needed
   - Use "Clear Memory" to reset conversation history

## 📁 Project Structure

```
jarvis_assistant/
├── app.py                      # Main Streamlit application
├── config/
│   └── settings.py            # Configuration and API key management
├── jarvis/
│   ├── assistant.py           # Main assistant class
│   ├── gemini_engine.py       # Google Gemini integration
│   ├── memory.py              # Conversation memory management
│   └── prompt_controller.py   # Prompt building and role management
├── memory.json                # Conversation history storage (auto-generated)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```


## 🎯 Roles

- **Tutor**: Explains concepts clearly and patiently, ideal for learning
- **Coder**: Acts as a senior software engineer, helps with coding questions
- **Mentor**: Provides career guidance and practical advice

## 📝 Dependencies

- `streamlit` - Web framework
- `google-generativeai` - Google Gemini API client
- `python-dotenv` - Environment variable management
- `speechrecognition` - Speech-to-text functionality
- `pyaudio` - Audio I/O for microphone access
- `pyttsx3` - Text-to-speech engine
