import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64

def text_to_speech_gtts(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return audio_file

st.title("Text-to-Speech Conversion")
text = st.text_area("Enter text to convert to speech:")

lang = st.selectbox("Select language:", ['en', 'es', 'fr', 'de', 'it'])

if st.button("Convert"):
    if text:
        audio_file = text_to_speech_gtts(text, lang)
        st.audio(audio_file, format='audio/mp3')
        st.success("Conversion successful!")
    else:
        st.warning("Please enter text to convert.")
