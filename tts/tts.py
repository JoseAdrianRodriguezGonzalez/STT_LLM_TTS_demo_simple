from TTS.api import TTS
import sounddevice as sd

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

def speak(text):
    print("Pasa al modelo")
    wav = tts.tts(text, speaker_wav="libro2.mp3", language="es")
    print("ya lo proceso")
    sd.play(wav, 22050)
    print("lo reproduce")
    sd.wait()