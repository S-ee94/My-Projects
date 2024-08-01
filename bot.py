# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:43:12 2024

@author: seema
"""

import streamlit as st
import speech_recognition as sr
import io
from tempfile import NamedTemporaryFile
import wave
import os
import sounddevice as sd
import numpy as np

# Function to recognize speech from audio data
def recognize_speech(audio_data, sample_rate, sample_width):
    recognizer = sr.Recognizer()
    audio = sr.AudioData(audio_data, sample_rate, sample_width)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Sorry, the speech recognition service is not available."

# Streamlit UI
st.title("AI Voice Recognition Bot")
st.write("Record your voice message and get the recognized text.")

# Record audio
audio_file = st.file_uploader("Upload an audio file (WAV format)", type=["wav"])

if audio_file is not None:
    st.audio(audio_file, format="audio/wav")

    # Read the uploaded file
    audio_data = audio_file.read()
    
    # Use wave to get sample rate and sample width
    with wave.open(io.BytesIO(audio_data), 'rb') as wf:
        sample_rate = wf.getframerate()
        sample_width = wf.getsampwidth()
        audio_data = wf.readframes(wf.getnframes())

    # Recognize speech from the audio data
    recognized_text = recognize_speech(audio_data, sample_rate, sample_width)
    st.write("Recognized Text:")
    st.write(recognized_text)

# Optional: Record audio using the microphone
st.write("Or record your voice directly:")

# Create a temporary file for recording
temp_file = NamedTemporaryFile(delete=False, suffix=".wav")
temp_file.close()

if st.button("Record Audio"):
    # Parameters for recording
    fs = 16000
    duration = 5  # seconds

    st.write("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    st.write("Recording finished.")

    # Save the recorded audio
    with wave.open(temp_file.name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(audio_data.tobytes())

    # Read the recorded audio
    with open(temp_file.name, 'rb') as f:
        audio_data = f.read()

    # Use wave to get sample rate and sample width
    with wave.open(io.BytesIO(audio_data), 'rb') as wf:
        sample_rate = wf.getframerate()
        sample_width = wf.getsampwidth()
        audio_data = wf.readframes(wf.getnframes())

    # Recognize speech from the recorded audio
    recognized_text = recognize_speech(audio_data, sample_rate, sample_width)
    st.write("Recognized Text:")
    st.write(recognized_text)

    # Clean up the temporary file
    os.remove(temp_file.name)
