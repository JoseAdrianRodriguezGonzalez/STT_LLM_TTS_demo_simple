import sounddevice as sd
from faster_whisper import WhisperModel
def test():
    samplerate=16000
    model=WhisperModel(
        "small",
        device="cuda",
        compute_type="float16"
    )
    print("habla...")
    audio=sd.rec(int(5*samplerate),samplerate=samplerate,channels=1)
    sd.wait()
    audio=audio.flatten()
    segments, _ =model.transcribe(audio,language="es")
    text="".join([s.text for s in segments])
    return text.strip()