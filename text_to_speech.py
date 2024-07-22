import gtts
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

def text_to_speech(msg):
    audio_array = generate_audio(msg)
    write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

